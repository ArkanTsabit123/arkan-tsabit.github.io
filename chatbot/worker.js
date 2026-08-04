// ============================================================
// CLOUDFLARE WORKER - RAG CHATBOT
// ============================================================

/**
 * Cloudflare Worker for RAG-powered chatbot.
 * Uses Cloudflare Vectorize for vector search and Cloudflare Workers AI for LLM.
 */

export default {
    async fetch(request, env, ctx) {
        // Handle CORS preflight
        if (request.method === 'OPTIONS') {
            return new Response(null, {
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type',
                },
            });
        }

        const url = new URL(request.url);

        // Health check endpoint
        if (url.pathname === '/health') {
            return new Response(JSON.stringify({
                status: 'healthy',
                service: 'arkan-chatbot',
                version: '1.0.0',
                timestamp: new Date().toISOString(),
            }), {
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
            });
        }

        // Chat endpoint
        if (url.pathname === '/api/chat' && request.method === 'POST') {
            try {
                const body = await request.json();
                const question = body.question;

                if (!question || typeof question !== 'string' || question.trim().length === 0) {
                    return new Response(JSON.stringify({
                        error: 'Question is required',
                        response: 'Please ask a question about Arkan.',
                    }), {
                        status: 400,
                        headers: {
                            'Content-Type': 'application/json',
                            'Access-Control-Allow-Origin': '*',
                        },
                    });
                }

                // Generate embedding for the question
                const embeddingResponse = await env.AI.run('@cf/baai/bge-small-en-v1.5', {
                    text: question.trim(),
                });

                const embedding = embeddingResponse.data[0];

                // Perform vector search
                const vectorResults = await env.VECTORIZE.query(embedding, {
                    topK: 5,
                    returnValues: true,
                    returnMetadata: true,
                });

                // Build context from search results
                let context = '';
                if (vectorResults.matches && vectorResults.matches.length > 0) {
                    const relevantDocs = vectorResults.matches
                        .filter(match => match.score > 0.3)
                        .map(match => match.value)
                        .join('\n\n');

                    if (relevantDocs) {
                        context = relevantDocs;
                    }
                }

                // If no context found, use default response
                if (!context) {
                    return new Response(JSON.stringify({
                        response: "I don't have specific information about that topic. Please ask about Arkan's experience, projects, certifications, or skills.",
                        source: 'default',
                    }), {
                        headers: {
                            'Content-Type': 'application/json',
                            'Access-Control-Allow-Origin': '*',
                        },
                    });
                }

                // Generate response using LLM
                const prompt = `
You are Arkan's AI assistant. Answer questions based ONLY on the provided context.
If the answer is not in the context, say "I don't have that information."

Context:
${context}

Question: ${question}

Answer:`;

                const llmResponse = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
                    messages: [
                        {
                            role: 'system',
                            content: 'You are Arkan\'s AI assistant. Answer questions based ONLY on the provided context. If the answer is not in the context, say "I don\'t have that information." Be concise and professional.',
                        },
                        {
                            role: 'user',
                            content: prompt,
                        },
                    ],
                    temperature: 0.3,
                    max_tokens: 500,
                });

                return new Response(JSON.stringify({
                    response: llmResponse.response || 'I am unable to answer that right now.',
                    source: 'llm',
                }), {
                    headers: {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*',
                    },
                });

            } catch (error) {
                console.error('Chatbot error:', error);
                return new Response(JSON.stringify({
                    error: 'Internal server error',
                    response: 'I am having trouble connecting right now. Please try again later.',
                }), {
                    status: 500,
                    headers: {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*',
                    },
                });
            }
        }

        // Handle unknown routes
        return new Response(JSON.stringify({
            error: 'Not found',
            message: 'The requested endpoint does not exist.',
        }), {
            status: 404,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
        });
    },
};