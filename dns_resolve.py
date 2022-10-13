import socket

hostname = input("Please enter website address:\n")
print(f'The {hostname} IP Address is {socket.gethostbyname(hostname)}')