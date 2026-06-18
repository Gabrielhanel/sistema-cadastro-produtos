### Considerações iniciais
* Bom, acredito que minha primeira duvida foi o projeto que eu usaria; achei que um sistema de cadastro de produtos seria relativamente muito simples

* Ao considerar as stacks iniciais, optei por inicialmente utilizar apenas banco de dados, servidor e frontend de inicio
    * Pensei em usar sqlite como banco de dados, por ja ter trabalhado em projetos anteriores, porém eu não conseguiria subir no docker compose da mesma forma que o postgreSQL, por isso optei por essa segunda opção

---
### Desenvolvimento
* Como ja tinha feito um crud parecido com flask/sqlite esse semestre, decidi replicar algumas partes dele, porém dessa vez usando postgres


* Após copiar uma base do projeto anterior e adaptar para o contexto do meu projeto, minha primeira duvida no desenvolvimento foi como usar o sqlalchemy com o postgres. Até inicialmente eu tentei consultar a documentação do sqlalchemy mas acabou não me ajudando muito, ai pedi pra IA e ela me disse que apenas trocando o endereço ja resolveria, ou seja:

    * configuração anterior:
    ``` python
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    ```

    * sugestão da IA:
    ``` python
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:senha@localhost:5432/meu_banco'
    ```

* Depois de considerar que o meu código estava pronto, eu pedi pra IA identificar possiveis erros lógicos, por exemplo:
    * Sem notar eu estava declarando 2 vezes a variavel `app`, uma pro flask e outra pra fastApi (como o python não aponta esse erro automaticamente, acabei não percebendo), e decidi por retirar a do fastAPI e consequentemente a parte do middleware que controlava o acesso do frontend às requisições, ou seja:

    ```python
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    ```
     * _Observação: como o Flask serve o HTML diretamente, o CORS se torna desnecessário_
    * Ao declarar o endereço do db, eu estava declarando as variaveis de forma errada:

    ``` python
    # errada:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:${db_password}@localhost:5433/db_produtos'
    #correta:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{db_password}@localhost:5433/db_produtos'
    ```

    * ao declarar a variavel preco na classe products, sem perceber estava usando `unique=True`, fazendo com que cada produto obrigatoriamente teria que ter um preço diferente, o que não faz sentido


    * (melhoria): Ao tentar buscar um produto por id, eu estava usando `products = Products.query.get(product_id)`
        * Porém eu descobri que existe uma função que retorna automaticamente um erro http 404 se não encontrar o produto, por isso decidi trocar o `get(product_id)` por `get_or_404(product_id)`

### Testando a aplicação pela primeira vez
#### Criação de um produto:
* Produto usado: Iphone 13, valor 3.000, quantidade 1:

![alt text](./evidencias/front/image.png)
![alt text](./evidencias/front/image-2.png)
![alt text](./evidencias/front/image-1.png)

#### Busca de um produto via nome:

![alt text](./evidencias/front/image-9.png)

#### Edição do valor pra 3500:

![alt text](./evidencias/front/image-3.png)
![alt text](./evidencias/front/image-4.png)

#### Edição da quantidade pra 5:

![alt text](./evidencias/front/image-5.png)
![alt text](./evidencias/front/image-6.png)

#### Remoção do produto:

![alt text](./evidencias/front/image-7.png)
![alt text](./evidencias/front/image-8.png)

### Dockerfile - criação
* Tive dificuldade nessa parte só ao iniciar pois não lembrava como fazia, ai voltei no AVA e levei como base esse:

``` dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

* Ai só fui alterando para o contexto do projeto, usando também a IA como apoio. Após procurei no dockerhub uma imagem python. Pensei em usar a alpine, por ser a mais leve que eu conheço, mas após procurar um auxilio na IA para tomada de decisão, descobri que o driver do postgresql que usei (psycopg2-binary) é compilado para glibc, e o alpine usa musl libc, então quebraria. Também pq ambos são baseados em imagens linux diferentes (alpine baseado em Alpine Linux e slim baseado em Debian)

* Tanto glibc quanto musl libc são bibliotecas em C que fornecem as system calls para que os programas se comuniquem com o sistema operacional

* Usei a psycopg2-binary ao invés da psycopg2 principalmente pela simplicidade; a psycopg2 exige que tenhamos o compilador da linguagem C e uma série de configurações a mais.

### Docker compose - criação
* Talvez a parte mais dificil pra mim construir no projeto.. 
* Usei como base a estrutura minima aceita no pdf e só fui alterando conforme usando o contexto do projeto, também usando a IA como apoio, por exemplo, pra saber como usar as variaveis de ambiente em yml

### Subida do container
* Depois de subir o container, eu vi que não deu nenhum erro nem no docker build nem no docker compose up -d, porem não estava aparecendo o container no docker ps.

* Verificando o docker desktop, vi que aparecia o container la porem logo ao lado tinha um erro:
![alt text](./evidencias/errors/image-1.png)
![alt text](./evidencias/errors/image.png)

* Contando com o auxilio da IA, eu descobri que na linha "CMD" eu defini `CMD ["python", "server.py"]`, mas como o arquivo com o codigo do servidor estava dentro de src/server, acabou não localizando, sendo assim ajustei para `CMD ["python", "src/server/server.py"]`

* Após repetir o docker build e o docker compose up, novamente não estava aparecendo. Nos logs me deparei com esse erro:
![alt text](./evidencias/errors/image-2.png)

* Usando a IA como apoio, descobri que o servidor web não estava localizando o db pois ambos estavam em redes diferentes, por isso precisei adicionar uma configuração a mais no docker compose:

``` 
networks:
  app-network:
    driver: bridge
```

* após, em ambos os serviços, adicionei:
```
    networks:
      - app-network
```

Após mudar essas configurações  e reiniciar o container, subiu corretamente:
* `docker build`

![alt text](./evidencias/docker/docker-build.png)

* `docker compose up -d`:

![alt text](./evidencias/docker/docker-compose-up-pt1.png)
![alt text](./evidencias/docker/docker-compose-up-pt2.png)

* `docker ps`

![alt text](./evidencias/docker/docker-ps.png)
