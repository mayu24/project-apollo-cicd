async function sendMessage() {
    const userMessage = document.getElementById("userInput").value;
    const responseBox = document.getElementById("aiResponse");

    responseBox.innerText = "Thinking...";

    try {
        const res = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await res.json();
        responseBox.innerText = data.reply;
    } catch (error) {
        responseBox.innerText = "Error: " + error;
    }
}
