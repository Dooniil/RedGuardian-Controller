from socketserver import StreamRequestHandler, TCPServer, ThreadingMixIn

from dotenv import load_dotenv
import os

load_dotenv()

CONTROLLER_HOST = os.environ.get('CONTROLLER_HOST')
CONTROLLER_PORT = os.environ.get('CONTROLLER_PORT')


class ControllerTCPHandler(StreamRequestHandler):
    def handle(self):
        while True:
            chunk = self.rfile.readline()
            if not chunk:
                break

            self.wfile.write(chunk)


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass
