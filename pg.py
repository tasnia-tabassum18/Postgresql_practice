import psycopg2

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="employee",
        user="postgres",
        password="oishee",
        port = "5432"
    )
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    # Execute a simple query
    cursor.execute("SELECT version()")
    # Fetch the query result
    result = cursor.fetchone()
    # Print the PostgreSQL server version
    print("Connected to PostgreSQL")
    print("PostgreSQL version:", result[0])
    # Close the cursor and the connection
    cursor.close()
    conn.close()
except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)

    
#creating table in postgres db
def create_table():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="employee",
        user="postgres",
        password="oishee"
    )

    cursor = conn.cursor()

    table_name = "employee_t"
    table_schema = """
                    CREATE TABLE IF NOT EXISTS employee_t (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255),
                        designation VARCHAR(60),
                        salary VARCHAR(100)
                    )
    """.format(table=table_name)

    cursor.execute(table_schema)

    conn.commit()
    cursor.close()
    conn.close()

create_table()

#creating table in postgres db
def create_table():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="employee",
        user="postgres",
        password="oishee"
    )

    cursor = conn.cursor()

    table_name = "employee_t"
    table_schema = """
                    CREATE TABLE IF NOT EXISTS employee_t (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255),
                        designation VARCHAR(60),
                        salary VARCHAR(100)
                    )
    """.format(table=table_name)

    cursor.execute(table_schema)

    conn.commit()
    cursor.close()
    conn.close()

create_table()

#inserting data 


def insert_data():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="employee",
        user="postgres",
        password="oishee"
    )

    cursor = conn.cursor()

    insert_query = "INSERT INTO employee_t (id, name, designation,salary) VALUES (%s, %s, %s, %s)"
    values = ("1", "Aelin", "Software Engineer", "50000")

    cursor.execute(insert_query, values)

    conn.commit()

    cursor.close()
    conn.close()

insert_data()
def show_data():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="employee",
        user="postgres",
        password="oishee"
    )

    cursor = conn.cursor()

    query ="SELECT * FROM employee_t" 

    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)


    conn.commit()

    cursor.close()
    conn.close()

show_data()