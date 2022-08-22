from src.routers import routers_produtos, routers_pedido, routers_auth
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

# Rota PRODUTOS
app.include_router(routers_produtos.router, prefix='/produto')

# Rota SEGURANÇA: AUTENTICAÇÃO E AUTORIZAÇÃO 
app.include_router(routers_auth.router, prefix='/auth')

# Rota PEDIDOS
app.include_router(routers_pedido.router, prefix='/pedido')