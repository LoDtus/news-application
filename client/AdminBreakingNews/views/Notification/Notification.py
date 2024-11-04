from tkinter import *
from functools import partial
from controllers.GET import GetAllMessage
from controllers.DELETE import DeleteMessage_byId
from controllers.reFormat import reFormat
from views.Notification.AddMessage import AddMessage
from views.Notification.DetailMessage import DetailMessage

def Notification(master):
    notification = Frame(master, width=980)
    notification.pack(side="left", fill="both", expand=True, padx=(30, 0))
    
    # Chuyển tới Form soạn và gửi thông báo:
    def moveForm(frame, refeshPage):
        for widget in frame.winfo_children():
            widget.destroy()
        AddMessage(notification, refeshPage)
    
    # Chuyển sang trang chi tiết nội dung thông báo:
    def showMessage(id, frame, refeshPage, event=None):
        for widget in frame.winfo_children():
            widget.destroy()
        DetailMessage(notification, refeshPage, id)
    
    # Xóa thông báo:
    def removeItem(id, frame, event=None):
        DeleteMessage_byId(id)
        for widget in frame.winfo_children():
            widget.destroy()
        refeshPage()
    
    def refeshPage():
        result = GetAllMessage()
        title = Label(notification, text="Quản lý thông báo", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, columnspan=4, pady=30)
        
        # Button tạo thông báo mới:
        btnAdd = Button(notification, text="Gửi thông báo mới", bg="#3ab54a", fg="white", font=("Arial", 12, "bold"), command=lambda: moveForm(notification, refeshPage))
        btnAdd.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 10))
        
        # Header danh sách:
        Label(notification, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
            text="STT").grid(row=2, column=0, sticky="ew", padx=2, pady=2)
        Label(notification, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
            text="Tiêu đề").grid(row=2, column=1, sticky="ew", padx=2, pady=2)
        Label(notification, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
            text="Bài viết").grid(row=2, column=2, sticky="ew", padx=2, pady=2)
        Label(notification, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
            text="Ngày gửi").grid(row=2, column=3, sticky="ew", padx=2, pady=2)
        Label(notification, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
            text="Thực hiện").grid(row=2, column=4, sticky="ew", padx=2, pady=2, columnspan=2)

        # Danh sách các thông báo:
        for i in range(len(result)):
            postId = 0
            if (result[i]['post'] is None):
                postId = ""
            else:
                postId = str(result[i]['post']['id'])
            
            Label(notification, width=3, bd=1, relief="solid", font=("Arial", 11),
                text=str(i+1)).grid(row=(i+3), column=0, sticky="ew", padx=2, pady=2)
            Label(notification, width=40, bd=1, relief="solid", font=("Arial", 11),
                text=result[i]['subject']).grid(row=(i+3), column=1, sticky="ew", padx=2, pady=2)
            Label(notification, width=5, bd=1, relief="solid", font=("Arial", 11),
                text=postId).grid(row=(i+3), column=2, sticky="ew", padx=2, pady=2)
            Label(notification, width=10, bd=1, relief="solid", font=("Arial", 11),
                text=str(reFormat(result[i]['sendDate']))).grid(row=(i+3), column=3, sticky="ew", padx=2, pady=2)
            
            # Button tương tác với thông báo:
            btnShow = Label(notification, width=10, bd=1, relief="solid", font=("Arial", 11, "bold"), fg="white", bg="#0b57d4", cursor="hand2", text="Xem")
            btnShow.grid(row=(i+3), column=4, sticky="ew", padx=2, pady=2)
            btnDel = Label(notification, width=10, bd=1, relief="solid", font=("Arial", 11, "bold"), fg="white", bg="#ed5e68", cursor="hand2", text="Xoá")
            btnDel.grid(row=(i+3), column=5, sticky="ew", padx=2, pady=2)

            # Gán sự kiện cho Button:
            btnShow.bind("<Button-1>", partial(showMessage, result[i]['id'], notification, refeshPage))
            btnDel.bind("<Button-1>", partial(removeItem, result[i]['id'], notification))
    
    refeshPage()
    notification.update_idletasks()