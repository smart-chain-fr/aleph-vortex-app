import psycopg2

def connectDatabase(host : str, port : str, database : str, user : str, password : str) :
    print(f"Connecting to database {database} on {host}:{port} as {user}...")
    try:
        dbConnection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
    except Exception as e:
        raise Exception(f"Error connecting to database : {e}")
    print("Connected to database.")
    return dbConnection

def disconnectDatabase(dbConnection) -> None:
    print("Disconnecting from database...")
    try:
        dbConnection.close()
    except AttributeError:
        pass
    except Exception as e:
        raise Exception('Error closing database connection: {}'.format(e))
    print("Disconnected from database.")
    
def initDatabase(dbConnection) -> None:
    print("Initializing database...")
    try:
        sqlToExecute : str = open('src/utils/sql/init.sql', 'r').read()
    except Exception as e:
        raise Exception('Error reading init.sql file: {}'.format(e))
    print("Executing SQL Initialization...")
    try:
        cursor : psycopg2.cursor = dbConnection.cursor()
        cursor.execute(sqlToExecute)
        dbConnection.commit()
        cursor.close()
    except Exception as e:
        raise Exception('Error initializing database: {}'.format(e))
    print("Database initialized.")