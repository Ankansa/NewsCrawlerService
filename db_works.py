import mysql.connector
from load_env import *

class DATABASE:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=e_host,
            user= e_user,
            password= e_password,
            database= e_database
        )

        self.cursor = self.db.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS news_details (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            description TEXT,
            published_at DATETIME,
            source VARCHAR(255),
            url VARCHAR(255)
        )
        """)
        self.db.commit()

    def insert_into_db(self , values):

        sql = "INSERT INTO news_details (title, description, published_at, source, url) VALUES (%s, %s, %s, %s, %s)"

        self.cursor.execute(sql, values)

        self.db.commit()