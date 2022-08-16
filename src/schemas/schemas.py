from pydantic import BaseModel
from typing import List, Optional


class Base(BaseModel):
    class Config:
        orm_mode = True

class UsuarioSchema(Base):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    #produtos: List[produtos] = None
    
    
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
    usuario_id: int
    usuario: Optional[UsuarioSimplesSchema]

    
class PedidoSchema(Base):
    id: Optional[int] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'



