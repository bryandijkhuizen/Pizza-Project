# create a Connection class
    # implementing the connection interface/composite pattern
class ConnectionManager:
    # constructor
    def __init__(self, *args):
        # positional arguments
        self.position = args[0]
        
        # list of children
        self.children = []
        
        # default child (connection)
        self.default = None
        
    def add_connection(self, child):
        self.children.append(child)
        
    def remove_connection(self, child):
        self.children.remove(child)
        
    def set_default_connection(self, child):
        self.default = child
        
# create a Connection Element class
class ConnectionElement:
    # constructor
    def __init__(self, *args):
        # get the position of the connection element
        self.position = args[0]
        
    # method to get the position of the connection element
    def get_protocol(self):
        return self.position
    
# create a Connection Manager class
connection_manager = ConnectionManager("Pizza Server")

# create connection protocols
tcp = ConnectionElement("TCP")
udp = ConnectionElement("UDP")
tcp_tls = ConnectionElement("TCP/TLS")

# add the connection protocols to the connection manager
connection_manager.add_connection(tcp)
connection_manager.add_connection(udp)
connection_manager.add_connection(tcp_tls)

# set the default connection
connection_manager.set_default_connection(tcp_tls)
        
    
    
