from database.DB_connect import DBConnect
from model.prodotto import Prodotto
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
                from go_daily_sales gds, go_products gp, go_retailers gr
                where gds.Product_number = gp.Product_number and gds.Retailer_code = gr.Retailer_code
        """

        cursor.execute(query)

        res = []
        for row in cursor:
            prod = Prodotto(row['Product_number'], row['Product_line'], row['Product_type'], row['Product'], row['Product_brand'],
                            row['Product_color'], row['Unit_cost'], row['Unit_price'])
            ret = Retailer(row['Retailer_code'], row['Retailer_name'], row['Type'], row['Country'])
            res.append(Vendita(retailer=ret, product=prod, Order_method_code=row['Order_method_code'],
                               Date=row['Date'], Quantity=row['Quantity'], Unit_price=row['Unit_price'],
                               Unit_sale_price=row['Unit_sale_price']))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getProducts():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                select *
                from go_products gp
        """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Prodotto(**row))

        cursor.close()
        cnx.close()
        return res