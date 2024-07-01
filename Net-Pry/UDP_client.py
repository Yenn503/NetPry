import socket



def run_UDP_client(UDP_IP, UDP_port):
    # create a socket object

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # send some data

    client.sendto(b"AAABBBCCC", (UDP_IP, UDP_port))

    # recieve some data

    data, addr = client.recvfrom(4096)

    print(data.decode())
    client.close()

if __name__ == "__main__":
    UDP_IP = input("Enter the UDP IP: ")
    UDP_port = int(input("Enter the UDP port: "))
    run_UDP_client()