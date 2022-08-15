from pydantic import BaseModel
from typing import Optional, List


class Base(BaseModel):
    orm_mode = True

class Usuario(Base):
    id: Optional[str] = None
    nome: str
    telefone: str

class Produto(Base):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

class Pedido(Base):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'


