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

fc = FritzConnection(address=environ["FritzBoxUri"],
                     user=environ["FritzBoxUser"], password=environ["FritzBoxPassword"])
fs = FritzStatus(fc)

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/ip":
            ip = fs.external_ip if fs.external_ip else fc.call_action("WANPPPConnection1", "GetInfo")["NewExternalIPAddress"]
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(ip.encode())


httpd = HTTPServer(("0.0.0.0", 8080), Server)
httpd.serve_forever()
