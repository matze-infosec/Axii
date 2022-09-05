import pyfiglet
import sys
import socket
from datetime import datetime
import threading

ascii_banner = pyfiglet.figlet_format("Axii")
print(ascii_banner)

target = input(str("IP: "))

#banner
print("-"*50)
print("Scanning Target: " + target)
print(str(datetime.now()))
print("-"*50)

def scanner():
    try:
        #Scan ports in the range of 1 to 65535.
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

        #return open ports
            result = s.connect_ex((target,port))
            if result == 0:
                print("[*] Port {} is open".format(port))
            s.close()
    except KeyboardInterrupt:
        print("\n Exiting ")
    sys.exit()

#scanner()
thread = threading.Thread(target=scanner)
thread.start()


