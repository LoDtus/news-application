from tkinter import *
from functools import partial
from controllers.GET import GetAllPost
from controllers.PUT import UpdatePost
from controllers.DELETE import DeletePost_byId
from controllers.reFormat import reFormat
from views.PostCreation.PostCreation import PostCreation
from views.PostManager.Post import Post

def PostManager(master):
    postManager = Frame(master)
    postManager.pack(fill="both", expand=True, padx=30)
    
    # Thay đổi trạng thái ẩn/hiện của bài viết:
    def toggleItem(id, title, thumbnail, content, show, frame, event=None):
        if (show == 1):
            UpdatePost(id, title, thumbnail, content, 0)
        else:
            UpdatePost(id, title, thumbnail, content, 1)
        for widget in frame.winfo_children():
            widget.destroy()
        refeshPage()
    
    # Xem bài viết:
    def viewItem(id, frame, event=None):
        for widget in frame.winfo_children():
            widget.destroy()
        Post(frame, id, master, PostManager, PostCreation)
    
    # Sửa bài viết:
    def updateItem(id, frame, event=None):
        for widget in frame.winfo_children():
            widget.destroy()
        PostCreation(frame, master, PostManager, id)
    
    # Xóa bài viết:
    def delItem(id, frame, event=None):
        DeletePost_byId(id)
        for widget in frame.winfo_children():
            widget.destroy()
        refeshPage()
    
    def refeshPage():
        Label(postManager, text="Quản lý các bài viết", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=5, pady=30)
        
        # Header của danh sách:
        Label(postManager, bd=1, bg="white", relief=SOLID, height=2, text="STT", width=10).grid(row=2, column=0, pady=(0, 2))
        Label(postManager, bd=1, bg="white", relief=SOLID, height=2, text="Tiêu đề", width=60).grid(row=2, column=1, pady=(0, 2))
        Label(postManager, bd=1, bg="white", relief=SOLID, height=2, text="Ngày đăng", width=20).grid(row=2, column=2, pady=(0, 2))
        Label(postManager, bd=1, bg="white", relief=SOLID, height=2, text="Trạng thái", width=10).grid(row=2, column=3, pady=(0, 2))
        Label(postManager, bd=1, bg="white", relief=SOLID, height=2, text="Thực hiện", width=26).grid(row=2, column=4, columnspan=4, pady=(0, 2))
        
        # Lấy dữ liệu toàn bộ bài viết:
        result = GetAllPost()
        for i in range(len(result)):
            Label(postManager, bd=1, relief=SOLID, width=10, height=2, 
                text=(i+1)).grid(row=(i+3), column=0, sticky="w", padx=(0, 2))
            Label(postManager, bd=1, relief=SOLID, width=60, height=2, 
                text=result[i]['title'], justify="left", wraplength=400).grid(row=(i+3), column=1, sticky="w", padx=(0, 2), pady=(0, 2))
            Label(postManager, bd=1, relief=SOLID, width=20, height=2, 
                text=str(reFormat(result[i]['creationDate']))).grid(row=(i+3), column=2, sticky="w", padx=(0, 2), pady=(0, 2))
            showTxt = {True: "Ẩn", False: "Hiện"} [result[i]['show'] == 0]
            Label(postManager, bd=1, relief=SOLID, width=10, height=2, 
                text=showTxt).grid(row=(i+3), column=3, sticky="w", padx=(0, 2), pady=(0, 2))
            
            # Các nút xử lý bài viết:
            showTxt = {True: "Hiện", False: "Ẩn"} [result[i]['show'] == 0]
            showBtn = Label(postManager, text=showTxt, width=6, height=2, bd=1, relief=SOLID, fg="white", bg="#e9a30a", cursor="hand2")
            showBtn.grid(row=(i+3), column=4, padx=(0, 2), pady=(0, 2))
            viewBtn = Label(postManager, text="Xem", width=6, height=2, bd=1, relief=SOLID, fg="white", bg="#3ab54a", cursor="hand2")
            viewBtn.grid(row=(i+3), column=5, padx=(0, 2), pady=(0, 2))
            updateBtn = Label(postManager, text="Sửa", width=6, height=2, bd=1, relief=SOLID, fg="white", bg="#24a0ed", cursor="hand2")
            updateBtn.grid(row=(i+3), column=6, padx=(0, 2), pady=(0, 2))
            delBtn = Label(postManager, text="Xóa", width=6, height=2, bd=1, relief=SOLID, fg="white", bg="#ed5e68", cursor="hand2")
            delBtn.grid(row=(i+3), column=7, padx=(0, 2), pady=(0, 2))
            
            # Gán sự kiện cho các nút:
            showBtn.bind("<Button-1>", partial(toggleItem, result[i]['id'], result[i]['title'], result[i]['thumbnail'], 
                result[i]['content'], result[i]['show'], postManager))
            viewBtn.bind("<Button-1>", partial(viewItem, result[i]['id'], postManager))
            updateBtn.bind("<Button-1>", partial(updateItem, result[i]['id'], postManager))
            delBtn.bind("<Button-1>", partial(delItem, result[i]['id'], postManager))
    
    refeshPage()
    return postManager