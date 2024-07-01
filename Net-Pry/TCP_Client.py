import socket

def run_TCP_Client(TCP_IP, TCP_port):
    try:
        # create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect the client
        client.connect((TCP_IP, TCP_port))

        # send some data
        client.send(b"GET / HTTP/1.1\r\nHost: Google.com\r\n\r\n")

        # receive some data
        response = client.recv(4096)

        print(response.decode())
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    TCP_IP = input("Enter the TCP IP: ")
    TCP_port = int(input("Enter the TCP port: "))
    run_TCP_Client(TCP_IP, TCP_port)
