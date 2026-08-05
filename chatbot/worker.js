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
        console.log('Vectorize matches:', searchResults.matches?.length || 0);

        const context = buildContext(searchResults);
        console.log('Context built:', context ? 'YES' : 'NO');

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
        return await env.VECTORIZE.query(embedding, {
            topK: 5,
            returnValues: false,
            returnMetadata: true,
        });
    } catch (error) {
        console.error('Vectorize query error:', error);
        return { matches: [] };
    }
}

function buildContext(searchResults) {
    if (!searchResults.matches || searchResults.matches.length === 0) {
        return null;
    }

    const contents = [];

    for (const match of searchResults.matches) {
        console.log(`Match: id=${match.id}, score=${match.score}`);

        let content = match.content || match.metadata?.content || match.metadata?.text || '';

        if (!content && match.id) {
            content = match.id;
        }

        if (content && content.length > 0) {
            contents.push(content);
        }
    }

    if (contents.length === 0) {
        return null;
    }

    return contents.join('\n\n');
}

async function generateAnswer(question, context, env) {
    const truncatedContext = context.length > 300 ? context.substring(0, 300) + '...' : context;

    const prompt = `Answer based ONLY on this context: ${truncatedContext}

Question: ${question}

Answer:`;

    try {
        const response = await env.AI.run('@cf/mistral/mistral-7b-instruct-v0.2-lora', {
            messages: [
                {
                    role: 'system',
                    content: 'You are a helpful assistant. Answer based ONLY on the context given. Be concise.',
                },
                {
                    role: 'user',
                    content: prompt,
                },
            ],
            temperature: 0.2,
            max_tokens: 150,
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