from http.server import HTTPServer, BaseHTTPRequestHandler
port = 8000

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type','text/html; charset=utf-8')
            self.end_headers()
            data = f''' 
            <html>
                <head>
                    <title>Olá mundo !</title>
                </head>
                <body>
                    <p>Server testing!</p>
                    <p>Directory: {self.path} </p>
                </body>
            </html>
            '''
            self.wfile.write(data.encode())
        elif self.path == '/events':
            self.send_response(200)
            self.send_header('Content-Type','text/html;charset=utf-8')
            self.end_headers() 
            data = f'''
            <html>
                <p>Oi</p>
            </html>
            '''
            self.wfile.write(data.encode())

server = HTTPServer(('localhost', port), SimpleHandler)
server.serve_forever()