from src.infra.sqlalchemy.models.models import Usuario
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepostorioPedido
from src.schemas.schemas import PedidoSchema
from src.infra.sqlalchemy.config.database import get_db
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter
from typing import List


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PedidoSchema)
def fazer_pedido(pedido: PedidoSchema, session: Session = Depends(get_db)):
    pedido_criado = RepostorioPedido(session).gravar_pedido(pedido)
    return pedido_criado

@router.get('/{id}', response_model=PedidoSchema)
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    try:
        pedido = RepostorioPedido(session).buscar_por_id(id)
        return pedido
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não exite pedido com o ID {id}.')

@router.get('/{usuario_id}/compras', response_model=List[PedidoSchema])
def listar_pedidos(usuario_id: int, session: Session = Depends(get_db)):
    pedidos = RepostorioPedido(session).listar_meus_pedidos_por_usuario_id(usuario_id)
    return pedidos

@router.get('/listar/{usuario_id}/vendas')
def listar_vendas(usuario_id: int, session: Session = Depends(get_db)):
    pedidos = RepostorioPedido(session).listar_minhas_vendas_por_usuario_id(usuario_id)
    return pedidos