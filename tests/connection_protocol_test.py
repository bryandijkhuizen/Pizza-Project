from config.ConnectionManager import ConnectionManager, ConnectionProtocol

connection_manager = ConnectionManager("Pizza Server")

tcp = ConnectionProtocol("TCP")
udp = ConnectionProtocol("UDP")

connection_manager.add_connection(tcp)
connection_manager.add_connection(udp)

connection_manager.set_default_connection(tcp)

print(connection_manager.default.get_protocol())


if connection_manager.default.get_protocol() == "TCP":
    print(1)