import sqlite3

class connexion:

    def __init__(self, limit = 440):  
        self.limit = limit
        self.timeout = 3000
        try:            
            sqliteConnection=sqlite3.connect('picture_orga.db',self.timeout)
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
            cursor.close()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
            print("The SQLite connection is closed")

    def insert(self,path,date):
        sql=sqlite3.connect('picture_orga.db',self.timeout)
        sql.execute("INSERT INTO picture (path,date) VALUES(?,?)",(path,date))
        sql.commit()
        sql.close()

    def selectAll(self):
        sql=sqlite3.connect('picture_orga.db',self.timeout)
        res = sql.execute("SELECT * FROM picture LIMIT "+ str(self.limit))
        result = res.fetchall()
        sql.close()
        return result

    def checkDoublon(self,path):
        sql=sqlite3.connect('picture_orga.db',self.timeout)
        res = sql.execute("SELECT path FROM picture WHERE path= ?",(path,))
        result = res.fetchall()
        sql.close()
        return result


    def filterList(self):
        sql=sqlite3.connect('picture_orga.db',self.timeout)
        res = sql.execute("SELECT DISTINCT date FROM picture")
        result = res.fetchall()
        sql.close()
        return result


    def getPictureByYear(self,year):
        sql=sqlite3.connect('picture_orga.db',self.timeout)
        res = sql.execute("SELECT path  FROM picture WHERE date= ? LIMIT ?",(year,str(self.limit)))
        result = res.fetchall()
        sql.close()
        return result


    def paginatePicture(self,ofset,filtre):     
        sql=sqlite3.connect('picture_orga.db',self.timeout)
        if int(filtre) > 0:                
            res = sql.execute("SELECT * FROM picture WHERE date= ? LIMIT ?,?" ,(str(filtre), str(ofset),str(self.limit)))
        else:            
            res = sql.execute("SELECT *  FROM picture  LIMIT ?, ?",(ofset,str(self.limit)))       
                                 
        result = res.fetchall()        
        sql.close()
        return result














                