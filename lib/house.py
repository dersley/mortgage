from decimal import Decimal

from lib.address import Address


class House:
    def __init__(
        self, address: Address, purchase_price: Decimal, current_value: Decimal
    ):
        self.address = address
        self.purchase_price = purchase_price
        self.current_value = current_value
