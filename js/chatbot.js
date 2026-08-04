// Chatbot Integration

function sendMessage() {
    const input = document.getElementById('chatbot-input');
    const message = input.value;
    // Send to Cloudflare Worker
    console.log('Sending:', message);
}