# Demonstração de vulnerabilidade em redes usando sockets em Python e Wireshark

É interessante imaginar porquê as informações que temos online hoje em dia são cobertas por todo tipo de criptografia possível. 
Afim de entender melhor as consequências de possíveis vulnerabilidades em sistemas, 
com esse projeto vamos explorar a possibilidade de captura de um login e senha numa rede desprotegida usando o Wireshark.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Tecnologias utilizadas
* Python
  * Biblioteca [Socket](https://docs.python.org/pt-br/3.8/howto/sockets.html)
  * Biblioteca [Tkinter](https://docs.python.org/3/library/tkinter.html)
   * O código para a janela de interface gráfica em Python, sem o socket, está disponível [aqui](https://github.com/f-gil/sockets-wireshark/blob/main/janela.py).
* Wireshark


### 📋 Pré-requisitos

Para o funcionamento desse projeto é necessário ter o [Python 3](https://www.python.org/downloads/) instalado em sua máquina assim como o [Wireshark](https://www.wireshark.org/download.html).
Ambas as bibliotecas citadas são nativas do [Python 3](https://www.python.org/downloads/).


### 🔧 Execução

Com todo o ambiente pronto, clone esse repositório em sua máquina local e abra os arquivos cliente.py e server.py. 

Os códigos estão feitos para funcionar localmente, mas caso queira conectar 2 computadores que estejam na mesma rede, basta modificar o IP 127.0.0.1 pelo IP do PC que fizer o papel de servidor.


![client.py](https://github.com/f-gil/sockets-wireshark/blob/main/img/client.png)




Abra o Wireshark, se for rodar localmente inicie uma captura através dp "Adapter for loopback traffic capture" que irá apenas capturar o pacotes locais. 
*Caso você rode os programas em computadores diferentes utilize o "Wi-fi" ou "Ethernet" (de acordo com o seu caso) para capturar os pacotes corretamente.*


Dê run em server.py para que ele entre em modo de escuta na porta informada e depois dê run em cliente.py. Na tela de login preencha seus dadose clique em Enviar. 

Em seguida, pare a captura no Wireshark para que seja mais fácil encontrar o pacote desejado. 


A implementação foi feita na camada TCP de acordo com o parâmetro "socket.SOCK_STREAM", vide [documentação](https://docs.python.org/3/library/socket.html). Portanto é nela que você irá procurar. 

*Dica* Você pode digitar o comando *tcp.port==8000* (lembrando que caso mude a porta no código troque o valor 8000 pela porta escolhida) para encontrar os pacotes de forma mais rápida.

Ao encontrar o pacote no Wireshark, você terá uma demonstração de quão fácil se pode obter dados em uma rede desprotegida.

Para facilitar o entendimento incluímos abaixo um gif com todo o procedimento, desde o run do servidor até o rastreio com o Wireshark:

![client.py](https://github.com/f-gil/sockets-wireshark/blob/main/img/execucao.gif)
