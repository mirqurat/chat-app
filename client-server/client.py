import socket
s = socket.socket()
host = 'localhost'
port = 1234
s.connect((host,port))
print("connected to server")
    #print("connection to server is failed")
# print(s.recv(1024).decode())
# m  = input("enter your message")
# m =m.encode()
# s.send(m)

un  = input("enter your username")
pwd  = input("enter your passkey")
s.sendall(un.encode())
s.send(pwd.encode())



    
while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("server >>",incoming_message)
    message = input(str("you >>"))
    message = message.encode()
    s.send(message)