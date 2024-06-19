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
        # ==========================UPDATE TABLE=======================================================
        with connection.cursor() as cursor:
            update_sql = '''
            UPDATE CEO_DETAILS
            SET COMPANY = :NEW_COMPANY_VALUE
            WHERE FIRST_NAME = :FIRST_NAME            '''

            # Define the values for the update
            NEW_COMPANY_VALUE = "CALI-CO"
            FIRST_NAME = "VIPHAKONE"
            
            # Execute the update statment
            cursor.execute(update_sql, [NEW_COMPANY_VALUE, FIRST_NAME])

            #Commit the transaction
            connection.commit()

    except Exception as err:
        print('Error while inserting the data', err)
    else:
        print('Update SUCCESSFULLY')
finally:
    connection.close()