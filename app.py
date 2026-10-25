from flask import Flask, request
import os
app = Flask(__name__)

SYSTEM = "You are ArewaMoney AI, Hausa fintech for market traders. Answer in Hausa, friendly."

@app.route("/")
def home():
    return "ArewaMoney AI is Live - From Yola to Dubai!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    msg = data.get("message", "Sannu")
    # Here connect Llama 3.3 API
    reply = f"ArewaMoney AI: Na ji ka - '{msg}'. Ribarka yau: 15000. Allah ya albarkaci kasuwanci!"
    return {"reply": reply}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
