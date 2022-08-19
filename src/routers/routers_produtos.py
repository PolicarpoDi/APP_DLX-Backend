from src.infra.sqlalchemy.repositorios.repositorio_produtos import RepositorioProduto
from src.schemas.schemas import ProdutoSchema, ProdutoSimplesSchema
from src.infra.sqlalchemy.config.database import get_db
from fastapi import Depends, status
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException
from typing import List


router = APIRouter()

@router.post('/criar', status_code=status.HTTP_201_CREATED, response_model=ProdutoSchema)
def criar_produto(produto: ProdutoSchema, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@router.get('/listar', status_code=status.HTTP_200_OK, response_model=List[ProdutoSchema])
def listar_produtos(session: Session = Depends(get_db)):
    listar_produto = RepositorioProduto(session).listar()
    return listar_produto

@router.get('/listar/{id}', status_code=status.HTTP_200_OK, response_model=ProdutoSimplesSchema)
def exibir_produto(id: int, session: Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(session).exibir_produto_id(id)
    if not produto_localizado:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Não há um produto com o ID {id}') 
    return produto_localizado

@router.put('/atualizar/{id}', status_code=status.HTTP_200_OK, response_model=ProdutoSimplesSchema)
def atualizar_produto(id: int, produto: ProdutoSchema, session: Session = Depends(get_db)):
    RepositorioProduto(session).atualizar(id, produto)
    produto.id = id
    return produto

@router.delete('/deletar/{id}', status_code=status.HTTP_200_OK)
def deletar_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).deletar(id)
    return {"Mensagem": f"Item {id} apagado com sucesso."}