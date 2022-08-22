from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'])

# gera o hash de acordo com o texto informado
def gerar_hash(texto):
    return pwd_context.hash(texto)

# Verifica o texto e o hash que esta informando
def verificar_hash(texto, hash):
    return pwd_context.verify(texto, hash)

 
 