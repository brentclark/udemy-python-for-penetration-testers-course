import socket

host = socket.gethostname()
port = 9338

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)

print("Server started:")
conn,addr = sock.accept()

print("Connection established with:",addr)
message = "Thank you for connecting." + str(addr)

conn.send(message.encode('ascii'))
conn.close()