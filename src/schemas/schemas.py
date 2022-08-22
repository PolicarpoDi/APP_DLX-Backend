from pydantic import BaseModel
from typing import List, Optional


class Base(BaseModel):
    class Config:
        orm_mode = True

class UsuarioSimplesSchema(Base):
    id: Optional[int] = None
    nome: str
    telefone: str


class ProdutoSchema(Base):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimplesSchema]
    
    
class ProdutoSimplesSchema(Base):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    

class PedidoSchema(Base):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacao: Optional[str] = "Sem observações"
    
    usuario_id: Optional[int]
    produto_id: Optional[int]
    
    usuario: Optional[UsuarioSimplesSchema]
    produto: Optional[ProdutoSimplesSchema]


class UsuarioSchema(Base):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimplesSchema] = []
    
    
class LoginDataSchema(Base):
    senha: str
    telefone: str
    

