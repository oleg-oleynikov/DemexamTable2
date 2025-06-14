    
import psycopg2
from psycopg2 import Error

class Database:
    def __init__(self):
        self.conn = None
        self.connect()
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                port="5432",
                user="postgres",
                password="toor",
                database="demexam"
            )
            print("Успешное подключение к PostgreSQL")
        except Error as e:
            print(f"Ошибка подключения: {e}")
            self.conn = None
    
    def get_products(self):
        if not self.conn:
            return []
        
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT p.article, p.name, p.min_partner_price, 
                           pt.type_name, p.width, pm.quantity * m.current_cost AS "product_price"
                    FROM products p 
                    JOIN product_types pt ON p.product_type_id = pt.product_type_id
                    JOIN product_materials pm ON pm.product_id = p.product_id
                    JOIN materials m ON m.material_id = pm.material_id
                """)
                return cur.fetchall()
        except Error as e:
            print(f"Ошибка запроса: {e}")
            return []
    
    def close(self):
        if self.conn:
            self.conn.close()


db = Database()