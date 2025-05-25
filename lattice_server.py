from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
MESSAGE_FILE = "message.txt"

@app.route("/", methods=["GET", "POST"])
def lattice():
    if request.method == "POST":
        message = request.form.get("message", "")
        with open(MESSAGE_FILE, "w") as f:
            f.write(message)

    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r") as f:
            message = f.read()
    else:
        message = "⚠️ No message has been written to the lattice yet."

    html = f"""
    <html>
        <head><title>CHAD LATTICE THREAD</title></head>
        <body>
            <h1>🧠 CHAD LATTICE THREAD</h1>
            <form method="POST">
                <textarea name="message" rows="10" cols="60">{message}</textarea><br>
                <input type="submit" value="Send to Lattice">
            </form>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)


