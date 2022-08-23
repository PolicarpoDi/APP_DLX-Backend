from src.jobs.write_notifications import write_notification
from src.middlewares.timer import time_request
from src.routers import routers_produtos, routers_pedido, routers_auth
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, BackgroundTasks
from starlette.middleware.base import BaseHTTPMiddleware


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
# Passando pelo middleware(time_request)
app.add_middleware(BaseHTTPMiddleware, dispatch=time_request)

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

# Jobs
@app.post('/send_email/{email}')
async def send_email(email: str, background: BackgroundTasks):
    background.add_task(write_notification, email, message='Testando job de email!!')
    return {'OK': 'Mensagem enviada em background.'}


