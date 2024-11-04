from tkinter import *
from functools import partial
from controllers.GET import GetAllFollower
from controllers.POST import AddEmail
from controllers.DELETE import DeleteEmail_byId
from controllers.reFormat import reFormat

def Follower(master):
    follower = Frame(master, width=980)
    follower.pack(side="left", fill="both", expand=True, padx=(30, 0))
    
    # Thêm người theo dõi mới:
    def Add(email, frame, event=None):
        AddEmail(email)
        for widget in frame.winfo_children():
            widget.destroy()
        refeshPage()
    
    # Xóa người theo dõi khỏi hệ thống:
    def removeItem(id, frame, event=None):
        DeleteEmail_byId(id)
        for widget in frame.winfo_children():
            widget.destroy()
        refeshPage()
    
    def refeshPage():
        result = GetAllFollower()
        title = Label(follower, text="Quản lý người theo dõi", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, columnspan=4, pady=30)
        
        # Thêm Email mới:
        Label(follower, text="Thêm email mới:", justify="right").grid(row=1, column=0, sticky="e", pady=(0, 5))
        addEmail = Entry(follower, width=72)
        addEmail.grid(row=1, column=1, pady=(0, 5))
        addBtn = Button(follower, text="Thêm", width=20, bg="#24a0ed", fg="white", cursor="hand2",
            font=("Arial", 12, "bold"), command=lambda: Add(addEmail.get(), follower)).grid(row=1, column=2, sticky="w", pady=(0, 5))
        
        # Header danh sách:
        Label(follower, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
            text="STT").grid(row=2, column=0, sticky="ew", padx=2, pady=2)
        Label(follower, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
            text="Email").grid(row=2, column=1, sticky="ew", padx=2, pady=2)
        Label(follower, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
            text="Ngày tham gia").grid(row=2, column=2, sticky="ew", padx=2, pady=2)
        Label(follower, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
            text="Xóa").grid(row=2, column=3, sticky="ew", padx=2, pady=2)
        
        # Danh sách những người đang theo dõi:
        for i in range(len(result)):
            Label(follower, width=5, bd=1, relief="solid", font=(12), 
                text=str(i+1)).grid(row=(i+3), column=0, sticky="ew", padx=2, pady=2)
            Label(follower, width=50, bd=1, relief="solid", font=(12), 
                text=str(result[i]['email'])).grid(row=(i+3), column=1, sticky="ew", padx=2, pady=2)
            Label(follower, width=30, bd=1, relief="solid", font=(12), 
                text=str(reFormat(result[i]['joinDate']))).grid(row=(i+3), column=2, sticky="ew", padx=2, pady=2)
            delBtn = Label(follower, width=10, bd=1, relief="solid", font=("Arial", 12, "bold"), 
                text="Xóa", cursor="hand2", bg="#ed5e68", fg="white")
            delBtn.grid(row=(i+3), column=3, sticky="ew", padx=2, pady=2)
            delBtn.bind("<Button-1>", partial(removeItem, result[i]['id'], follower))
    
    refeshPage()
    follower.update_idletasks()