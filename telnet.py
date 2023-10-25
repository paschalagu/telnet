import paramiko
import telnetlib

# Router information
router_ip = "192.168.56.101"
router_ssh_port = 22
router_telnet_port = 23
username = 'AguPaschal'
password = 'cisco123!'
password_enable = 'class123!'

def ssh_to_router():
    try:
        print("Connecting via SSH...")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(router_ip, port=router_ssh_port, username=username, password=password)

        # Execute a command on the router
        stdin, stdout, stderr = ssh_client.exec_command("show version")
        print("SSH Command Output:")
        print(stdout.read().decode())

        # Close the SSH connection
        ssh_client.close()
        print("SSH Connection Closed.")
    except Exception as e:
        print(f"SSH connection failed: {e}")

def telnet_to_router():
    try:
        print("Connecting via Telnet...")
        # Connect to the router via telnet
        tn = telnetlib.Telnet(router_ip, router_telnet_port)

        tn.write(b"show version\n")
        output = tn.read_until(b"#", timeout=5).decode()
        print("Telnet Command Output:")
        print(output)

        # Close the telnet connection
        tn.close()
        print("Telnet Connection Closed.")
    except Exception as e:
        print(f"Failed connection for Telnet: {e}")

if __name__ == "__main__":
    ssh_to_router()
    telnet_to_router()
