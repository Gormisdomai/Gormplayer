from SimpleWebSocketServer import *

clients = []
class Serve(WebSocket):

    def handleMessage(self):
       for client in clients:
          if client != self:
             client.sendMessage(self.data)
       return

    def handleConnected(self):
       clients.append(self)

    def handleClose(self):
       clients.remove(self)

server = SimpleWebSocketServer('', 9999, Serve)
server.serveforever()
