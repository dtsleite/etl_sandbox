# Apresentação
Esta aplicação python realiza a extração assíncrona dos dados fornecidos por um serviço web de stream relativo a mudanças recentes realizadas nas páginas da Wikipedia.

Após os dados serem extraídos são então armazenados em tempo real em um banco de dados local SQLITE3 e em seguinda a quantidade de escritas por segundo podem ser acessadas através de um dashboard servido em uma página web.

### Arquitetura
![Alt text](https://user-images.githubusercontent.com/18425415/58600590-a007a080-825b-11e9-8b0b-df3169bf68e7.JPG?raw=true "Python ETL architecture")

#### Tecnologias utilizadas:
- Python 3
- SqLite3
- Flask

# Instruções de uso

As instruções a seguir são para colocar a aplicação em execução desde que todos os requerimentos sejam satisfeitos. Ver em Requerimentos de sistema.

1-Realizar o clone deste repositório

2-Acessar a pasta do clone

3-Em um terminal Linux execute o comando source init.sh (comando responsavel por instalar as dependências e iniciar o extrator de dados)
Se tudo correu como o esperado serão vistos os dados sendo extraídos no formato JSON conforme a tela abaixo:
![Alt text](https://user-images.githubusercontent.com/18425415/58528579-69734c80-81ad-11e9-86f8-4787cedd5c9e.JPG?raw=true "Title")

4 - Em um novo terminal acesse novamente a mesma pasta deste repositório e digite o comando source init_dashboard.sh

Abra seu navegador de preferência e acesse o endereço: http://localhost:8080

Você deverá visualizar o dashboard sendo atualizado com a quantidade de edições capturadas por segundo.

![Alt text](https://user-images.githubusercontent.com/18425415/58601702-66856400-8260-11e9-9282-2dbd94e226e3.JPG?raw=true "Python ETL dashboard")


