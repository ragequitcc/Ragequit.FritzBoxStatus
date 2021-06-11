from os import environ
from http.server import BaseHTTPRequestHandler, HTTPServer
from fritzconnection.lib.fritzstatus import FritzStatus

print(environ)

if "FritzBoxUri" not in environ:
    print("FritzBoxUri Missing")
    quit()

if "FritzBoxUser" not in environ:
    print("FritzBoxUser Missing")
    quit()

if "FritzBoxPassword" not in environ:
    print("FritzBoxPassword Missing")
    quit()

fc = FritzStatus(address=environ["FritzBoxUri"],
                 user=environ["FritzBoxUser"], password=environ["FritzBoxPassword"])


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(fc.external_ip.encode())


httpd = HTTPServer(("0.0.0.0", 8080), Server)
httpd.serve_forever()
