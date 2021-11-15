import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))
sock.listen(10)
conn, addr = sock.accept()

print('connected:', addr)

while b5.bucket != 4:

    data = conn.recv(1024)
    if not data:
        break
    buck, act = data.decode('utf-8').split()
    action(buck, act)
    n += 1
    ans = (f'b5 = {b5.bucket}, b3 = {b3.bucket}, ходы = {n}').encode('utf-8')
    conn.send(ans)

ans = (f'\nВы справились за {n} ходов').encode('utf-8')
conn.send(ans)
conn.close()
