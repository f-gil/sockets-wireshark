import socket

host = ''
port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print('Aguardando conexão')

conx, ender = server.accept()
print('Conectando em', ender)
while True:
    data = conx.recv(1024)
    resp = 'Cadastro Efetuado!'
    print(data.decode())
    if not data:
        print('Conexão encerrada!')
        conx.close()
        break
    conx.sendall(resp.encode())


