// messenger.js
document.addEventListener("DOMContentLoaded", function () {
    const usersList = document.getElementById("users-list");
    const conversation = document.getElementById("conversation");
    const messageInput = document.getElementById("message-input");
    const sendMessageBtn = document.getElementById("send-message");

    // Mock data for users and conversation
    const users = ["User1", "User2", "User3"];
    const conversationData = {
        "User1": ["Hello!", "How are you?"],
        "User2": ["Hi there!", "I'm good, thanks."],
        "User3": ["Hey!", "What's up?"]
    };

    // Populate users list
    users.forEach(user => {
        const listItem = document.createElement("li");
        listItem.textContent = user;
        listItem.addEventListener("click", () => loadConversation(user));
        usersList.appendChild(listItem);
    });

    // Load initial conversation (example: User1)
    loadConversation("User1");

    // Function to load and display conversation
    function loadConversation(user) {
        conversation.innerHTML = ""; // Clear previous conversation
        const messages = conversationData[user] || [];
        messages.forEach(message => displayMessage(message));
    }

    // Function to display a message in the conversation
    function displayMessage(message) {
        const messageElement = document.createElement("div");
        messageElement.textContent = message;
        conversation.appendChild(messageElement);
    }

    // Function to send a message
    function sendMessage() {
        const user = "User1"; // Assuming the logged-in user is User1
        const message = messageInput.value;
        if (message.trim() !== "") {
            // Update the conversation data
            conversationData[user] = conversationData[user] || [];
            conversationData[user].push(message);

            // Display the message in the conversation
            displayMessage(message);

            // Clear the input field
            messageInput.value = "";
        }
    }

    // Event listener for send message button
    sendMessageBtn.addEventListener("click", sendMessage);
});
