# lattice_server.py
import http.server
import socketserver
import os
from urllib.parse import parse_qs

PORT = 8000
MESSAGE_FILE = "message.txt"

class LatticeHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = ""
        if os.path.exists(MESSAGE_FILE):
            with open(MESSAGE_FILE, "r") as f:
                message = f.read()

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

        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        parsed = parse_qs(post_data)
        message = parsed.get("message", [""])[0]

        with open(MESSAGE_FILE, "w") as f:
            f.write(message)

        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), LatticeHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()


