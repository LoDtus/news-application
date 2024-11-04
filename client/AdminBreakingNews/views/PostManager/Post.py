from tkinter import *
from PIL import Image, ImageTk
from controllers.GET import GetPost_byId
import requests
from io import BytesIO

def Post(master, id, managerFrame, PostManager, PostCreation):
    post = Frame(master)
    post.pack(side="top", fill='x', expand=True)
    
    # Thoát khỏi Form, chuyển trang:
    def exitForm(frame, event=None):
        for widget in frame.winfo_children():
            widget.destroy()
        PostManager(frame)

    # Chuyển sang Form cập nhật bài viết:
    def updateForm(frame, id, event=None):
        for widget in frame.winfo_children():
            widget.destroy()
        PostCreation(frame, frame, PostManager, id)
    
    result = GetPost_byId(id)

    # Tiêu đề bài viết:
    btnFr = Frame(post)
    btnFr.pack(side="top", expand=True, fill="x", anchor="w", pady=30)
    exitBtn = Button(btnFr, text="Thoát", bg="#ed5e68", fg="white", font=("Arial", 11, "bold"), width=10,
        command=lambda: exitForm(managerFrame))
    exitBtn.pack(side="left")
    updateBtn= Button(btnFr, text="Sửa", bg="#3ab54a", fg="white", font=("Arial", 11, "bold"), width=10,
        command=lambda: updateForm(managerFrame, id))
    updateBtn.pack(side="left")
    
    titleText = result['title']
    title = Label(post, text=titleText, font=("Arial", 16), wraplength=900, justify="left")
    title.pack(side="top")
    
    # Ảnh nền bài viết:
    response = requests.get(result['thumbnail'])
    response.raise_for_status()
    image = Image.open(BytesIO(response.content))
    resized_image = image.resize((720, 405), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_image)
    
    label = Label(post, image=tk_image)
    label.image = tk_image
    label.pack(side="top", padx=15, pady=10)
    
    # Nội dung bài viết:
    contentText = result['content']
    content = Label(post, text=contentText, font=("Arial", 12), wraplength=700, justify="left")
    content.pack(side="bottom", pady=(0, 30))