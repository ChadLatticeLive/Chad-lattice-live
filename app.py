from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
MESSAGE_FILE = "message.txt"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CHAD LATTICE THREAD</title>
    <style>
        body { font-family: monospace; background: #0d0d0d; color: #00ffcc; padding: 20px; }
        h1 { color: #ff4081; }
        form { margin-top: 20px; }
        textarea { width: 100%; height: 100px; background: #1e1e1e; color: #00ffcc; border: 1px solid #ff4081; padding: 10px; }
        input[type="submit"] { background: #ff4081; color: white; border: none; padding: 10px 20px; cursor: pointer; margin-top: 10px; }
        .message { background: #1e1e1e; padding: 20px; border: 1px solid #00ffcc; margin-top: 20px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>CHAD LATTICE THREAD</h1>
    <form method="POST">
        <textarea name="message" placeholder="Enter your message to the lattice..."></textarea><br>
        <input type="submit" value="Update Lattice">
    </form>
    <div class="message">
        <strong>Latest Broadcast:</strong><br>{{ message }}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        new_message = request.form.get("message", "")
        with open(MESSAGE_FILE, "w") as f:
            f.write(new_message)

    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r") as f:
            message = f.read()
    else:
        message = "⚠️ No message has been written to the lattice yet."

    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
