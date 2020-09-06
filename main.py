import Display as d
from tkinter import *
from tkinter import filedialog
import connectdatabase as db

class Main:
    def __init__(self):
        self.limit = 440

    def initApp(self):
        bdd = db.connexion(self.limit)
        root = Tk()
        app = d.Display(root,self.limit)
        app.homePage()
        root.geometry("1024x875")
        root.title("PictureOrganizer")       
        menubar = Menu(root)
        root.configure(menu = menubar)
        menufichier = Menu(menubar,tearoff=0) 
        menubar.add_cascade(label="Ajouter", menu=menufichier) 
        menufichier.add_command(label="Ouvrir",command=app.UploadAction) 
        menuFiltre = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Trier", menu=menuFiltre)
        listFilter = app.filter()
        menuFiltre.add_command(label= "All",command= app.all) 
        for el in listFilter:
            menuFiltre.add_command(label= el[0],command=lambda year = el[0]: app.getPictureByear(year)) 
        root.mainloop()   

if __name__ == "__main__":
    app = Main()
    app.initApp()         
