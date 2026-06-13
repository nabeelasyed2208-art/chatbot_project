from flask import Flask, request, render_template_string

app = Flask(__name__)

chat_history = []

html = """
<h1>My AI Chatbot ??</h1>

<form method="POST">
  <input name="message" placeholder="Type message..." required>
  <button type="submit">Send</button>
</form>

{% for msg in chat %}
<p><b>You:</b> {{ msg.user }}</p>
<p><b>Bot:</b> {{ msg.bot }}</p>
<hr>
{% endfor %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_msg = request.form["message"].lower()

        if "hello" in user_msg:
            bot_reply = "Hi ?? How are you?"
        elif "how are you" in user_msg:
            bot_reply = "I'm good ?? What about you?"
        elif "name" in user_msg:
            bot_reply = "I am your AI chatbot ??"
        else:
            bot_reply = "I am still learning..."

        chat_history.append({"user": user_msg, "bot": bot_reply})

    return render_template_string(html, chat=chat_history)

if __name__ == "__main__":
    app.run(debug=True)