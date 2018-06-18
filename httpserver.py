from socket import *
from magicallygivingoutvalues import *
import os.path

servername="0.0.0.0"
serverport=80
serverSocket=socket(AF_INET,SOCK_STREAM)

serverSocket.bind((servername,serverport))
serverSocket.listen(2)

print("Server up and running")
while 1:
    conn,address=serverSocket.accept()
    message=conn.recv(1024)
    attrib=parseme(message)
    reqd_file=attrib["GET"]
    if reqd_file=="":
        file=open('./templates/index.html')
        stuff=file.read()
        length=len(stuff)
        postmessage="HTTP/1.1 200 OK\r\nContent-Length: {}\r\nContent-Type: text/html\r\n\n{}".format(length,stuff)
        conn.send(postmessage)
    if os.path.exists('./templates/{}'.format(reqd_file)) and reqd_file!="":
        file=open('./templates/{}'.format(reqd_file))
        stuff=file.read()
        length=len(stuff)
        postmessage="HTTP/1.1 200 OK\r\nContent-Length: {}\r\nContent-Type: text/html\r\n\n{}".format(length,stuff)
        conn.send(postmessage)
    else:
        print("404 running")
        postmessage="HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\n<html><head><title>404</title></head><body>404 Page Not Found :(</body></html>"
        conn.send(postmessage)
    conn.close()
