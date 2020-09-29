import psycopg2

try:
    connection = psycopg2.connect(
                    user = 'postgres',
                    password = 'Elisett12!',
                    host = 'localhost',
                    port = '5432',
                    database = 'airline_db',
                    )
    cursor = connection.cursor()
    postgreSQL_select_Query = """SELECT * from customer; """
    postgreSQL_insert_Query = """INSERT INTO airport  VALUES 
	                    ('ORD', 'USA', 'IL', '41.9742 N', '87.9073 W'),
	                    ('LAX', 'USA', 'CA', '33.9416 N', '118.4085 W'),
	                    ('ATL', 'USA', 'GA', '33.6407 N', '84.4277 W'),
	                    ('JFK', 'USA', 'NY', '40.6413 N', '73.7781 W'),
	                    ('HKG', 'CHINA', 'HK', '22.3080 N', '113.9185 E');
                    """
    cursor.execute(postgreSQL_insert_Query)
    count = cursor.rowcount
    connection.commit()
    print (count, "Record inserted successfully into airport table")

except (Exception, psycopg2.Error) as error :
    print ("Error while inserting data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")