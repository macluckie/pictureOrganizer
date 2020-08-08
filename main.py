import display as d
from tkinter import *
from tkinter import filedialog
import connectdatabase as db

bdd = db.connexion()

root = Tk()
app = d.Display(root)
root.geometry("512x475")
root.title("PictureOrganizer")       
menubar = Menu(root)
root.configure(menu = menubar)
menufichier = Menu(menubar,tearoff=0) 
menubar.add_cascade(label="Ajouter", menu=menufichier) 
# menubar.add_command(label="test1") 
menufichier.add_command(label="Ouvrir",command=app.UploadAction) 

menuFiltre = Menu(menubar,tearoff=0)
# ici rajouter les filtres en récupérant les années distincte de création des fichiers dans la bdd (sqlite).

menubar.add_cascade(label="Trier", menu=menuFiltre)





root.mainloop()