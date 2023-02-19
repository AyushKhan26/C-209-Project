import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 5500
SERVER= None
clients= {}

def handleClient():
  pass

def acceptConnections():
    global SERVER
    global clients

    while True:
        client,addr = SERVER.accept()
        client_name = client.recv(2048).decode().lower()
        clients[client_name]= {
             "client": client,
             "address": addr,
             "connected_with": "",
             "file_name": " ",
             "file_size": 4096
        }
        print(f"Connection established with {client_name}: {addr}" )

     
        thread = Thread(target= handleClient,args={client,client_name})
        thread.start()

def setup():
  global SERVER
  global IP_ADDRESS
  global PORT

  SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  SERVER.bind((IP_ADDRESS,PORT))

  SERVER.listen(100)

  print("\t\t\t SERVER IS WAITING FOR INCOMING REQUESTS.......")
  print('\n')

  acceptConnections()

server_thread = Thread(target=setup)
server_thread.start()