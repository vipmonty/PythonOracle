import getpass
import oracledb

# go to this link for instructions: https://oracle.github.io/python-oracledb/
# go to this link to continue tutorial: https://oracle.github.io/python-oracledb/samples/tutorial/Python-and-Oracle-Database-The-New-Wave-of-Scripting.html

# pw = getpass.getpass("Enter password: ")
pw = "Sky8pr24!!Sky8pr24!!"
connection = oracledb.connect(
    user="ADMIN",
    password=pw,
    dsn="(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.us-sanjose-1.oraclecloud.com))(connect_data=(service_name=g5dda15b7e5cf8c_vipdb_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))")  # the connection string copied from the cloud console

print("Successfully connected to Oracle Database")

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

# ===================================SELECT STATEMENTS=================================
cur = connection.cursor()
cur.execute("Select * from todoitem")
res = cur.fetchall()
for row in res:
    print(row)

