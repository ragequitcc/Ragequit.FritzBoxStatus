from http.server import BaseHTTPRequestHandler, HTTPServer
from fritzconnection.lib.fritzstatus import FritzStatus

# u should probably change this
fc = FritzStatus(address='192.168.178.1',
                 user="dyndns", password="admin123")


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(fc.external_ip.encode())


httpd = HTTPServer(('0.0.0.0', 8080), Server)
httpd.serve_forever()
