### 1. Estrutura de Arquivos e Pastas
- [X] Repositório ou arquivo compactado segue a estrutura raiz exigida (`meu-projeto-docker/`).  
- [X] Pasta `src/` criada contendo o código-fonte da aplicação.  
- [X] Arquivo `Dockerfile` na raiz do projeto.  
- [X] Arquivo `docker-compose.yml` na raiz do projeto.  
- [X] Pasta `evidencias/` criada para armazenar os prints.  
- [X] Arquivo `diario.md` criado na raiz do projeto.  
- [X] Arquivo `README.md` criado na raiz do projeto.  

---

### 2. A Aplicação (Pasta `src/`)
- [X] A aplicação é funcional e faz algo observável (como responder a uma rota, exibir dados ou processar uma entrada).  
- [X] O código-fonte contém comentários que explicam as decisões de implementação, e não apenas descrições óbvias do que o código faz.  

---

### 3. Dockerfile
- [X] A imagem base foi escolhida e possui uma justificativa escrita em comentário (versão, tamanho, compatibilidade).  
- [X] Cada instrução do arquivo possui comentários explicando o motivo da escolha (ex: explicar a estratégia de cache na cópia de arquivos).  
- [X] A porta exposta (`EXPOSE`) está documentada e é condizente com a porta que a aplicação utiliza.  
- [X] O comando `CMD` ou `ENTRYPOINT` está funcional e com a escolha explicada em comentários.  

---

### 4. Docker Compose (`docker-compose.yml`)
- [X] Possui no mínimo dois serviços configurados e integrados.  
- [X] Utiliza uma das combinações permitidas: App + Banco de dados, App + Nginx, ou App + Redis.  
- [X] As variáveis de ambiente estão declaradas no arquivo (garantindo que credenciais não estejam "hardcoded" no código da aplicação).  
- [X] Existe um volume nomeado configurado para garantir a persistência de dados do segundo serviço (ex: banco de dados).  
- [X] A propriedade `depends_on` foi configurada corretamente para garantir a ordem de inicialização.  
- [X] Ambos os serviços estão funcionando e conseguem se comunicar em rede interna.  

---

### 5. Evidências (Pasta `evidencias/`)
- [X] Print ou vídeo do processo `docker build` concluindo com sucesso (ex: `build.png`).  
- [X] Print do comando `docker compose up` mostrando a inicialização dos serviços (ex: `compose-up.png`).  
- [X] Print com o output do comando `docker ps` exibindo os containers em execução.  
- [X] Print da aplicação rodando e sendo acessada pelo navegador, Postman ou curl (ex: `app-rodando.png`).  

---

### 6. Diário de Desenvolvimento (`diario.md`)
- [X] O diário documenta o processo de desenvolvimento (o que funcionou e o que não funcionou).  
- [X] Contém o registro de erros encontrados durante o trabalho.  
- [X] Inclui as mensagens de erro reais que ocorreram.  
- [X] Explica detalhadamente como cada um dos erros listados foi solucionado.  

---

### 7. Documentação e Integridade (`README.md`)
- [ ] O README possui uma descrição geral sobre o projeto.  
- [X] Inclui obrigatoriamente uma seção intitulada `## Uso de IA`.  
- [X] A seção detalha quais partes do projeto foram geradas ou assistidas por ferramentas de IA (como ChatGPT ou Copilot).  
- [X] A seção de IA explica o que você modificou no código gerado e o que aprendeu a partir disso.  
- [X] Você tem o domínio e entendimento completo sobre tudo o que está sendo entregue (requisito validado em apresentação).