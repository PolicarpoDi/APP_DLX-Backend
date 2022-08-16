from fastapi import Depends, FastAPI, status
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import ProdutoSchema, UsuarioSchema, UsuarioSimplesSchema
from src.infra.sqlalchemy.repositorios.produtos import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from typing import List


app = FastAPI()

@app.get('/')
def root():
    return {'Mensagem': 'Bem vindo ao APP DLX'}

# Rota Produtos
# Nas rotas o utilizado é só os schemas, no repositório que é utilizado os modelos

@app.post('/produto/criar', status_code=status.HTTP_201_CREATED, response_model=ProdutoSchema)
def criar_produto(produto: ProdutoSchema, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@app.get('/produto/listar', status_code=status.HTTP_200_OK, response_model=List[ProdutoSchema])
def listar_produtos(session: Session = Depends(get_db)):
    listar_produto = RepositorioProduto(session).listar()
    return listar_produto


# Rota USuários

@app.post('/usuario/criar', status_code=status.HTTP_201_CREATED, response_model=UsuarioSimplesSchema)
def criar_usuario(usuario: UsuarioSchema, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@app.get('/usuario/listar', status_code=status.HTTP_200_OK, response_model=List[UsuarioSimplesSchema])
def listar_usuarios(session: Session = Depends(get_db)):
    listar = RepositorioUsuario(session).listar()
    return listar