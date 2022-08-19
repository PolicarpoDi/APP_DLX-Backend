from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models.models import Pedido, Produto
from src.schemas.schemas import PedidoSchema


class RepostorioPedido():
    
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def gravar_pedido(self, pedido: PedidoSchema):
        pedido_db = Pedido(quantidade=pedido.quantidade,
                            local_entrega=pedido.local_entrega,
                            tipo_entrega=pedido.tipo_entrega,
                            observacao=pedido.observacao,
                            usuario_id=pedido.usuario_id,
                            produto_id=pedido.produto_id)
        self.session.add(pedido_db)
        self.session.commit()
        self.session.refresh(pedido_db)
        return pedido_db
    
    def buscar_por_id(self, id: int):
        query = select(Pedido).where(Pedido.id == id)
        busca_id = self.session.execute(query).scalars().one()
        return busca_id
    
    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int):
        query = select(Pedido).where(Pedido.usuario_id == usuario_id)
        resultado = self.session.execute(query).scalars().all()
        return resultado
    
    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int): 
        query = select(Pedido) \
        .join_from(Pedido, Produto) \
        .where(Produto.usuario_id == usuario_id)
        resultado = self.session.execute(query).scalars().all()
        return resultado