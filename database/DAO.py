from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.vendita import Vendita


class DAO:

    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                select distinct year(gds.`Date`)
                from go_daily_sales gds
        """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row['year(gds.`Date`)'])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getBrands():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                select distinct gp.Product_brand
                from go_products gp
        """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row['Product_brand'])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getRetailers():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                select *
                from go_retailers
        """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Retailer(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getVendite():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                select *
                from go_daily_sales
        """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Vendita(**row))

        cursor.close()
        cnx.close()
        return res