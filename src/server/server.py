from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# usei variaveis de ambiente para proteção de algumas informações importantes, como a porta e a senha do banco de dados
load_dotenv() 

# decidi construir o backend com flask principalmente por familiariadade e pela sintaxe simples mesmo
app = Flask(__name__)  

db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{db_password}@db:{db_port}/db_produtos'

# da mesma forma que o flask, usei o sqlalchemy pela familiaridade e principalmente pelo fato de poder lidar com varios bancos diferentes praticamente só trocando a URI
db = SQLAlchemy(app)

# criei uma classe pra usar como uma especie de molde usando a estrutura sugerida pela IA
class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable = False)

# rota principal, retorna todos os produtos puxando do db, acredito que não tenha muito o que explicar, se tratando de um crud esse seria o read
@app.route('/')
def index():
    products = Products.query.all()
    return render_template('index.html', products=products, search_id=None)

# busca os elementos com base no nome, usado na barra de pesquisa, buscando atraves do id do produto
@app.route('/get/products/<string:nome>')
def get_product_by_id(nome):
    product = Products.query.filter_by(nome=nome).first()
    products = [product] if product else []
    return render_template('index.html', products=products, search_id=nome)

# create
@app.route('/post/products', methods=["POST"])
def create_products():
    nome = request.form.get('nome', '').strip()
    preco = request.form.get('preco', '').strip()
    quantidade = request.form.get('quantidade', '').strip()

    if not nome or not preco or not quantidade:
        return redirect('/')

    existing_product = Products.query.filter_by(nome=nome).first()
    if existing_product:
        return 'Erro: Produto ja existe!', 400

    new_product = Products(nome=nome, preco=float(preco), quantidade=int(quantidade))
    db.session.add(new_product)
    db.session.commit()
    return redirect('/')

# update
@app.route('/update/<int:product_id>', methods=['POST'])
def update_product(product_id):
    products = Products.query.get(product_id)
    if products:
        products.nome = request.form['nome']
        products.preco = request.form['preco']
        products.quantidade = request.form['quantidade']
        db.session.commit()
    return redirect('/')

# delete
@app.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    products = Products.query.get(product_id)
    if products:
        db.session.delete(products)
        db.session.commit()
    return redirect('/')

# inicializa a aplicação e o banco de dados
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(host='0.0.0.0', debug=True, port=5153)
    

# algumas coisas aqui não expliquei o porquê do uso pois na verdade é um padrão do proprio flask