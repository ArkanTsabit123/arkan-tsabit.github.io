// ============================================================
// CLOUDFLARE WORKER - RAG CHATBOT
// ============================================================

export default {
    async fetch(request, env, ctx) {
        if (request.method === 'OPTIONS') {
            return handleCors();
        }

        const url = new URL(request.url);

        if (url.pathname === '/health') {
            return handleHealthCheck();
        }

        if (url.pathname === '/api/chat' && request.method === 'POST') {
            return handleChatRequest(request, env);
        }

        return handleNotFound();
    },
};

function handleCors() {
    return new Response(null, {
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        },
    });
}

function handleHealthCheck() {
    return new Response(
        JSON.stringify({
            status: 'healthy',
            service: 'arkan-chatbot',
            version: '2.0.0',
            timestamp: new Date().toISOString(),
        }),
        {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
        }
    );
}

function handleNotFound() {
    return new Response(
        JSON.stringify({
            error: 'Not found',
            message: 'The requested endpoint does not exist.',
        }),
        {
            status: 404,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
        }
    );
}

async function handleChatRequest(request, env) {
    try {
        const body = await request.json();
        const question = body.question;

        if (!question || typeof question !== 'string' || question.trim().length === 0) {
            return createErrorResponse('Question is required', 400);
        }

        const embedding = await generateEmbedding(question, env);
        if (!embedding) {
            console.error('Failed to generate embedding');
            return createErrorResponse('Failed to generate embedding', 500);
        }

        const searchResults = await queryVectorize(embedding, env);

        const context = buildContext(searchResults);

        if (!context) {
            return createDefaultResponse();
        }

        const answer = await generateAnswer(question, context, env);
        return createSuccessResponse(answer);

    } catch (error) {
        console.error('Chatbot error:', error);
        return createErrorResponse('Internal server error', 500);
    }
}

async function generateEmbedding(question, env) {
    try {
        const response = await env.AI.run('@cf/baai/bge-small-en-v1.5', {
            text: question.trim(),
        });

        if (!response || !response.data) {
            console.error('AI response invalid');
            return null;
        }

        return response.data[0];
    } catch (error) {
        console.error('Embedding error:', error);
        return null;
    }
}

async function queryVectorize(embedding, env) {
    try {
        const result = await env.VECTORIZE.query(embedding, {
            topK: 5,
            returnValues: false,
            returnMetadata: true,
        });
        
        // Debug logging
        if (result.matches && result.matches.length > 0) {
            if (result.matches[0].metadata) {
            }
        }
        
        return result;
    } catch (error) {
        console.error('Vectorize query error:', error);
        return { matches: [] };
    }
}

function buildContext(searchResults) {
    if (!searchResults.matches || searchResults.matches.length === 0) {
        console.log('No matches found');
        return null;
    }

    const contents = [];

    for (const match of searchResults.matches) {
        
        let content = '';

        // Try to extract content from metadata
        if (match.metadata) {
            // Priority order: content > text > description > name
            content = match.metadata.content || 
                      match.metadata.text || 
                      match.metadata.description || 
                      match.metadata.name || 
                      '';
            
            // If still empty, try to join all string values
            if (!content) {
                const stringValues = Object.values(match.metadata)
                    .filter(v => typeof v === 'string' && v.length > 0);
                if (stringValues.length > 0) {
                    content = stringValues.join(' ');
                }
            }
        }

        // If still empty, try using match.content (if exists)
        if (!content && match.content) {
            content = match.content;
        }

        // If still empty, use id as fallback
        if (!content && match.id) {
            content = match.id;
        }

        // Add to contents if we have meaningful content
        if (content && content.length > 0) {
            contents.push(content);
        }
    }

    if (contents.length === 0) {
        console.log('No content extracted from matches');
        return null;
    }

    const context = contents.join('\n\n');
    return context;
}

async function generateAnswer(question, context, env) {
    // Use full context (max 500 chars)
    const truncatedContext = context.length > 500 ? context.substring(0, 500) + '...' : context;

    const prompt = `Answer based ONLY on this context. If the answer is not in the context, say "I don't know".

Context:
${truncatedContext}

Question: ${question}

Answer:`;

    try {
        const response = await env.AI.run('@cf/mistral/mistral-7b-instruct-v0.2-lora', {
            messages: [
                {
                    role: 'system',
                    content: 'You are a helpful assistant. Answer based ONLY on the context given. Be concise and informative. If the answer is not in the context, say "I don\'t know."',
                },
                {
                    role: 'user',
                    content: prompt,
                },
            ],
            temperature: 0.2,
            max_tokens: 250,
        });

        return response.response || 'No response from LLM.';
    } catch (error) {
        console.error('LLM error:', error);
        return 'LLM error: ' + error.message;
    }
}

function createDefaultResponse() {
    return new Response(
        JSON.stringify({
            response: "I don't have specific information about that topic. Please ask about Arkan's experience, projects, certifications, or skills.",
            source: 'default',
        }),
        {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
        }
    );
}

function createSuccessResponse(answer) {
    return new Response(
        JSON.stringify({
            response: answer,
            source: 'llm',
        }),
        {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
        }
    );
}

function createErrorResponse(message, status = 500) {
    return new Response(
        JSON.stringify({
            error: message,
            response: 'I am having trouble connecting right now. Please try again later.',
        }),
        {
            status: status,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
        }
    );
}