from pydantic import SecretStr

from sqlalchemy.orm import Session
from src.schemas.schemas import UsuarioSchema
from src.infra.sqlalchemy.models.models import Usuario
from sqlalchemy import select


class RepositorioUsuario():
    
    def __init__(self, session: Session):
        self.session = session
        
    
    def criar(self, usuario: UsuarioSchema):
        usuario_bd = Usuario(nome=usuario.nome,
                             senha=usuario.senha,
                             telefone=usuario.telefone)
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        return usuario_bd
    
    
    def listar(self):
        stmt = select(Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios
        
        