from flask import Flask, render_template_string
import os

app = Flask(__name__)

MESSAGE_FILE = "message.txt"

@app.route("/")
def display_message():
    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r") as f:
            message = f.read()
    else:
        message = "⚠️ No message written yet."

    return render_template_string(f"""
        <html>
        <head>
            <title>CHAD LATTICE THREAD</title>
            <meta http-equiv="refresh" content="3">
            <style>
                body {{
                    background-color: black;
                    color: #00FF99;
                    font-family: monospace;
                    padding: 40px;
                }}
                h1 {{
                    font-size: 2em;
                    color: #FF00FF;
                }}
                pre {{
                    font-size: 1.2em;
                    white-space: pre-wrap;
                }}
            </style>
        </head>
        <body>
            <h1>CHAD LATTICE THREAD</h1>
            <pre>{{{{ message }}}}</pre>
        </body>
        </html>
    """, message=message)

if __name__ == "__main__":
    app.run(port=8000)

