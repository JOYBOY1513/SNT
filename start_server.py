"""
Quantum Mastery Lab - Local Launcher
Starts a local web server and automatically opens the platform in your browser.
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import os

PORT = 8080

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Clean logging
        pass

def open_browser():
    time.sleep(1.2)
    url = f"http://localhost:{PORT}/index.html"
    print(f"[*] Opening Quantum Mastery Lab in browser: {url}")
    webbrowser.open(url)

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    handler = QuietHandler

    print("=" * 65)
    print("🚀 QUANTUM MASTERY LAB - LOCAL SERVER")
    print("=" * 65)
    print(f"[*] Serving at: http://localhost:{PORT}")
    print("[*] Press Ctrl+C to stop the server at any time.")
    print("=" * 65)

    threading.Thread(target=open_browser, daemon=True).start()

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] Server stopped.")

if __name__ == "__main__":
    main()
