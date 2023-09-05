import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  #IP address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'END'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET --> IPV4   SOCK_STREAM--> TCP
server.bind(ADDR)


server.listen()
print('Server Listening. ')
conn, addr = server.accept()


connection = True
while connection:
    message_length = conn.recv(HEADER)
    if message_length:
        message_length = int(message_length)
        message = conn.recv(message_length).decode(FORMAT)
        if message == DISCONNECT_MESSAGE:
            connection = False
            conn.send('Disconnecting.' .encode(FORMAT))
        else:
            print(message)
           
            conn.send('Message Received.' .encode(FORMAT))

conn.close()

