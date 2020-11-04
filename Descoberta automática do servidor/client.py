import rpyc
from constRPYC import *

class Client:
    conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)
    (address, port) = conn_directory.root.public_lookup("DBList")
    print (adress, port)

    conn_server = rpyc.connect(adress, port)
    conn_server.root.public_append(2)
    conn_server.root.public_append(4)
    print (conn_server.root.exposed_value())