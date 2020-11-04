import rpyc
from constRPYC import * 
from rpyc.utils.server import ThreadedServer

class Directory(rpyc.Service):
    registry = {}

    def public_register(self, server_name, ip_adress, port_number):
        self.registry[server_name] = {ip_adress, port_number}
        print (self.registry)
        return "Registered Successfully"

    def public_lookup(self, server_name):
        print (self.registry)
        return self.registry[server_name]

if __name__ == "__main__":
    server_dir = ThreadedServer(Directory, port = DIR_PORT )
    server_dir.start()