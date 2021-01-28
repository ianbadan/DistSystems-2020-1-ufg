# Servidor de diretórios para descoberta automática de servidor <h1>
É possivel rodar esses testes tem uma maquina local, basta colocar o IP local dentro do arquivo ConstRPYC.py, mas a ideia central é utilizar como um sistema distribuído e para isso, foi utilizado o AWS e três máquinas EC2 t2.micro, uma máquina será para o servidor de diretórios, a outra máquina será um cliente e a terceira máquina será um servidor.

Os arquivos que devem estar dentro de cada máquina são os seguintes:

* Servidor de diretórios: serverDirectory.py e constRPYC.py

* Cliente: client.py e constRPYC.py

* Servidor: server.py e constRPYC.py

Note que o arquivo constRPYC.py está presente em todas as máquinas, pois se presume que um servidor de diretório é amplamente conhecido pelo clientes e servidores, por isso que o arquivo deve estar no presente tanto no cliente, quanto no servidor. Esse arquivo deve conter o IP e Porta de conexão do servidor de diretórios, se estiver utilizando de forma distribuída, deve ser o IP da máquina utilizada para o servidor de diretório no AWS ou na plataforma de sua preferência, caso tenha feito no AWS, é necessario ajustar os grupos de segurança para permiter a comunicação entre as máquinas na porta determinada.

## O que cada código faz <h2>

* O serverDirectory.py é o servidor de diretórios onde serão guardados os IPs e portas do servidores, para assim que os clientes possam descobrir os servidores que estão buscando e realizar a conexão e comunicação entre cliente e servidor.

* O client.py consiste na implementação do cliente que fará as requisições, primeiramente será feita a chamada para o diretorio do servidor, para descobrir o endereço e porta e depois fara a requisição para o servidor.

* O server.py é a implementação do servidor, primeiro irá mandar para o diretório o seu ip e porta do momento e então esperá as requisições do cliente, para assim poder responder.

## Como utilizar <h2>

Para o funcionamento desse sistema é necessário rodar cada implementação(client.py, server.py e serverDirectory.py) em uma instância diferente do AWS e ajustar o arquivo de constRPYC.py, alterando o DIR_SERVER para o ip da máquina do servidor de diretorios e o DIR_PORT para o porta que será utlizada. 

Um futuro ajuste é adaptar o codigo do serverDirectory para que sempre que programa seja executado, ele pegue o ip da maquina atual e guarde nesse arquivo automaticamente, para que não seja necessário ficar alterando caso a maquina do diretório mude.

## Melhorias <h2>

Algumas melhorias foram implementadas no Servidor de Diretório para a segunda parte do trabalho, são elas:

* Não registrar novamente um nome já existente; 

* Evitar o lookup de nomes não existentes;

* Remover o registro de um nome existente.

E foram acrescentadas novas funcionalidades ao servidor da aplicação para excluir e consultar elementos da lista.
