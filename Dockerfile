# imagem base do python mais básica; como comentado também no diário, usamos a slim pois o driver do postgresql que usei (psycopg2-binary) é compilado para glibc, e o alpine usa musl libc, então quebraria ao tentarmos subir o container
FROM python:3.11-slim

# diretório dentro do container, usei /app por convenção
WORKDIR /app

# copia primeiro só o arquivo com as dependências. se não me falha a memória, lembro de ter sido comentado pelo professor em algum momento durante a introdução do docker, que essa é uma boa pratica pois se o código mudar mas o requirements não, ele reinstala tudo do 0, aumentando (e muito) o tempo necessario pra subir um container
COPY requirements.txt .

# instalação dos pacotes; o --no-cache-dir desativa o cache, o que segundo a própria documentação do docker, "reduz o tamanho da imagem Docker ao não armazenar dados de cache desnecessários"
RUN pip install --no-cache-dir -r requirements.txt

# copia o restante do projeto para o container
# se apenas o código mudar, o Docker reutiliza a camada do pip install sem reinstalar todos os pacotes do requirements.txt novamente
COPY . .

# porta definida no projeto para rodar a api (app.run(debug=True, port=5153))
EXPOSE 5153


# comando que inicia a aplicação
CMD ["python", "src/server/server.py"]
