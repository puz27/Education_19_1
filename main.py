from http.server import BaseHTTPRequestHandler, HTTPServer


hostname = "localhost"
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    """ Light Web Server"""

    def get_content(self) -> str:
        """Return text information"""
        return """Hello, World wide web!"""

    def do_POST(self) -> None:
        """Execute POST request"""
        content_len = int(self.headers.get("Content-Length"))
        client_data = self.rfile.read(content_len)
        print(client_data.decode())

    def do_GET(self) -> None:
        """Execute GET request"""
        page_content = self.get_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostname, server_port), MyServer)
    print("Server started http://%s:%s" % (hostname, server_port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Stop Server")
