from fastapi import Depends, FastAPI, status
from src.infra.sqlalchemy.config.database import criar_bd, get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import ProdutoSchema, UsuarioSchema, UsuarioSimplesSchema, ProdutoSimplesSchema
from src.infra.sqlalchemy.repositorios.repositorio_produtos import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from typing import List
from fastapi.middleware.cors import CORSMiddleware


#criar_bd()

app = FastAPI()

# CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.put('/produto/atualizar/{id}', status_code=status.HTTP_200_OK, response_model=ProdutoSimplesSchema)
def atualizar_produto(id: int, produto: ProdutoSchema, session: Session = Depends(get_db)):
    RepositorioProduto(session).atualizar(id, produto)
    produto.id = id
    return produto


@app.delete('/produto/deletar/{id}', status_code=status.HTTP_200_OK)
def deletar_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).deletar(id)
    return {"Mensagem": f"Item {id} apagado com sucesso."}


# Rota USuários

@app.post('/usuario/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSimplesSchema)
def signup(usuario: UsuarioSchema, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@app.get('/usuario/listar', status_code=status.HTTP_200_OK, response_model=List[UsuarioSchema])
def listar_usuarios(session: Session = Depends(get_db)):
    listar = RepositorioUsuario(session).listar()
    return listar