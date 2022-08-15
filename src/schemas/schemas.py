from pydantic import BaseModel
from typing import Optional


class Base(BaseModel):
    class Config:
        orm_mode = True

class UsuarioSchema(Base):
    id: Optional[str] = None
    nome: str
    telefone: str


class ProdutoSchema(Base):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False


class ProdutoSimplesSchema(Base):
    id: Optional[str] = None
    nome: str
    preco: float

    
class PedidoSchema(Base):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'



