from flask import Flask, render_template, request
from chatbot import chatbot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def chatbot():
    user_text = request.args.get("msg")
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)
