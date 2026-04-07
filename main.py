import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 3000))

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
print(f"Serving on http://0.0.0.0:{PORT}")
httpd.serve_forever()
