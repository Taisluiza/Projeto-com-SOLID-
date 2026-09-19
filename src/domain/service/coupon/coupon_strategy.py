from abc import ABC, abstractmethod

class CouponStrategy(ABC):
    @abstractmethod
    def apply_discount(self, value: float):
        pass


class BlackFridayCoupon(CouponStrategy):
    def apply_discount(self, value: float):
        if value < 300:
            raise ValueError("O valor deve ser maior que 300")
        return value * 0.20


class NatalCoupon(CouponStrategy):
    def apply_discount(self, value: float):
        if value < 800:
            raise ValueError("O valor deve ser maior que 800")
        return value * 0.30


