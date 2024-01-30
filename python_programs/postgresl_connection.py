import psycopg2


def get_db_connection():
    try:
        con = psycopg2.connect(
            database="school_db",
            user="rm_user",
            password="tiger1",
            host="localhost",
            port='5432'
        )
        # print(f"database connection is: {con}")
        return con
    except Exception as e:
        print(str(e))
        return None


if __name__ == "__main__":
    db_connection = get_db_connection()

    cursor_obj = db_connection.cursor()
    cursor_obj.execute("SELECT * FROM rooms")
    result = cursor_obj.fetchall()
    print(f"Result set: \n{result}")
