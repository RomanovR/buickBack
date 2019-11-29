# python3
# Набросок для однопоточного сервера.
import sys
from socketserver import BaseRequestHandler, TCPServer


class MyTCPHandler(BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        self.request.sendall(data[::-1])


if __name__ == '__main__':
    host = 'localhost'
    port = int(sys.argv[1])

    with TCPServer((host, port), MyTCPHandler) as srv:
        srv.serve_forever()
