import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Enter the ip: ")
port = 53

def portscanner(port):
    if sock.connect_ex((host,port)):
        print("Port "+ str(port) +" is closed")
    else:
        print("Port "+ str(port) +" is open")
portscanner(port)