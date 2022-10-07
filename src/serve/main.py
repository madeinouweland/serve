from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import os
import subprocess

port = 8008
address = "localhost"
website_directory = os.path.abspath(os.getcwd())

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        path = website_directory + self.path
        if path.endswith("/"):
            path += "index.html"

        try:
            with open(path, "r", encoding="utf-8") as file:
                text = file.read()
                self.end_headers()
                self.wfile.write(bytes(text, "utf-8"))

        except UnicodeDecodeError:
            self.end_headers()
            with open(path, "rb") as file:
                self.wfile.write(file.read())
        except FileNotFoundError:
            if path.endswith("index.html"):
                print("Cannot serve this folder because it does not contain index.html!")
                exit()
            print(f"{path} not found")

def main():
    httpd = HTTPServer((address, port), Handler)
    print(f"--=*> Starting server at {address}:{port} <*=--")
    print(f"Opening index.html from local directory: {website_directory}.")
    subprocess.Popen(["open", "-a", "Brave Browser", f"http://127.0.0.1:{port}"])
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")

if __name__ == '__main__':
    main()
