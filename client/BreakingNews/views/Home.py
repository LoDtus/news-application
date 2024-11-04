from tkinter import *
from views.Header import *
from views.Content import *
from views.Footer import *
from views.Post import *

def Home(master):
    home = Frame(master)
    home.pack(side="top", fill='both', expand=True)
        
    bodyFrame = Frame(home)
    def movePage(master, frame, id):
        for widget in master.winfo_children():
            widget.destroy()
        if (frame.__name__ == "Post"):  
            frame(bodyFrame, id)
        else:
            frame(bodyFrame, movePage, Post)

    Header(home, bodyFrame, movePage, Content)
    bodyFrame.pack()
    Content(bodyFrame, movePage, Post)
    Footer(home)

    return home