from tkinter import *

def SideBar(master, frameMaster, movePage, DashBoard, PostCreation, PostManager, Notification, Follower):
    sideBar = Frame(master, width=200)
    sideBar.pack(side="left", fill="y")
    
    title = Label(sideBar, text="Admin", font=("Arial", 16, "bold"))
    title.grid(row=0, column=0, pady=(10, 5), padx=10, sticky="ew")
    
    # DashBoard:
    dashboard = Button(sideBar, width=30, height=2, text="Dashboard", command=lambda: movePage(frameMaster, DashBoard))
    dashboard.grid(row=1, column=0, pady=3, padx=3, sticky="ew")
    
    # Add Post:
    postCreation = Button(sideBar, width=30, height=2, text="Create Post", command=lambda: movePage(frameMaster, PostCreation))
    postCreation.grid(row=2, column=0, pady=3, padx=3, sticky="ew")

    # Post Manager:
    postManager = Button(sideBar, width=30, height=2, text="Manage Post", command=lambda: movePage(frameMaster, PostManager))
    postManager.grid(row=3, column=0, pady=3, padx=3, sticky="ew")

    # Notification Manager
    notification = Button(sideBar, width=30, height=2, text="Notification", command=lambda: movePage(frameMaster, Notification))
    notification.grid(row=4, column=0, pady=3, padx=3, sticky="ew")
    
    # Follower Manager:
    follower = Button(sideBar, width=30, height=2, text="Follower", command=lambda: movePage(frameMaster, Follower))
    follower.grid(row=5, column=0, pady=3, padx=3, sticky="ew")

    for i in range(4):
        sideBar.grid_rowconfigure(i, weight=0)
    
    return sideBar