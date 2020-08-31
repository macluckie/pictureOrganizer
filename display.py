from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import os
import time        
from pathlib import Path
import connectdatabase as db

class Display:

    def __init__(self,root):
        self.root = root
        self.frameLabel = "NULL"  
        self.limit = 440

    def UploadAction(self):
        directorie = filedialog.askdirectory()
        contentFolder =  os.listdir(directorie)             
        self.handlerContent(contentFolder,directorie)
        self.root.mainloop()

  
    def handlerContent(self,contentFolder,directorie):
        bdd = db.connexion()
        self.frameLabel.pack_forget()
        progress = ttk.Progressbar(self.root, orient = HORIZONTAL,length = 400, mode = 'determinate')
        progress.pack(side = "top")
        extensions = ['jpeg','jpg','png']
        i =0
        for imge in contentFolder:     
            if i < 80: 
                i = i+ 1     
            
            progress['value'] = i
            self.root.update_idletasks() 
          
            
            if os.path.isdir(directorie + "/"+ imge):
                path = Path(directorie + "/"+ imge)               
                self.handlerContent(os.listdir(str(path)), str(path))            
            for extension in extensions:               
                if imge.lower().endswith(extension):                    
                    if isinstance(bdd.checkDoublon(directorie + "/"+ imge),list):
                        if (len(bdd.checkDoublon(directorie + "/"+ imge)) == 0):
                            bdd.insert(directorie + "/"+ imge,(time.ctime(os.path.getctime(directorie + "/"+ imge)).split()[int(len(time.ctime(os.path.getctime(directorie + "/"+ imge)).split())) - 1]))

        progress.pack_forget() 
        
        progress2 = ttk.Progressbar(self.root, orient = HORIZONTAL,length = 400, mode = 'determinate')
        progress2.pack(side = "top")                   
        progress2['value'] = 100
        self.root.update_idletasks() 
       

    def homePage(self):
        bdd = db.connexion()
        pathImages = bdd.selectAll()  
        self.displayer(pathImages)
          

    def filter(self):
        bdd = db.connexion()
        filter = bdd.filterList()
        return filter



    def getPictureByear(self,date):
        self.frameLabel.pack_forget()
        bdd = db.connexion()
        pathImages = bdd.getPictureByYear(date)      
        self.displayer(pathImages,0,date)



    def displayer(self,ListPicture,ofset = 0,filter = 0):
        j = 0
        y = 0
        wrapper = LabelFrame(self.root)
       
        self.frameLabel = wrapper
        bigCanva = Canvas(wrapper)
        frame = Frame(bigCanva) 
        previous = Button(bigCanva,text="previous",command= lambda o = ofset, f = filter: self.paginatePrev(o,f))
        previous.place(x=0,y=0) 
        next = Button(bigCanva,text="next",command= lambda o = ofset, f = filter: self.paginateNext(o,f))
        next.place(x=90,y=0)     
        frame.pack(fill = "both", expand = True)
        vbar = Scrollbar(wrapper,orient= VERTICAL,command=bigCanva.yview)
        bigCanva.configure( yscrollcommand=vbar.set)
        vbar.pack(side = RIGHT,fill= Y)
        bigCanva.create_window((0,0), window = frame)
        bigCanva.bind('<Configure>',lambda e: bigCanva.configure(scrollregion = bigCanva.bbox('all')))
        wrapper.pack(fill = "both", expand = True) 
        bigCanva.pack(fill = "both", expand= True)        

        for index,pathDate in enumerate(ListPicture):
            path = pathDate[0]                          
            j = j+1      
            globals()['canvas'+str(index)] = Canvas(frame,width= 300,height= 300)          
            globals()['canvas'+str(index)].grid(column=j,row=y)
            if j == 4:
                j = 0
                y = y + 1
            globals()['image'+str(index)] = ImageTk.PhotoImage(Image.open(path).resize((150, 150), Image.ANTIALIAS))       
            globals()['canvas'+str(index)].create_image(30,30,image = globals()['image'+str(index)],anchor = "nw", tags = "all")
           
            globals()['canvas'+str(index)].bind("<Button-1>",lambda a, i = index: Image.open(ListPicture[i][0]).show())    



    def all(self):
        self.frameLabel.pack_forget()
        bdd = db.connexion()
        pathImages = bdd.selectAll()  
        self.displayer(pathImages)

    def paginateNext(self,ofset,filter):
        bdd = db.connexion()
        pathImages = bdd.paginatePicture(str(ofset),filter)
        if len(pathImages) == 0:
            return FALSE
        self.frameLabel.pack_forget()    
        self.displayer(pathImages,(int(ofset) + int(self.limit)),filter )


    def paginatePrev(self,ofset,filter):
        if int(ofset) - int(self.limit) >= 0:
            self.frameLabel.pack_forget()
            bdd = db.connexion()
            pathImages = bdd.paginatePicture(int(ofset) - int(self.limit),filter)
            if len(pathImages) == 0:
                return FALSE
            self.displayer(pathImages,(int(ofset) - int(self.limit)),filter )
        else:
            return FALSE        

        



                    
       




        