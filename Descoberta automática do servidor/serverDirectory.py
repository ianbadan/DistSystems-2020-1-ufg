import rpyc
from constRPYC import * 
from rpyc.utils.server import ThreadedServer

class Directory(rpyc.Service):
    registry = {}

    def exposed_register(self, server_name, ip_adress, port_number):
        if server_name in self.registry:
            return "Register Error: server name already exists" 
        else:   
            self.registry[server_name] = (ip_adress, port_number)
            print (self.registry)
            return "Registered Successfully"

    def exposed_unregister(self, server_name):
        if server_name in self.registry:
            self.registry.pop(server_name)
            return "Server Unregistered"
        else:
            return "Server does not exist"
    
    def exposed_lookup(self, server_name):
        print ("Client looking for server " + server_name)
        if server_name in self.registry:
            return self.registry[server_name]
        else:
            return None

if __name__ == "__main__":
    server_dir = ThreadedServer(Directory, port = DIR_PORT )
    print ("Server Started. Waiting Requests")
    server_dir.start()