import socket 
import threading



def run_TCP_server(TCPS_IP, TCPS_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TCPS_IP, TCPS_port))
    server.listen(5)
    
    print(f'[*] Listening on {TCPS_IP}:{TCPS_port}')
    
    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
        
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recieved: {request.decode("utf-8")}')
        sock.send(b'ACK')
        
if __name__ == '__main__':
    TCPS_IP =  input("Enter the server IP: ")
    TCPS_port = int(input("Enter the server port: "))
    run_TCP_server()
