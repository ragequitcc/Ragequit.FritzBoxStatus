from os import environ
from http.server import BaseHTTPRequestHandler, HTTPServer
from fritzconnection.lib.fritzstatus import FritzStatus
from fritzconnection import FritzConnection

fc = FritzConnection(address="192.168.178.1",
                     user="dyndns", password="admin123")
fs = FritzStatus(fc)

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = fs.external_ip if fs.external_ip else fc.call_action("WANPPPConnection1", "GetInfo")["NewExternalIPAddress"]
        if self.path == "/ip/v4":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(ip.encode())

        elif self.path == "/ip/v6":
            ip = fs.external_ipv6 if fs.external_ipv6 else "Not Available"

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(ip.encode())

httpd = HTTPServer(("0.0.0.0", 8080), Server)
httpd.serve_forever()
