from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import os
import subprocess

port = 8008
address = "localhost"
website_directory = os.path.abspath(os.getcwd())

class Handler(BaseHTTPRequestHandler):
    def write_response(self, response, extension=None):
        self.send_response(200)
        if extension == "jpg":
            self.send_header("Content-type", "image/jpeg")
        if extension == "png":
            self.send_header("Content-type", "image/png")
        if extension == "svg":
            self.send_header("Content-type", "image/svg+xml")
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        if self.path.endswith("/favicon.ico"):
            self.send_response(200)
            self.send_header("Content-Type", "image/x-icon")
            self.send_header("Content-Length", 0)
            self.end_headers()
            return

        path = website_directory + self.path
        if path.endswith("/"):
            path += "index.html"

        try:
            with open(path, "r", encoding="utf-8") as file:
                text = file.read()
                self.write_response(bytes(text, "utf-8"))

        except UnicodeDecodeError:
            with open(path, "rb") as file2:
                self.write_response(file2.read(), path.split(".")[-1])
        except FileNotFoundError:
            if path.endswith("index.html"):
                text = "Cannot serve this folder because it does not contain index.html."
                self.write_response(bytes(text, "utf-8"))
                print(text)
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
