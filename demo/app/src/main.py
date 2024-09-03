import psycopg2

from config import HOST, PORT, USER, PASSWORD, NAME


try:
    connection = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=NAME,
        port=PORT
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print("[INFO] Successful connection to PostgreSQL")
        print(cursor.fetchone())

except Exception as ex:
    print("[ERROR] Cannot connect to PostgreSQL", ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
