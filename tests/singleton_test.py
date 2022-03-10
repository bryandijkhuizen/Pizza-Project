from UDPSocketServer import UDPSocketServer
from UDPSocketClient import UDPSocketClient



def udp_server_test(passed_tests):
    server1 = UDPSocketServer('127.0.0.1', 5001)
    server2 = UDPSocketServer('127.0.0.1' , 5002)
    
    if server1 == server2 and server1.PORT == server2.PORT:
        print("Test 1 Passed")
        
        
    else:
        print("Test 1 Failed")
        
def udp_client_test(passed_tests):
    client1 = UDPSocketClient('127.0.0.1', 5001)
    client2 = UDPSocketClient('127.0.0.1', 5002)
    
    if client1 == client2 and client1.PORT == client2.PORT:
        print("Test 2 Passed")
     
        
    else:
        print("Test 2 Failed")
        
if __name__ == "__main__":
    udp_server_test()
    udp_client_test()

    
    
        



    