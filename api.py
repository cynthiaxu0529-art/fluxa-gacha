#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class APIHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": True,
                "data": {
                    "status": "ready",
                    "agent_id": "7a123ed9-1517-4405-bafb-708b9aeb0577"
                }
            }).encode())
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path == '/api/create_payment':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            import time
            self.wfile.write(json.dumps({
                "success": True,
                "data": {
                    "payment_id": f"gacha_{int(time.time())}",
                    "amount": "10000",
                    "currency": "USDC"
                }
            }).encode())
        else:
            super().do_POST()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), APIHandler)
    print('🚀 Server running on http://localhost:8080')
    server.serve_forever()
