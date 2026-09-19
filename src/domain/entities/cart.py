import uuid
from typing import List
from enum import StrEnumEnum, auto

from domain.entities.product import product


class cartStatus(StrEnumEnum):
    ACTIVE = auto()
    FINISHED = auto()
    EXPIRED = auto()


class cart:
    def __init__(self, products: List[product], cart_id: str):
        self._products = products
        self._cart_id = cart_id
        self._status = cartStatus.ACTIVE


    def get_cart_id(self):
        if not self._cart_id:
            self._cart_id = uuid.uuid4()
        return self._cart_id


    def add_novo_product(self, product: product):
        self._products.append(product)


    def switch(self, new_status):
        self._status = new_status
        return self._status


    def get_status(self):
        return self._status


    def _cal_subtotal(self):
        prices = [
            product.get_price() for product in self._products
            if product.is_available() is True
        ]
        return sum(prices)


    def get_subtotal(self):
        return self._cal_subtotal()
    
