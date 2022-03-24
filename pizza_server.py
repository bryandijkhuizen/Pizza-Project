# import the socket server classes
from sockets.UDPSocketServer import UDPSocketServer
from sockets.TCPSocketServer import TCPSocketServer
from sockets.TCPTLSSocketServer import TCPSSLSocketServer

# from sockets.UDPSocketServer_fake import UDPSocketServer_fake

# import the connection manager class
from config.ConnectionManager import connection_manager

# check for the default protocol 
if connection_manager.default.get_protocol() == "TCP":
    # create an instance of the tcp server class and bind it to an ip and port
    # it will be listening for incoming connections automatically
    tcp_socket_server = TCPSocketServer('127.0.0.1', 5001)
    
    # listen for orders
    tcp_socket_server.listen_for_orders()
    
elif connection_manager.default.get_protocol() == "UDP":
    # create an instance of the udp server class and bind it to an ip and port
    udp_socket_server = UDPSocketServer('127.0.0.1', 5001)

    # listen for orders
    udp_socket_server.listen_for_orders()
    
elif connection_manager.default.get_protocol() == "TCP/TLS":

    tcp_tls_socket_server = TCPSSLSocketServer('127.0.0.1', 5001)
    tcp_tls_socket_server.listen_for_orders()
    
    






