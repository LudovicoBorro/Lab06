from dataclasses import dataclass

@dataclass
class Vendita:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: str
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

    def __eq__(self, other):
        return (self.Retailer_code == other.Retailer_code
                and self.Product_number == other.Product_number
                and self.Order_method_code == other.Order_method_code)

    def __hash__(self):
        return hash((self.Retailer_code, self.Product_number, self.Order_method_code))

    def __str__(self):
        pass