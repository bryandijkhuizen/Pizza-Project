from UDPSocketServer import UDPSocketServer

udp_socket_server = UDPSocketServer('127.0.0.1', 5001)
udp_socket_server.listen_for_orders() 
