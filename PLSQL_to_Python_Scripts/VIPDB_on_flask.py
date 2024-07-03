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

def get_all_records():
    connection = get_connection()
    if connection is None:
        return [], []

    try:
        cur = connection.cursor()
        cur.execute("SELECT * FROM CEO_DETAILS")
        columns = [col[0] for col in cur.description]
        records = cur.fetchall()
        return columns, records
    except Exception as err:
        print('Error while fetching the data:', err)
        return [], []
    finally:
        if cur:
            cur.close()
        if connection:
            connection.close()

def describe_table(table_name):
    connection = get_connection()
    if connection is None:
        return []

    try:
        cur = connection.cursor()
        describe_sql = f"SELECT column_name, data_type, nullable FROM user_tab_columns WHERE table_name = UPPER('{table_name}')"
        cur.execute(describe_sql)
        res = cur.fetchall()
        return res
    except Exception as err:
        print('Error while describing the table:', err)
        return []
    finally:
        if cur:
            cur.close()
        if connection:
            connection.close()

def get_schema():
    connection = get_connection()
    if connection is None:
        return []

    try:
        cur = connection.cursor()
        schema_sql = """
        SELECT table_name, column_name, data_type, nullable 
        FROM user_tab_columns 
        ORDER BY table_name, column_id
        """
        cur.execute(schema_sql)
        res = cur.fetchall()
        schema = [
            {
                'table_name': row[0],
                'column_name': row[1],
                'data_type': row[2],
                'nullable': row[3]
            }
            for row in res
        ]
        return schema
    except Exception as err:
        print('Error while fetching the schema:', err)
        return []
    finally:
        if cur:
            cur.close()
        if connection:
            connection.close()

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
