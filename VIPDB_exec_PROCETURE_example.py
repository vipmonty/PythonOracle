from VIPDB_on_flask import get_connection

#reference link:https://youtu.be/kcy1U7TIee4

try:
    conn = get_connection()
except Exception as err:
    print('Error while connecting to the database:', err)
else:
    try:
        cur = conn.cursor()
        data = ('John','Connor','The Future', 1066,'SkyNet@gmail.com')
        cur.callproc('INSERT_CEO_DETAILS', data)
    except Exception as err:
        print('Exception raised while executing the procedure ', err)
    else:
        print('Procedure Executed')
    finally:
        cur.close()
finally:
    conn.close()
