import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sh01ad02w03#@#.",
        database="delivery_system"
    )