class product:
    def __init__(self, sku, price, descricao, qtd):
        self._sku = sku
        self._price = price
        self._descricao = descricao
        self._qtd = qtd

    def get_price(self):
        return self._price

    def get_estoque(self):
        if self._qtd > 0:
            result = True
        else:
            result = False
        return result

    def get_product(self):
        return {
            "sku": self._sku,
            "price": self._price,
            "descricao": self._descricao,
            "qtd": self._qtd
        }