# import oracledb
from dotenv import load_dotenv
# import os
from VIPDB_on_flask import get_connection

load_dotenv() # Load environment variables from .env file

try:
    #create a connection
    conn = get_connection()
except Exception as err:
    print('Exception occured while creating a connection ', err)
else:
    try:
        cur = conn.cursor()
        data = [10,11]
        result = cur.callfunc('ADD_INT', int, data)
    except Exception as err:
        print('Exception occured while executing the func', err)
    else:
        print('Result: ',result)
    finally:
        cur.close()

finally:
    conn.close()
