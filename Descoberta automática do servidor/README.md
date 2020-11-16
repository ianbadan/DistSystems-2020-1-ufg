O client.py consiste na implementação do cliente que fará as requisições, primeiramente será feita a chamada para o diretorio do servidor, para descobrir o endereço e porta e depois fara a requisição para o servidor.

O server.py é a implementação do servidor, que vai rodar esperando as requisições do cliente, mas antes vai mandar para o diretório o seu ip e porta do momento.

Já o serverDirectory.py é o diretório do servidor onde será guardados os IPs e portas do servidores para que os clientes possam usar para descobrir os servidores e mandar mensagem para aquele que está procurando.

O arquivo constRPYC.py é o arquivo que está o IP e porta do diretório do servidor.
Arquivos para a implementação do trabalho, para o funcionamento do mesmo é necessário rodar cada implementação(client.py, server.py e serverDirectory.py) em uma instância diferente do AWS e ajustar o arquivo de constRPYC.py, ajusta o DIR_SERVER para o ip da máquina que será o diretório do servidor, um futuro ajuste é adaptar o codigo do serverDirectory para que sempre que programa seja executado, ele pegue o ip da maquina atual e guarde nesse arquivo automaticamente, para que não seja necessário ficar alterando caso a maquina do diretório mude.

Melhorias foram implementadas no Servidor de Diretório para:
a) Registrar novamente um nome já existente;
b) Evitar o lookup de nomes não existentes;
c) Remover o registro de um nome existente.

E foram acrescentadas novas funcionalidades ao servidor da aplicação para excluir e consultar elementos da lista.