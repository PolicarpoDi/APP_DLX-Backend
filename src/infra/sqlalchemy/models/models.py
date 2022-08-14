from xmlrpc.client import Boolean
from sqlalchemy import Float, String, Column, Integer, Boolean
from infra.sqlalchemy.config.database import Base


class Produto(Base):

    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)