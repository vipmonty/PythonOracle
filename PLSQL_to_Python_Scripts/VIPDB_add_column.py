import os
from dotenv import load_dotenv
import oracledb

load_dotenv()  # Load environment variables from .env file

def get_connection():
    try:
        user = os.getenv('ORACLE_USER')
        pw = os.getenv('ORACLE_PASSWORD')
        dsn = os.getenv('ORACLE_DSN')

        connection = oracledb.connect(
            user=user,
            password=pw,
            dsn=dsn
        )
        print("Successfully connected to Oracle Database")
        return connection
    except Exception as err:
        print('Error while connecting to the database:', err)
        return None

def add_column(table_name, column_name, data_type):
    connection = get_connection()
    if connection is None:
        return False

    try:
        cur = connection.cursor()
        alter_table_sql = f"ALTER TABLE {table_name} ADD {column_name} {data_type}"
        cur.execute(alter_table_sql)
        connection.commit()
        print(f"Column '{column_name}' added successfully to table '{table_name}'")
        return True
    except Exception as err:
        print('Error while adding the column:', err)
        return False
    finally:
        if cur:
            cur.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    table_name = input("Enter table name: ")
    column_name = input("Enter column name: ")
    data_type = input("Enter data type (e.g., VARCHAR2(100)): ")

    success = add_column(table_name, column_name, data_type)
    if success:
        print("Column added successfully.")
    else:
        print("Failed to add the column.")
