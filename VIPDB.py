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
        # ==========================CREATE TABLE=======================================================
        cur = connection.cursor()
        sql_insert = """INSERT INTO CEO_DETAILS VALUES (:1,:2,:3,:4)"""#<=represents the fields
        values = [('BONSON','LAY','CALI-CO',24),('JOHNNY','BUN','CALI-CO',24),('KHOM','SISINTHONG','DA VILL',24)]
        cur.executemany(sql_insert, values)
        connection.commit()
        # sql_create = """
        # CREATE TABLE CEO_DETAILS(
        #     FIRST_NAME VARCHAR2(50),
        #     LAST_NAME VARCHAR2(50),
        #     COMPANY VARCHAR2(50),
        #     AGE NUMBER
        # )
        # """
        # cur.execute(sql_create)
        # print('Table Created')
    except Exception as err:
        print('Error while inserting the data', err)
    else:
        print('Insert Completed')
finally:
    cur.close()
    connection.close()

# ===========================CREATE TABLES=========================================
# Create a table
# with connection.cursor() as cursor:

    # cursor.execute("""
    #     begin
    #         execute immediate 'drop table todoitem';
    #         exception when others then if sqlcode <> -942 then raise; end if;
    #     end;""")

    # cursor.execute("""
    #     create table todoitem (
    #         id number generated always as identity,
    #         description varchar2(4000),
    #         creation_ts timestamp with time zone default current_timestamp,
    #         done number(1,0),
    #         primary key (id))""")




    # print(f"Table created {connection.version}")
# ===============================INSERT MULTIPLE ROWS=================================
# Insert some data
# with connection.cursor() as cursor:

#     rows = [("buy redbull", 1),
#             ("Task 2", 0),
#             ("Task 3", 1),
#             ("Task 4", 0),
#             ("Task 5", 1)]

#     cursor.executemany(
#         "insert into todoitem (description, done) values(:1, :2)", rows)
#     print(cursor.rowcount, "Rows Inserted")

# connection.commit()

# # Now query the rows back
# with connection.cursor() as cursor:

#     for row in cursor.execute('select description, done from todoitem'):
#         if (row[1]):
#             print(row[0], "is done")
#         else:
#             print(row[0], "is NOT done")

# ===================================SELECT * STATEMENTS=================================
# cur = connection.cursor()
# cur.execute("Select * from todoitem")
# res = cur.fetchall()
# for row in res:
#     print(row)

# cur.close
# connection.close
# =================================SELECT WHERE STATEMENT================================

# Create a cursor object
# cursor = connection.cursor()

# # Define the SQL query
# query = """
# SELECT *
# FROM todoitem
# WHERE description = :value
# """

# # Execute the query with a parameter value
# cursor.execute(query, value="buy redbull")

# # Fetch all rows matching the query
# rows = cursor.fetchall()

# # Print the results
# for row in rows:
    # print(row)


# =========================CLOSE CURSOR() AND CONNECTION================================

# Close the cursor and connection
# cursor.close()
# connection.close()