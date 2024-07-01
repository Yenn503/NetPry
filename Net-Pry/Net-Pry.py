import colorama
import os
import subprocess
from colorama import Fore, Back, init
import argparse
from netcat import NetCat
from ssh_cmd import SSH_client
from ssh_server import start_server
from TCP_Client import run_TCP_Client # type: ignore
from TCP_server import run_TCP_server # type: ignore
from TCP_proxy import server_loop # type: ignore
from UDP_client import run_UDP_client # type: ignore



# Initialize colorama for colored output
init(autoreset=True)

logo = """
 ███▄    █ ▓█████▄▄▄█████▓ ██▓███   ██▀███ ▓██   ██▓
 ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▓██░  ██▒▓██ ▒ ██▒▒██  ██▒
▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▓██░ ██▓▒▓██ ░▄█ ▒ ▒██ ██░
▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ▒██▄█▓▒ ▒▒██▀▀█▄   ░ ▐██▓░
▒██░   ▓██░░▒████▒ ▒██▒ ░ ▒██▒ ░  ░░██▓ ▒██▒ ░ ██▒▓░
 ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ▒▓▒░ ░  ░░ ▒▓ ░▒▓░  ██▒▒▒ 
 ░░   ░ ▒░ ░ ░  ░   ░    ░▒ ░       ░▒ ░ ▒░▓██ ░▒░ 
   ░   ░ ░    ░    ░      ░░         ░░   ░ ▒ ▒ ░  
         ░    ░  ░                    ░     ░ ░     
                                                ░ ░     
                                            ░
"""



'''


  _____       _           _   _             
 |_   _|     (_)         | | (_)            
   | |  _ __  _  ___  ___| |_ _  ___  _ __  
   | | | '_ \| |/ _ \/ __| __| |/ _ \| '_ \ 
  _| |_| | | | |  __/ (__| |_| | (_) | | | |
 |_____|_| |_| |\___|\___|\__|_|\___/|_| |_|
            _/ |                            
           |__/                             


'''




