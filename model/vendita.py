from dataclasses import dataclass
from model.prodotto import Prodotto
from model.retailer import Retailer

@dataclass
class Vendita:
    retailer: Retailer
    product: Prodotto
    Order_method_code: int
    Date: str
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

    def __eq__(self, other):
        return (self.retailer == other.retailer
                and self.product == other.product
                and self.Order_method_code == other.Order_method_code)

    def __hash__(self):
        return hash((self.retailer, self.product, self.Order_method_code))

    def __str__(self):
        return (f"Nome prodotto: {self.product.Product} -- Brand prodotto: {self.product.Product_brand} -- "
                f"Nome retailer: {self.retailer.Retailer_name} -- Data vendita: {self.Date} -- "
                f"Ricavo totale: {self.Quantity * self.Unit_sale_price:.2f}€")