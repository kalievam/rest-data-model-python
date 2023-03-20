import os
import http.server
import socketserver

HOST = "0.0.0.0"
PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path[1:]        # path from the request URL
        # List directory content:
        if os.path.isdir(path):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("\n".join(os.listdir(path)).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        path = self.path[1:]
        content_length = int(self.headers.get("Content-Length"))    # request headers content length
        # read request body, if too large transfer in chunks of max 512MB
        chunk_size = 512 * 1024 * 1024
        bytes_read = 0
        with open(path, "wb") as f:
            while bytes_read < content_length:
                left_bytes = content_length - bytes_read
                chunk = self.rfile.read(min(chunk_size, left_bytes))
                if not chunk:   break
                f.write(chunk)
                bytes_read += len(chunk)
        self.send_response(200)
        self.end_headers()

# Start listening for incoming requests
with socketserver.TCPServer((HOST, PORT), MyHandler) as httpd:
    print(f"Serving on {HOST}:{PORT}")
    httpd.serve_forever()
