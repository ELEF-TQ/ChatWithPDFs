css = '''
<style>
/* Chat Container Styling */
.chat-container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    background-color: #f4f6f9;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    height: 80vh;
    overflow-y: auto;
}

/* Chat Message Bubbles */
.chat-message {
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.chat-message.user {
    background-color: #e9ecef;
    border: 1px solid #6c757d;
}

.chat-message.bot {
    background-color: #d1e7ff;
    border: 1px solid #007bff;
}

/* Avatar Styling */
.chat-message .avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin-right: 15px;
    overflow: hidden;
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Message Content */
.chat-message .message {
    max-width: calc(100% - 80px);
    word-wrap: break-word;
    font-size: 16px;
    color: #343a40;
}

/* Custom Scrollbar */
.chat-container::-webkit-scrollbar {
    width: 8px;
}

.chat-container::-webkit-scrollbar-thumb {
    background-color: #007bff;
    border-radius: 10px;
}

.chat-container::-webkit-scrollbar-track {
    background-color: #f4f6f9;
}

/* Chat Input Section */
.chat-input {
    margin-top: 20px;
    display: flex;
    align-items: center;
    border-top: 2px solid #e0e0e0;
    padding-top: 10px;
}

.chat-input textarea {
    flex: 1;
    padding: 15px;
    border: none;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    resize: none;
    font-size: 16px;
    outline: none;
}

.chat-input button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    margin-left: 10px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    font-size: 16px;
}

.chat-input button:hover {
    background-color: #0056b3;
}

/* Header Styling */
header {
    text-align: center;
    margin-bottom: 20px;
}

header h1 {
    color: #007bff;
    font-size: 32px;
    font-weight: bold;
}

header p {
    color: #6c757d;
    font-size: 16px;
}
</style>
'''


bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/VDgZ52s/robot.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/XCD0CDC/employe.png" alt="User Avatar">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

