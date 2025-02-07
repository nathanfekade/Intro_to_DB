import mysql.connector



try:
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="password"  
    )

    mycursor = mydb.cursor()

    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")

    mydb.database = "alx_book_store"

    print(f"Database alx_book_store created successfully!")


except mysql.connector.Error as err:
    if err.errno == 1007: 
        print(f"Database alx_book_store already exists.")
    else:
        print(f"Error connecting or creating database: {err}")
except Exception as e: 
    print(f"An unexpected error occurred: {e}")

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()



