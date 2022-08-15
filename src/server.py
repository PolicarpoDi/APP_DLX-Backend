from fastapi import Depends, FastAPI, status
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from sqlalchemy.orm import Session
from src.schemas.schemas import ProdutoSchema, ProdutoSimplesSchema
from src.infra.sqlalchemy.repositorios.produtos import RepositorioProduto
from typing import List


app = FastAPI()

@app.get('/')
def root():
    return {'Mensagem': 'Bem vindo ao APP DLX'}

@app.post('/criar', status_code=status.HTTP_201_CREATED, response_model=ProdutoSchema)
def criar_produto(produto: ProdutoSchema, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@app.get('/listar', status_code=status.HTTP_200_OK, response_model=List[ProdutoSchema])
def listar_produtos(session: Session = Depends(get_db)):
    listar_produto = RepositorioProduto(session).listar()
    return listar_produto