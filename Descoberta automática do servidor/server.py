import rpyc
import socket
from constRPYC import *
from rpyc.utils.server import ForkingServer

class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value = self.value + [data]
        print ("Appended value = ", data)
        return self.value

    def exposed_value(self):
        return self.value

if __name__ == "__main__":
    server = ForkingServer(DBList, port = 20202)
    conn_dir = rpyc.connect(DIR_SERVER, DIR_PORT)
    my_address = socket.gethostbyname(socket.gethostname())
    print (conn_dir.root.exposed_register("DBList", my_address, 20202))
    server.start()