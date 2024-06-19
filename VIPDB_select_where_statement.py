import getpass
import oracledb

# go to this link for instructions: https://oracle.github.io/python-oracledb/
# go to this link to continue tutorial: https://oracle.github.io/python-oracledb/samples/tutorial/Python-and-Oracle-Database-The-New-Wave-of-Scripting.html
try:
    # pw = getpass.getpass("Enter password: ")
    pw = input('Enter your password Vip:')
    connection = oracledb.connect(
        user="ADMIN",
        password=pw,
        dsn="(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.us-sanjose-1.oraclecloud.com))(connect_data=(service_name=g5dda15b7e5cf8c_vipdb_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))")  # the connection string copied from the cloud console

    print("Successfully connected to Oracle Database")
except Exception as err:
    print('Error while inserting the data', err)
else:
    print(connection.version)
    try:
        # =================================SELECT WHERE STATEMENT================================

        # Create a cursor object
        cursor = connection.cursor()

        # Define the SQL query
        query = """
        SELECT *
        FROM CEO_DETAILS
        WHERE COMPANY = :value
        """

        # Execute the query with a parameter value
        cursor.execute(query, value="CALI-CO")

        # Fetch all rows matching the query
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except Exception as err:
        print('Error while inserting the data', err)
    else:
        print('SELECT WHERE Completed')
finally:
    cursor.close()
    connection.close()