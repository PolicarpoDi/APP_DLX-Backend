import token
from jose import JWTError
from src.routers.routers_auth import obter_usuario_logao
from src.infra.providers import token_provider
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.schemas.schemas import UsuarioSchema, UsuarioSimplesSchema, LoginDataSchema
from src.infra.sqlalchemy.config.database import get_db
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import APIRouter
from typing import List
from src.infra.providers import hash_provider


router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSimplesSchema)
def signup(usuario: UsuarioSchema, session: Session = Depends(get_db)):
    # Verificar se já existe um usuario para o telefone informado
    usuario_localizado = RepositorioUsuario(session).obter_telefone(usuario.telefone)
    
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Já existe um usuario para este telefone.')
    # Criar novo usuario     
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.get('/listar', status_code=status.HTTP_200_OK, response_model=List[UsuarioSchema])
def listar_usuarios(session: Session = Depends(get_db)):
    listar = RepositorioUsuario(session).listar()
    return listar

@router.post('/token', status_code=status.HTTP_202_ACCEPTED)
def login(login_data: LoginDataSchema, session: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone
    
    usuario = RepositorioUsuario(session).obter_telefone(telefone)
    
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha estão incorretos!.')
    
    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha estão incorretos!.')
    # Gerar o token JWT
    token = token_provider.criar_access_token({'sub': usuario.telefone})
    return {'usuario': usuario, 'access_token': token}

@router.get('/me', response_model=UsuarioSimplesSchema)
def me(usuario: UsuarioSchema = Depends(obter_usuario_logao)):
    return usuario