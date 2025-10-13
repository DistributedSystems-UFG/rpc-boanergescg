import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.values = self.values + [data]
    return self.values

  def exposed_values(self):
    return self.values

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

