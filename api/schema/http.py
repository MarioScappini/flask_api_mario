import sqlite3


class HTTP:
    def create_table():
        connection = sqlite3.connect('database.db')

        with open('schema.sql') as f:
            connection.executescript(f.read())

        connection.commit()
        connection.close()

    def login_user(id, token):
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()

        cur.execute("INSERT INTO active_users (id, token) VALUES (?, ?)",
                    (id, token)
                    )
        cur.close()
        connection.commit()
        connection.close()    

    def get_active_user(id):
        connection = sqlite3.connect('database.db')

        active_users = connection.execute("SELECT * FROM active_users WHERE `id`= ?",(id)).fetchall()
        connection.close()   
        return active_users

    def get_all_active_user():
        connection = sqlite3.connect('database.db')

        active_users = connection.execute("SELECT * FROM active_users").fetchall()
        connection.close()   
        return active_users

    def delete_session(id):
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()

        cur.execute("DELETE FROM active_users WHERE `id` = ?",(id))

        cur.close()

        connection.commit()
        connection.close()  


