import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('93.125.15.6', 9090))
run = True


while run:
    data = input('Enter the action: ')
    sock.send(data.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    a = data.decode('utf-8')
    if a[5] == '4':
        run = False

data = sock.recv(1024)
print(data.decode('utf-8'))
sock.close()


