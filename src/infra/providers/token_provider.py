from datetime import datetime, timedelta
from jose import jwt

#CONFIG
SECRET_KEY = 'c37d837479ea95daeca9026bfb1c5b18'
ALGORITHM = 'HS256'
EXPIRES_IN_MINUTES = 3000

def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTES)
    
    dados.update({'exp': expiracao})
    
    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt
    
def verificar_access_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')       