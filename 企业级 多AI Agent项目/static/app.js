async function send() {
    const input = document.getElementById("input");
    const msg = input.value.trim();
    if (!msg) return;

    const box = document.getElementById("msg-box");
    box.innerHTML += `<div class='user'>你：${msg}</div>`;
    input.value = "";

    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    });

    const data = await res.json();
    box.innerHTML += `<div class='agent'>AI：${data.reply}</div>`;
    box.scrollTop = box.scrollHeight;
}

document.getElementById("input").addEventListener("keypress", (e) => {
    if (e.key === "Enter") send();
});