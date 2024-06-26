import oracledb

def insert_record(first_name, last_name, company, age):
    connection = None
    cur = None
    try:
        pw = "YOUR_PASSWORD"  # Replace with your secure password management
        connection = oracledb.connect(
            user="ADMIN",
            password=pw,
            dsn="(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.us-sanjose-1.oraclecloud.com))(connect_data=(service_name=g5dda15b7e5cf8c_vipdb_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"
        )
        print("Successfully connected to Oracle Database")
    except Exception as err:
        print('Error while connecting to the database', err)
        return False
    else:
        try:
            cur = connection.cursor()
            insert_sql = """
            INSERT INTO CEO_DETAILS (first_name, last_name, company, age)
            VALUES (:1, :2, :3, :4)
            """
            cur.execute(insert_sql, (first_name, last_name, company, age))
            connection.commit()
            print("Record inserted successfully")
            return True
        except Exception as err:
            print('Error while inserting the data', err)
            return False
        finally:
            if cur is not None:
                cur.close()
            if connection is not None:
                connection.close()

if __name__ == "__main__":
    # Example usage
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    company = input("Enter company: ")
    age = int(input("Enter age: "))

    success = insert_record(first_name, last_name, company, age)
    if success:
        print("Insertion completed.")
    else:
        print("Insertion failed.")
