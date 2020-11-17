import rpyc
import socket
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value = self.value + [data]
        print ("Appended value = ", data)
        return self.value

    def exposed_value(self):
        return self.value
    
    def exposed_delete(self, data):
        if data in self.value:
            print ("Deleted value = " + data)
            self.value.remove(data)
            return self.value

if __name__ == "__main__":
    server = ThreadedServer(DBList, port = 20202)
    conn_dir = rpyc.connect(DIR_SERVER, DIR_PORT)
    my_address = socket.gethostbyname(socket.gethostname())
    print (conn_dir.root.exposed_unregister("DBList"))
    print (conn_dir.root.exposed_register("DBList", my_address, 20202))
    server.start()