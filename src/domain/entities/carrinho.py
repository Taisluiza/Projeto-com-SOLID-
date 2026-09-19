import uuid
from src.domain.entities.produto import Produto
from typing import List
from enum import Enum, auto


class CarrinhoStatus(Enum):
    ATIVO = auto()
    FINALIZADO = auto()
    EXPIRADO = auto()


class Carrinho:
    def __init__(self, products: List[Produto], carrinho_id: str):
        self._products = products
        self._carrinho_id = carrinho_id
        self._status = CarrinhoStatus.ATIVO


    def get_id(self):
        if not self._carrinho_id:
            self._carrinho_id = uuid.uuid4()
        return self._carrinho_id


    def add_novo_produto(self, produto: Produto):
        self._products.append(produto)


    def switch(self, new_status):
        self._status = new_status
        return self._status


    def get_status(self):
        return self._status


    def _cal_subtotal(self):
        prices = [
            product.get_preco() for product in self._products
            if product.is_available() is True
        ]
        return sum(prices)


    def get_subtotal(self):
        return self._cal_subtotal()
    