def inject_text_file():
    print(f"{Fore.GREEN}Running Proccess injection...{Fore.RESET}\nThis is my Version of techniques put together from the {Fore.RED}MalDev{Fore.RESET}{Fore.BLACK}Academy{Fore.RESET} course. ")
    try:
        I_choice = input("Using process hacker 2 or tasklist | findstr notepad.exe. You can find the PID of a running process.\nDo you wish to proceed Y/n: ")
        if I_choice == "Y":
            pid = int(input("Enter the PID of the target process: "))
            file_path = input("Enter the path to the text file to inject: ").strip()
        if I_choice == "n":
            print("Returning..")
            selection()
        # Check if the text file exists
        if not os.path.exists(file_path):
            print(f"{Fore.RED}Error: Text file not found at {file_path}")
            return

        # Construct absolute path to Net-Injector.exe
        script_dir = os.path.dirname(os.path.abspath(__file__))
        net_injector_path = os.path.join(script_dir, 'Net-Injector.exe')

        # Check if Net-Injector.exe exists
        if not os.path.exists(net_injector_path):
            print(f"{Fore.RED}Error: Net-Injector.exe not found at {net_injector_path}")
            return

        # Execute Net-Injector.exe with PID and file path
        process = subprocess.Popen([net_injector_path, str(pid), file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Decode stdout and stderr from bytes to strings
        stdout_str = stdout.decode('utf-8').strip()
        stderr_str = stderr.decode('utf-8').strip()

        # Display output
        if stdout_str:
            print(f"{Fore.GREEN}Stdout:\n{stdout_str}")
        if stderr_str:
            print(f"{Fore.RED}Stderr:\n{stderr_str}")

        # Check for success or failure
        if process.returncode == 0:
            print(f"{Fore.GREEN}Injection successful")
        else:
            print(f"{Fore.RED}Injection failed: {stderr_str}")

    except ValueError:
        print(f"{Fore.RED}Invalid PID. Please enter a valid number.")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")


"""  
  _   _      _                      _      _______          _     
 | \ | |    | |                    | |    |__   __|        | |    
 |  \| | ___| |___      _____  _ __| | __    | | ___   ___ | |___ 
 | . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /    | |/ _ \ / _ \| / __|
 | |\  |  __/ |_ \ V  V / (_) | |  |   <     | | (_) | (_) | \__ \
 |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\    |_|\___/ \___/|_|___/
                                                                  
                                                                  
                                 

"""

def run_network_tools():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
        print(f"{Fore.LIGHTBLACK_EX}{Back.BLACK}" + logo)  # Print logo
        print("\nChoose a network tool: ")
        print("1. Netcat (Python version)")
        print("2. SSH client")
        print("3. SSH server")
        print("4. TCP client")
        print("5. TCP server")
        print("6. TCP proxy")
        print("7. UDP client")
        print("8. Back to main menu")

        net_choice = input("Enter an option: ")

        if net_choice == '1':
            print(f"Running Netcat ({Fore.GREEN}Python Version{Fore.RESET})")
            target = input("Enter target IP: ")
            port = int(input("Enter port: "))
            listen = input("Listen mode? (yes/no): ").lower() == 'yes'
            execute = input("Enter command to execute (leave blank if not used): ")
            command = input("Enter command shell? (yes/no): ").lower() == 'yes'
            upload = input("Enter file path to upload (leave blank if not used): ")
            buffer = input("Enter buffer (leave blank if not used): ")

            args = argparse.Namespace(
                target=target, port=port, listen=listen, execute=execute, 
                command=command, upload=upload
            )
            nc = NetCat(args, buffer.encode() if buffer else None)
            nc.run()

        elif net_choice == '2':
            print("Running SSH client...")
            import getpass
            user = input('Username: ')
            password = getpass.getpass()
            ip = input('Enter server IP: ')
            port = input('Enter port or <CR>: ')
            cmd = input('Enter command or <CR>: ')
            SSH_client.ssh_command(ip, port, user, password, cmd)
            
        elif net_choice == '3':
            print("Running SSH server...")
            server_ip = input("Enter the server IP: ")
            server_port = input("Enter the server port: ")
            start_server(server_ip, server_port)
            
            
        elif net_choice == '4':
            print(f"{Fore.GREEN}Running TCP client...{Fore.RESET}")
            TCP_IP = input("Enter the TCP IP: ")
            TCP_port = int(input("Enter the TCP port: "))
            run_TCP_Client(TCP_IP, TCP_port)


        elif net_choice == '5':
            print(f"{Fore.GREEN}Running TCP server...{Fore.RESET}")
            TCPS_IP =  input("Enter the server IP: ")
            TCPS_port = int(input("Enter the server port: "))
            run_TCP_server(TCPS_IP, TCPS_port)


        elif net_choice == '6':
            print("Running TCP proxy...")
            local_host = input("Enter local IP to bind (e.g., 127.0.0.1): ")
            local_port = int(input("Enter local port to bind: "))
            remote_host = input("Enter remote IP to forward to (e.g., 192.168.0.1): ")
            remote_port = int(input("Enter remote port to forward to: "))
            receive_first = input("Receive first packet from remote? (True/False): ").lower() == 'true'
    
            server_loop(local_host, local_port, remote_host, remote_port, receive_first)


        elif net_choice == '7':
            print("Running UDP client...")
            UDP_IP = input("Enter the UDP IP: ")
            UDP_port = int(input("Enter the UDP port: "))
            run_UDP_client(UDP_IP, UDP_port)

        elif net_choice == '8':
            print("Returning to main menu...")
            break
        else:
            print("Invalid option. Please choose again.")

        input("\nPress Enter to continue...")  # Wait for user to press Enter



"""   
   _____      _           _   _             
  / ____|    | |         | | (_)            
 | (___   ___| | ___  ___| |_ _  ___  _ __  
  \___ \ / _ \ |/ _ \/ __| __| |/ _ \| '_ \ 
  ____) |  __/ |  __/ (__| |_| | (_) | | | |
 |_____/ \___|_|\___|\___|\__|_|\___/|_| |_|
                                                                                   

"""


def selection():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
        print(f"{Fore.LIGHTBLACK_EX}{Back.BLACK}" + logo)  # Print logo
        print("\nPlease choose an option: ")
        print("1. Networking tools")
        print(f"2. Process Injection ({Fore.GREEN}RC4 encryption{Fore.RESET})")
        print("3. Option three")
        print("4. Option four")
        print("5. Exit")

        choice = input("Enter an Option: ")

        if choice == '1':
            run_network_tools()  # Call function to run networking tools
        elif choice == '2':
            inject_text_file()  # Call function to perform text file injection
        elif choice == '3':
            print("Option selected")
            # Implement option three functionality
        elif choice == '4':
            print("Option selected")
            # Implement option four functionality
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please choose again.")

        input("\nPress Enter to continue...")  # Wait for user to press Enter

if __name__ == '__main__':
    selection()  # Call main selection function

