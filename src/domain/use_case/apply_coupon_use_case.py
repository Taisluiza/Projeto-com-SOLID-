from domain.entities.cart import cart
from src.domain.service.coupon.apply_coupon import ApplyCouponStrategy
from src.domain.factories.coupon_strategy_factory import TypeCoupon, StrategyCouponFactory



class ApplyCouponUseCase:
    def execute(self, cart: cart, type_coupon):
        subtotal = cart.get_subtotal()
        strategy = StrategyCouponFactory.create(type_coupon)
        discount = ApplyCouponStrategy(strategy).apply_discount(subtotal)
        new_price = subtotal - discount
        return{
            "discount_value": discount,
            "new_subtotal" : new_price, #AJUSTEI
            "cart_id": cart.get_cart_id()
        }

