from sqlalchemy.orm import Session
from schemas.schemas import Produto
from infra.sqlalchemy.models import models


class RepositorioProduto():

    def __init__(self, session: Session):
        self.session = session

    def criar(self, produto: Produto):
        db_produto = models.Produto(nome=produto.nome, 
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel)
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto        
 

    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos


    def remover(self):
        pass


    def obter(self):
        pass