from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)
MESSAGE_FILE = "message.txt"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        with open(MESSAGE_FILE, "w") as f:
            f.write(request.form.get("message", ""))

    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r") as f:
            message = f.read()
    else:
        message = "⚠️ No message found."

    return render_template_string('''
        <html><body>
            <h2>CHAD LATTICE THREAD</h2>
            <form method="POST">
                <textarea name="message" rows="10" cols="50">{{ message }}</textarea><br>
                <input type="submit" value="Broadcast">
            </form>
        </body></html>
    ''', message=message)

@app.route("/api/message", methods=["GET"])
def api_message():
    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r") as f:
            return jsonify({"message": f.read()})
    else:
        return jsonify({"message": "No message found."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)