from sqlalchemy.orm import Session
from src.schemas.schemas import ProdutoSchema
from src.infra.sqlalchemy.models import models
from sqlalchemy import update, delete


class RepositorioProduto():

    def __init__(self, session: Session):
        self.session = session

    def criar(self, produto: ProdutoSchema):
        db_produto = models.Produto(nome=produto.nome, 
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel,
                                    usuario_id=produto.usuario_id)
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto        
 
    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos

    def atualizar(self, id: int, produto: ProdutoSchema):
        update_stmt = update(models.Produto).where(
            models.Produto.id == id).values(nome=produto.nome, 
                                            detalhes=produto.detalhes,
                                            preco=produto.preco,
                                            disponivel=produto.disponivel)
        self.session.execute(update_stmt)
        self.session.commit()

    def deletar(self, id: int):
        delete_stmt = delete(models.Produto).where(
            models.Produto.id == id)
        self.session.execute(delete_stmt)
        self.session.commit()