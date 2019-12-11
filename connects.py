# python3

from socketserver import BaseRequestHandler, ThreadingMixIn, TCPServer

class MyTCPHandler(BaseRequestHandler):
  def handle(self):
    data = self.request.recv(1024)
    self.request.sendall(data[::-1])


# Важная строчка! Эквивалент socketserver.ThreadingTCPServer
# https://github.com/python/cpython/blob/43fc3bb7cf0278735eb0010d7b3043775a120cb5/Lib/socketserver.py#L682
class ThreadedTCPServer(ThreadingMixIn, TCPServer): pass


if __name__ == '__main__':
  host = 'localhost'
  port = int(sys.argv[1])

  with ThreadedTCPServer((host, port), MyTCPHandler) as srv:
    srv.serve_forever()
