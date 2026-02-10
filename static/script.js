function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (message === "") return;

    const chatBox = document.getElementById("chat-box");

    // Show user message
    chatBox.innerHTML += `<div><b>You:</b> ${message}</div>`;
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div><b>Bot:</b> ${data.reply}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        chatBox.innerHTML += `<div style="color:red;">Error: ${error}</div>`;
    });
}
