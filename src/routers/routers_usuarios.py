from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.schemas.schemas import UsuarioSchema, UsuarioSimplesSchema
from src.infra.sqlalchemy.config.database import get_db
from fastapi import Depends, status
from sqlalchemy.orm import Session
from fastapi import APIRouter
from typing import List


router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSimplesSchema)
def signup(usuario: UsuarioSchema, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.get('/listar', status_code=status.HTTP_200_OK, response_model=List[UsuarioSchema])
def listar_usuarios(session: Session = Depends(get_db)):
    listar = RepositorioUsuario(session).listar()
    return listar