// ============================================================
// RAG CHATBOT INTEGRATION
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // DOM Elements
    const chatbotWidget = document.getElementById('chatbot-widget');
    const chatbotToggle = document.getElementById('chatbotToggle');
    const chatbotClose = document.getElementById('chatbotClose');
    const chatbotInput = document.getElementById('chatbotInput');
    const chatbotSend = document.getElementById('chatbotSend');
    const chatbotMessages = document.getElementById('chatbotMessages');

    let isOpen = false;

    // ============================================================
    // TOGGLE CHATBOT
    // ============================================================
    function toggleChatbot() {
        isOpen = !isOpen;
        chatbotWidget.classList.toggle('open', isOpen);
        chatbotToggle.style.display = isOpen ? 'none' : 'flex';

        if (isOpen) {
            chatbotInput.focus();
        }
    }

    // ============================================================
    // ADD MESSAGE
    // ============================================================
    function addMessage(text, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;

        const bubble = document.createElement('div');
        bubble.className = 'message-bubble';
        bubble.textContent = text;

        messageDiv.appendChild(bubble);
        chatbotMessages.appendChild(messageDiv);
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }

    // ============================================================
    // SHOW TYPING INDICATOR
    // ============================================================
    function showTyping() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'typing-indicator active';
        typingDiv.id = 'typingIndicator';

        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('span');
            typingDiv.appendChild(dot);
        }

        const messageDiv = document.createElement('div');
        messageDiv.className = 'message bot';
        messageDiv.appendChild(typingDiv);
        chatbotMessages.appendChild(messageDiv);
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }

    // ============================================================
    // HIDE TYPING INDICATOR
    // ============================================================
    function hideTyping() {
        const typing = document.getElementById('typingIndicator');
        if (typing) {
            const parent = typing.closest('.message');
            if (parent) {
                parent.remove();
            }
        }
    }

    // ============================================================
    // SEND MESSAGE TO CLOUDFLARE WORKER
    // ============================================================
    async function sendMessageToWorker(message) {
        try {
            const response = await fetch('https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question: message }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            return data.response || 'I am unable to answer that right now. Please try again.';
        } catch (error) {
            console.error('Chatbot API error:', error);
            return 'I am having trouble connecting right now. Please try again later.';
        }
    }

    // ============================================================
    // HANDLE USER MESSAGE
    // ============================================================
    async function handleUserMessage() {
        const message = chatbotInput.value.trim();
        if (!message) return;

        // Clear input
        chatbotInput.value = '';

        // Add user message
        addMessage(message, 'user');

        // Show typing indicator
        showTyping();

        try {
            // Get response from worker
            const response = await sendMessageToWorker(message);

            // Hide typing indicator
            hideTyping();

            // Add bot response
            addMessage(response, 'bot');
        } catch (error) {
            hideTyping();
            addMessage('Sorry, an error occurred. Please try again later.', 'bot');
        }
    }

    // ============================================================
    // EVENT LISTENERS
    // ============================================================
    if (chatbotToggle) {
        chatbotToggle.addEventListener('click', toggleChatbot);
    }

    if (chatbotClose) {
        chatbotClose.addEventListener('click', toggleChatbot);
    }

    if (chatbotSend) {
        chatbotSend.addEventListener('click', handleUserMessage);
    }

    if (chatbotInput) {
        chatbotInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                handleUserMessage();
            }
        });
    }

    // ============================================================
    // INITIALIZE
    // ============================================================
    // Ensure chatbot is closed on load
    chatbotWidget.classList.remove('open');
    chatbotToggle.style.display = 'flex';

    console.log('Chatbot: Initialized');
});