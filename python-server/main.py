from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8000


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Sharath Madarchod!",  "utf-8"))


if __name__ == "__main__":
    webserver = HTTPServer((hostName, serverPort), Server)

    try:
        webserver.serve_forever()
    except KeyboardInterrupt as e:
        print(e)
    
    webserver.server_close()