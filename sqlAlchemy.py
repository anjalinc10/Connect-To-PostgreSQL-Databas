from sqlalchemy import create_engine
  
# DEFINE THE DATABASE CREDENTIALS
user = 'postgres'
password = 'anjali'
host = 'localhost'
port = 5432
database = 'postgres'
  
# PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
  
  
if __name__ == '__main__':
  
    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        print(
            f"Connection to the {host} for user {user} created successfully.")

        result = engine.execute( "SELECT * FROM employee where name='anjali';")
        for i in result:
            print(i)

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)