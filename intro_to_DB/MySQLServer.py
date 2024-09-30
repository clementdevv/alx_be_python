import mysql.connector
from mysql.connector import Error

def create_database():
    # Database connection parameters
    host = 'localhost'  # Adjust if your MySQL server is on a different host
    user = 'root'  # Replace with your MySQL username
    password = 'My_1_&_only_me'  # Replace with your MySQL password

    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        
        if connection.is_connected():
            print("Connected to MySQL server")

            # Create a cursor object
            cursor = connection.cursor()

            # Attempt to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
