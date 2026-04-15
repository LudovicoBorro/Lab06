from database.DAO import DAO

class Model:

    def __init__(self):
        self._vendite = {}

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
            self._vendite[(v.Retailer_code, v.Product_number, v.Order_method_code)] = v

        return self._vendite