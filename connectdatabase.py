import sqlite3

class connexion:
    def __init__(self):
        try:
            sqliteConnection=sqlite3.connect('picture_orga.db')
            cursor = sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")

            request='''
                    CREATE TABLE IF NOT EXISTS picture 
                    (
                         id INTEGER PRIMARY KEY,
                        path varchar(255) NULL,
                        date DATE NULL
                      
                    ); 
            '''
            cursor.execute(request)
            

            # check = '''SELECT * FROM picture;
            # '''

            # cursor.execute(check)
            # res = cursor.fetchall()   
            # print(res)         
            cursor.close()



        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")



                