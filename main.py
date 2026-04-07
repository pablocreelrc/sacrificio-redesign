import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 5000))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.path = '/direction-b.html'
        return super().do_GET()

    def log_message(self, format, *args):
        pass

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}", flush=True)
    httpd.serve_forever()
