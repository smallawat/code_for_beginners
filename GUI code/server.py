import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(5)
c,addr=s.accept()
print('Got connection from',addr)
while True:
    messg=bytes("sanketm=>"+input(r""),encoding='utf-8')
    c.send(messg)
    data=str(c.recv(1024)).strip('b').strip('\'')
    print(data)
  