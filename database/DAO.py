from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.sale import Sale


class DAO():
    @staticmethod
    def get_anni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            query = """SELECT DISTINCTROW YEAR(Date) 
                    FROM go_daily_sales g"""
            cursor.execute(query)
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_brands():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            query = """SELECT DISTINCTROW Product_brand 
                    FROM go_products"""
            cursor.execute(query)
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_retailers():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                    FROM go_retailers"""
            cursor.execute(query)
            for row in cursor:
                result.append(Retailer(row["Retailer_code"],
                                       row["Retailer_name"],
                                       row["Type"],
                                       row["Country"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def top_vendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *, Unit_sale_price*Quantity as UQ FROM go_daily_sales s JOIN go_products p on s.Product_number = p.Product_number
                    WHERE YEAR(Date)=COALESCE(%s, YEAR(Date)) AND Product_brand=COALESCE(%s, Product_brand) AND Retailer_code=COALESCE(%s, Retailer_code)
                    ORDER BY UQ DESC"""
            cursor.execute(query, (anno, brand, retailer))
            for row in cursor:
                result.append(Sale(row["Retailer_code"],
                                   row["Product_number"],
                                   row["Order_method_code"],
                                   row["Date"],
                                   row["Quantity"],
                                   row["Unit_price"],
                                   row["Unit_sale_price"]
                                   ))
            cursor.close()
            cnx.close()
            return result
