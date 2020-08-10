import sqlite3

class connexion:

    def __init__(self):
        try:            
            sqliteConnection=sqlite3.connect('picture_orga.db',timeout=30000)
            cursor = sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")

            request='''
                    CREATE TABLE IF NOT EXISTS picture 
                    (
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
        # finally:
        #     if (sqliteConnection):
        #         sqliteConnection.close()
        #         print("The SQLite connection is closed")

    def insert(self,path,date):
        sql=sqlite3.connect('picture_orga.db',timeout=30000)
        sql.execute("INSERT INTO picture (path,date) VALUES(?,?)",(path,date))
        sql.commit()
        sql.close()
        print('rec ok')

    def selectAll(self):
        sql=sqlite3.connect('picture_orga.db',timeout=30000)
        res = sql.execute("SELECT * FROM picture")
        print(res.fetchall())
        sql.close()







                