// ============================================================
// CHATBOT WIDGET
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    var chatbotWidget = document.getElementById('chatbot-widget');
    var chatbotToggle = document.getElementById('chatbotToggle');
    var chatbotClose = document.getElementById('chatbotClose');
    var chatbotInput = document.getElementById('chatbotInput');
    var chatbotSend = document.getElementById('chatbotSend');
    var chatbotMessages = document.getElementById('chatbotMessages');
    var openChatbotBtn = document.getElementById('openChatbotBtn');

    var isOpen = false;
    var isProcessing = false;

    var API_URL = 'https://arkan-chatbot.arkan-chatbot.workers.dev/api/chat';

    // ============================================================
    // TOGGLE CHATBOT
    // ============================================================
    function toggleChatbot() {
        isOpen = !isOpen;
        if (isOpen) {
            chatbotWidget.classList.add('open');
            chatbotToggle.style.display = 'none';
            chatbotInput.focus();
        } else {
            chatbotWidget.classList.remove('open');
            chatbotToggle.style.display = 'flex';
        }
    }

    function openChatbot() {
        if (!isOpen) {
            toggleChatbot();
        }
    }

    function closeChatbot() {
        if (isOpen) {
            toggleChatbot();
        }
    }

    // ============================================================
    // MESSAGE HANDLING
    // ============================================================
    function addMessage(message, sender) {
        var messageDiv = document.createElement('div');
        messageDiv.className = 'message ' + sender;

        var bubble = document.createElement('div');
        bubble.className = 'message-bubble';
        bubble.textContent = message;

        messageDiv.appendChild(bubble);
        chatbotMessages.appendChild(messageDiv);
        scrollToBottom();
    }

    function showTyping() {
        var typingDiv = document.createElement('div');
        typingDiv.className = 'message bot';
        typingDiv.id = 'typingIndicator';

        var bubble = document.createElement('div');
        bubble.className = 'message-bubble typing-indicator active';
        bubble.innerHTML = '<span></span><span></span><span></span>';

        typingDiv.appendChild(bubble);
        chatbotMessages.appendChild(typingDiv);
        scrollToBottom();
    }

    function removeTyping() {
        var typingIndicator = document.getElementById('typingIndicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    function scrollToBottom() {
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }

    // ============================================================
    // SEND MESSAGE
    // ============================================================
    async function sendMessage() {
        var question = chatbotInput.value.trim();

        if (!question || isProcessing) {
            return;
        }

        addMessage(question, 'user');
        chatbotInput.value = '';
        isProcessing = true;
        chatbotSend.disabled = true;

        showTyping();

        try {
            var response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question: question })
            });

            if (!response.ok) {
                throw new Error('API request failed with status ' + response.status);
            }

            var data = await response.json();
            var botResponse = data.response || 'I am unable to answer that at the moment.';

            removeTyping();
            addMessage(botResponse, 'bot');

        } catch (error) {
            console.error('Chatbot Error:', error);
            removeTyping();
            addMessage('Sorry, I encountered an error. Please try again later.', 'bot');
        } finally {
            isProcessing = false;
            chatbotSend.disabled = false;
            chatbotInput.focus();
        }
    }

    // ============================================================
    // EVENT LISTENERS
    // ============================================================
    if (chatbotToggle) {
        chatbotToggle.addEventListener('click', toggleChatbot);
    }

    if (chatbotClose) {
        chatbotClose.addEventListener('click', closeChatbot);
    }

    if (chatbotSend) {
        chatbotSend.addEventListener('click', sendMessage);
    }

    if (chatbotInput) {
        chatbotInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                sendMessage();
            }
        });
    }

    if (openChatbotBtn) {
        openChatbotBtn.addEventListener('click', openChatbot);
    }

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && isOpen) {
            closeChatbot();
        }
    });
});