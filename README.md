# Spotnews

Spotnews é um sistema para gerenciar um site de notícias desenvolvido usando o Django, Django Rest Framework e MySQL.

## Executando o projeto

 1. Clone o repositório:

```bash
git clone git@github.com:KanandaRibas/spotnews.git
```

2. Entre na pasta do repositório que você acabou de clonar:

```bash
cd spotnews
```

3. Crie o ambiente virtual para o projeto:

```bash
python3 -m venv .venv
```

4. Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

5. Instale as dependências no ambiente virtual:

```bash
python3 -m pip install -r dev-requirements.txt
```

6. Execute a aplicação:

```bash
python3 manage.py runserver
```

Abra no seu navegador:
http://127.0.0.1:8000/

Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. 


## Para rodar o MySQL via Docker:
 
- Para buildar a imagem:
 ```bash
 docker build -t spotnews-db .
 ```
- Para executar o container - as variáveis de acesso foram definidas na variável DATABASES, do arquivo settings.py:
 ```bash
 docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db
 ```
  O MySQL utiliza por padrão a porta 3306. Se já houver outro serviço utilizando esta porta, considere desativá-lo ou mudar a porta no comando acima.

## 
O projeto foi utilizado como avaliação para o módulo de certificações eletivas de Python do curso de desenvolvimento web Full-Stack da [Trybe](https://app.betrybe.com).
