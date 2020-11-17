import rpyc
from constRPYC import *

class Client:
    conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)
    (address, port) = conn_directory.root.exposed_lookup("DBList")
    print (address, port)

    conn_server = rpyc.connect(address, port)
    conn_server.root.exposed_append(2)
    conn_server.root.exposed_append(10)
    conn_server.root.exposed_append(5)
    conn_server.root.exposed_append(4)
    print (conn_server.root.exposed_value())
    conn_server.root.exposed_delete(4)
    print (conn_server.root.exposed_value())
    conn_server.root.exposed_delete(10)
    print (conn_server.root.exposed_value())