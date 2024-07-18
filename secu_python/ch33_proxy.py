import http.server
import socketserver
import logging
import requests

PORT = 8080

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]  # Remove leading slash
        logging.info(f"GET request for {url} from {self.client_address}")

        # Filtering rules
        if "blocked.com" in url:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Blocked by proxy")
            logging.warning(f"Blocked request to {url}")
            self.send_alert(f"Blocked request to {url} from {self.client_address}")
            return

        # Forward the request
        try:
            response = requests.get(url)
            self.send_response(response.status_code)
            self.send_headers(response.headers)
            self.wfile.write(response.content)
        except requests.RequestException as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Error forwarding request")
            logging.error(f"Error forwarding request: {e}")

    def send_headers(self, headers):
        for key, value in headers.items():
            self.send_header(key, value)
        self.end_headers()

    def send_alert(self, message):
        # Print alert message to console
        print(f"ALERT: {message}")
        logging.warning(f"ALERT: {message}")

    def log_message(self, format, *args):
        # Override to prevent default logging
        return

def run_server():
    logging.basicConfig(filename='proxy.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    with socketserver.TCPServer(("", PORT), Proxy) as httpd:
        logging.info(f"Starting proxy on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
