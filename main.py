from os import environ
from http.server import BaseHTTPRequestHandler, HTTPServer
from fritzconnection.lib.fritzstatus import FritzStatus
from fritzconnection import FritzConnection

if "FritzBoxUri" not in environ:
    print("FritzBoxUri Missing")
    quit()

if "FritzBoxUser" not in environ:
    print("FritzBoxUser Missing")
    quit()

if "FritzBoxPassword" not in environ:
    print("FritzBoxPassword Missing")
    quit()

fc = FritzConnection(address="192.168.178.1",
                     user="dyndns", password="admin123")
fs = FritzStatus(fc)


ip = fs.external_ip if fs.external_ip else fc.call_action(
    "WANPPPConnection1", "GetInfo")["NewExternalIPAddress"]


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(ip.encode())


httpd = HTTPServer(("0.0.0.0", 8080), Server)
httpd.serve_forever()
