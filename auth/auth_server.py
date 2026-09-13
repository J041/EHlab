from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

VALID_USERNAME = "Admin"
VALID_PASSWORD = "harrypotter123"

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/login":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8", errors="ignore")
        data = parse_qs(body)

        username = data.get("username", [""])[0]
        password = data.get("password", [""])[0]

        if username != VALID_USERNAME:
            status = 404
            message = "Invalid credentials\n"
        elif password != VALID_PASSWORD:
            status = 401
            message = "Invalid password\n"
        else:
            status = 200
            message = "Login successful\nepITL6KxA2JrCFPUdabmIxQI0AQXTKUa\n"

        encoded = message.encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, fmt, *args):
        pass

HTTPServer(("0.0.0.0", 9000), Handler).serve_forever()
