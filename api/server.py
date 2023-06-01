from http.server import HTTPServer, BaseHTTPRequestHandler
port = 8000

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.send_header('Teste','abc')
        self.end_headers()
        self.wfile.write('Olá, mundo!'.encode())

server = HTTPServer(('localhost', port), SimpleHandler)
server.serve_forever()