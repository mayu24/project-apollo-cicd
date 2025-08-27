from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# 🔹 Configure your OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]

    # Call OpenAI Chat API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",   # You can use gpt-4 if you have access
        messages=[{"role": "user", "content": user_message}]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
