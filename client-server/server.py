import socket
import sys

import connect
s = socket.socket()
host = 'localhost'
port = 1234
s.bind((host,port))
print("server is bound successfully")
s.listen(1)
conn,addr = s.accept()
print(addr,"has connected")
username =conn.recv(1024).decode()
password =conn.recv(1024).decode()


print(f"{username} {password}")

result=connect.varify(username,password)
if result is True:
    print("valid user")
else:
    print("invalid user ")
    


# m  = input("enter your message")
# m =m.encode()
# conn.send(m)
# print(conn.recv(1024).decode())

while 1:
    message = input(str("you>>"))
    message = message.encode()
    conn.send(message)
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("client >>",incoming_message)