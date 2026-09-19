from typing import List

from src.domain.ports.outbound.repository_protocol import (
    CartRepositoryProtocol, GetRepositoryProtocol, DeleteRepositoryProtocol, InsertRepositoryProtocol
)


LIST_CART = []

class CartRepository(
    GetRepositoryProtocol,
    DeleteRepositoryProtocol,
    InsertRepositoryProtocol
):
    def __init__(self):
        self._carts = LIST_CART


    def save(self, data:dict):
        self._carts.append(data)
        
        
    def delete(self, item_id: str):
        result = [
            unique for unique in self._carts
            if unique.get_cart_id() == item_id
        ]
        self._carts.remove(result[0])


    def read(self, item_id: str):
        result = [
            unique for unique in self._carts
            if unique.get_cart_id() == item_id
        ]
        return result




   
