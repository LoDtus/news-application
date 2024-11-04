from tkinter import *

from views.SideBar import * 
from views.DashBoard.DashBoard import *
from views.PostCreation.PostCreation import * 
from views.PostManager.PostManager import * 
from views.Notification.Notification import * 
from views.Follower.Follower import *

def Home(master):
    home = Frame(master)
    home.pack(side="top", fill='both', expand=True)

    managerFrame = Frame(home, width=980)
    def movePage(container, frame):
        for widget in container.winfo_children():
            widget.destroy()
        frame(container)

    SideBar(home, managerFrame, movePage, DashBoard, PostCreation, PostManager, Notification, Follower)
    managerFrame.pack(side="right", fill="both", expand=True)
    DashBoard(managerFrame)

    return home