# Sistema de cadastro de produtos
### Optei por fazer algo mais simples, basicamente é um crud onde podemos ver todos os produtos cadastrados, adicionar, pesquisar, atualizar e remover produtos

## Tecnologias utilizadas:
* Para o backend utilizei python + flask e sqlalchemy, principalmente pela simplicidade, familiaridade e pela sintaxe simples; o flask acho simples num geral para a parte de construção e configuração das rotas; o SQLalchemy, além da questão da sintaxe simples, gosto principalmente pela versatilidade, pois caso quisessemos poderiamos trocar o banco de dados usado na aplicação trocando praticamente só o `SQLALCHEMY_DATABASE_URI` 

* Para o banco de dados usei o postgreSQL pela familiaridade também, e pra "cumprir o requisito" dos dois serviços no docker compose. Por exemplo, eu poderia ter usado SQlite mas até onde sei não existe imagem dele no dockerhub. Poderia ter usado também MySQL, porém é nunca utilizei esse banco de dados em nenhum projeto e acredito que não teria tempo hábil de aprender em 1 semana

* Utilizei HTML/CSS/JS pois como o projeto em si era simples, acredito que não teria o porquê de usar um framework como o React por exemplo, só deixaria o projeto desnecessariamente mais complexo

* Por fim, usei Docker e Docker Compose para containerização e orquestração.

## Estrutura do projeto

```
sistema-cadastro-produtos/
├── evidencias/
│   ├── docker/
│   ├── errors/
│   └── front/
├── src/
│   └── server/
│       ├── templates/
│       │   └── index.html
│       └── server.py
├── .env
├── .gitignore
├── checklist.md
├── diario.md
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

## Pré requisitos
* Docker instalado [Documentação](https://www.docker.com/get-started/)
* Docker Compose instalado [Documentação](https://docs.docker.com/compose/)
* .env configurado

## Configuração
1. Clone o repositório
``` bash
git clone https://github.com/Gabrielhanel/sistema-cadastro-produtos.git
cd sistema-cadastro-produtos
```

2. Crie um arquivo chamado .env, copie o .env.example e preencha com suas credenciais

## Rodando o projeto
### Subir os containers
``` bash
docker compose up -d
```
### Verificar se está rodando
``` bash
docker ps
```
### Acessar a aplicação
``` bash
http://localhost:5153
```
### Ver logs da aplicação
``` bash
docker compose logs web
```
### Parar o container
``` bash
docker compose down
```

* Rotas:

|Método  |Rota            |O que faz      |
|--------|----------------|---------------|
|GET   |/     |lista todos    |
|GET   |/get/products/{nome} |busca um produto por nome|
|POST  |/post/products     |cadastra novo  |
|POST |/delete/{id}|remove por ID  |

* Estrutura do banco:
produtos

| Nome da Coluna | Tipo |
| :--- | :--- |
| `product_id` | serial primary key |
| `nome` |  varchar(100) |
| `preco` | float |
| `quantidade` | integer |

## Gerado por IA
* Frontend
* Algumas correções pontuais, principalmente de sintaxe (prefiro a do java, mas optei por fazer em python pelo fato da sintaxe ser mais simples) - tem mais detalhado no diario
* Auxilio na construção do docker compose
