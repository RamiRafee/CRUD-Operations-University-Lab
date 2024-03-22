import mysql.connector

def connect_to_db():
    # Database connection parameters
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'jinroot',
        'database': 'mycvproject'
    }


    try:
        # Connect to the database
        connection = mysql.connector.connect(**config)
        print("Connected to the database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None