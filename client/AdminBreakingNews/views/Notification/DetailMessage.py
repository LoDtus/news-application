from tkinter import *
from controllers.GET import GetMessage_byId

def DetailMessage(master, refeshPage, id):
    title = Label(master, text="Message", font=("Arial", 20, "bold"))
    title.pack(side="top", pady=30)
    
    def exitForm(frame):
        for widget in frame.winfo_children():
            widget.destroy()
        refeshPage()
    
    result = GetMessage_byId(id)
    exitBtn = Button(master, text="Thoát", bg="#ed5e68", fg="white", width=10, font=("Arial", 11, "bold"),
        command=lambda: exitForm(master))
    exitBtn.pack(side="top", anchor="w", pady=(0, 10))
    
    Label(master, font=("Arial", 12, "normal"), text=result['subject'], wraplength=900, justify="left").pack(side="top", anchor="w")
    Label(master, font=("Arial", 12, "normal"), text="Hi there,").pack(side="top", anchor="w")
    Label(master, font=("Arial", 12, "normal"), text=result['content'], wraplength=900, justify="left").pack(side="top", anchor="w")
    Label(master, font=("Arial", 12, "normal"), text="Best regards,").pack(side="top", anchor="w")
    Label(master, font=("Arial", 12, "normal"), text=result['author'], wraplength=900, justify="left").pack(side="top", anchor="w")