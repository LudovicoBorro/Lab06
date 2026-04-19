from database.DAO import DAO
from model.retailer import Retailer

class Model:

    def __init__(self):
        self._vendite = {}
        self.getVendite()

    @staticmethod
    def getAnni():
        return DAO.getAnni()

    @staticmethod
    def getBrands():
        return DAO.getBrands()

    @staticmethod
    def getRetailers():
        return DAO.getRetailers()

    def getVendite(self):
        vendite = DAO.getVendite()

        for v in vendite:
            self._vendite[(v.retailer, v.product, v.Order_method_code)] = v

    def getBestSales(self, anno, brand, retailer):

        check_anno = anno.lower() != "nessun filtro"
        check_brand = brand.lower() != "nessun filtro"
        check_retailer = isinstance(retailer, Retailer)

        filtered_list = []

        # print(self._vendite)

        for v in self._vendite.values():

            if check_anno and v.Date.year != int(anno):       # se check è su nessun filtro non entra qua dentro e va al prossimo if
                continue                                       # se invece check ha qualcosa ma la data è diversa dall'anno richiesto skippa

            if check_brand and v.product.Product_brand != brand:
                continue

            if check_retailer and v.retailer != retailer:
                continue

            filtered_list.append(v)

        best_sales = {v: v.Quantity * v.Unit_sale_price for v in filtered_list}

        best_sales_sorted = dict(sorted(best_sales.items(), key=lambda item: item[1], reverse=True))

        if len(best_sales_sorted) > 5:
            best_five_sales = list(best_sales_sorted)[:5]
        else:
            best_five_sales = list(best_sales_sorted)[:len(best_sales_sorted)]

        return best_five_sales