from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
MESSAGE_FILE = "message.txt"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_message = request.form.get("message")
        with open(MESSAGE_FILE, "w") as f:
            f.write(new_message)

    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r") as f:
            message = f.read()
    else:
        message = "⚠️ No message has been written to the lattice yet."

    return render_template_string("""
        <html>
            <head><title>CHAD LATTICE THREAD</title></head>
            <body style="background-color: black; color: #00ffcc; font-family: monospace;">
                <h1>CHAD LATTICE THREAD</h1>
                <pre>{{ message }}</pre>
                <hr>
                <form method="POST">
                    <textarea name="message" rows="10" cols="60">{{ message }}</textarea><br>
                    <button type="submit">Update Lattice</button>
                </form>
            </body>
        </html>
    """, message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


