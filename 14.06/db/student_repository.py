from db.db_config import connection

def create_student(name: str, age: int, course: str, email: str | None, status: str = "active"):
    q = """
    INSERT into students 
    (name, age, course, email, status) VALUES
    (%s,%s, %s, %s, %s)
    """
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(q, (name, age, course, email, status))
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def get_all_students():
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("select * from students")
        return cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def get_by_id(id: int):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("select * from students where id = %s", (id,))
        return cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
def delete_by_id(id: int):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("delete from students where id = %s", (id,))
        connection.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(e)
    finally:
        cursor.close()
def update_name_by_id(id: int, name: str):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("update students set name = %s where id = %s", (name, id))
        connection.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def get_count_students():
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("select count(*) as total_count from students")
        return cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        cursor.close()

print(get_count_students())