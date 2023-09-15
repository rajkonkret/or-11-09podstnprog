# sqllite3 - baza sql w jednym plik - baza relacyjna
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    query = '''
    CREATE TABLE SqliteDb_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL);'''

    insert = '''
    INSERT INTO SqliteDB_developers (id,name) VALUES (1, 'Radek');
    '''
    select = '''
    SELECT * FROM SqliteDB_developers;'''
    cursor = sql_connection.cursor()
    print("Baza danych została podłaczona")

    for row in cursor.execute(select):
        print(row)  # (1, 'Radek')

    # cursor.execute(query)
    # cursor.execute(insert)
    # sql_connection.commit()

except sqlite3.Error as e:
    print("Bład podczas podłączania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostałą zamknięta")
