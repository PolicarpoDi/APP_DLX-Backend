from fastapi import Depends, FastAPI
from infra.sqlalchemy.config.database import get_db, criar_bd
from sqlalchemy.orm import Session
from schemas.schemas import Produto
from infra.sqlalchemy.repositorios.produtos import RepositorioProduto


criar_bd()

app = FastAPI()

@app.get('/')
def root():
    return {'Mensagem': 'Bem vindo ao APP DLX'}

@app.post('/criar')
def criar_produto(produto: Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@app.get('/produtos')
def listar_produtos(session: Session = Depends(get_db)):
    listar_produto = RepositorioProduto(session).listar()
    return listar_produto