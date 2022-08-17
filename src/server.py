from src.routers import routers_produtos, routers_usuarios
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


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

# Rota ROOT
@app.get('/')
def root():
    return {'Mensagem': 'Bem vindo ao APP DLX'}

# Rota Produtos
app.include_router(routers_produtos.router, prefix='/produto')

# Rota Usuários
app.include_router(routers_usuarios.router, prefix='/usuario')