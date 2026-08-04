// Cloudflare Worker - RAG Chatbot

export default {
  async fetch(request, env, ctx) {
    return new Response('Hello from Arkan\'s AI Chatbot!');
  }
};
