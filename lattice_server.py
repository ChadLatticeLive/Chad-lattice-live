from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
MESSAGE_FILE = "message.txt"

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
  <title>CHAD LATTICE THREAD</title>
  <meta http-equiv="refresh" content="2">
  <style>
    body { font-family: monospace; background-color: black; color: #39ff14; padding: 20px; }
    pre { white-space: pre-wrap; word-wrap: break-word; }
  </style>
</head>
<body>
  <h1>CHAD LATTICE THREAD</h1>
  <pre>{{ message }}</pre>
</body>
</html>
"""

@app.route("/")
def home():
    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r") as f:
            message = f.read()
    else:
        message = "⚠️ No message has been written to the lattice yet."
    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == "__main__":
    app.run(port=8000)

