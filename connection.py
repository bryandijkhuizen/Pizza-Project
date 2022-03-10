

# create a Connection class
    # implementing the connection interface/composite pattern
class ConnectionManager:
    
    def __init__(self, *args):
        
        self.position = args[0]
        self.children = []
        self.default = None
        
    def add_connection(self, child):
        self.children.append(child)
        
    def remove_connection(self, child):
        self.children.remove(child)
        
    def set_default_connection(self, child):
        self.default = child
        
        
class ConnectionElement:
    
    def __init__(self, *args):
        self.position = args[0]
        
    def get_protocol(self):
        return self.position
    
connection_manager = ConnectionManager("Pizza Server")

tcp = ConnectionElement("TCP")
udp = ConnectionElement("UDP")

connection_manager.add_connection(tcp)
connection_manager.add_connection(udp)

connection_manager.set_default_connection(udp)
        
    
    
