import paramiko

class SSH_client:
    def ssh_command(ip, port, user, passwd, cmd):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=port, username=user, password=passwd)
        
        _, stdout, stderr, = client.exec_command(cmd)
        output = stdout.readlines() + stderr.readlines()
        if output:
            print('---Output---')
            for line in output:
                print(line.strip())
                
    
        import getpass
        # user = getpass.getuser()
        user = input('Username: ')
        password = getpass.getpass()
        print(password)
        
        ip = input('Enter server IP: ')
        port = input('Enter port or <CR>: ')
        cmd = input('Enter command or <CR>: ')
        ssh_command(ip, port, user, password, cmd) # type: ignore

if __name__ == "__main__":
    SSH_client()