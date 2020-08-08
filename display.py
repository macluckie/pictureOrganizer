from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import os
from pathlib import Path



class Display:

    def __init__(self,root):
        self.root = root  

    def UploadAction(self):
        directorie = filedialog.askdirectory()
        contentFolder =  os.listdir(directorie)      
        wrapper = LabelFrame(self.root)
        bigCanva = Canvas(wrapper)
        frame = Frame(bigCanva,background="blue")       
        frame.pack(fill = BOTH,side = BOTTOM)
        vbar = Scrollbar(wrapper,orient= VERTICAL,command=bigCanva.yview)
        bigCanva.configure( yscrollcommand=vbar.set)
        bigCanva.bind('<Configure>',lambda e: bigCanva.configure(scrollregion = bigCanva.bbox('all')))
        vbar.pack(side = RIGHT,fill= Y)
        bigCanva.create_window((0,0), window = frame )
        wrapper.pack(fill = "both", expand = "yes", padx=50, pady=50)  
        self.handlerContent(contentFolder,frame,directorie)
        bigCanva.pack(fill = "both", expand=True,padx=300,pady=0)
        self.root.mainloop()

  
    def handlerContent(self,contentFolder,frame,directorie):
     
        progress = ttk.Progressbar(self.root, orient = HORIZONTAL,length = 100, mode = 'determinate')
        progress.pack(side = "top")

        i = 0
        extensions = ['jpeg','jpg','png']
        for imge in contentFolder:
            import time
        
            progress['value'] = 20
            self.root.update_idletasks() 
            progress['value'] = 40
            self.root.update_idletasks() 
        
            progress['value'] = 50
            self.root.update_idletasks() 
        
            progress['value'] = 60
            self.root.update_idletasks() 
        
            progress['value'] = 80
            self.root.update_idletasks() 
            
            if os.path.isdir(directorie + "/"+ imge):
                path = Path(directorie + "/"+ imge)
                # print(path.parent)
                # print(path)
                # print(os.listdir(str(path)))
                # print(str(path.parent))
                self.handlerContent(os.listdir(str(path)),frame, str(path))

                # print(os.listdir(directorie + "/"+ imge))
                # print(imge)
    
            for extension in extensions:               
                if imge.lower().endswith(extension):
                    i = i+1           
                    globals()['canvas'+str(i)] = Canvas(frame,width = 350,height = 350, background = "green")
                    globals()['canvas'+str(i)].pack()   
                    globals()['image'+str(i)] = ImageTk.PhotoImage(Image.open(directorie + "/"+ imge).resize((300, 300), Image.ANTIALIAS))       
                    globals()['canvas'+str(i)].create_image(20,20,image =  globals()['image'+str(i)],anchor = "nw") 
                    texteLabel = Label(globals()['canvas'+str(i)], text = directorie + "/"+ imge, image =   globals()['image'+str(i)], compound = 'top')
                    texteLabel.pack()
                    
        progress['value'] = 100
        self.root.update_idletasks() 





        