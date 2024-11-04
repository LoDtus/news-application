from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
import requests
from controllers.GET import GetPost_byId
from controllers.POST import AddPost
from controllers.PUT import UpdatePost
from controllers.CheckImage import CheckImage

def PostCreation(master, managerFrame=None, PostManager=None, id=""):
    postCreation = Frame(master, width=980)
    postCreation.pack(side="left", fill="both", expand=True, padx=(30, 0))
    
    # Hàm thoát khỏi trang:
    def exitForm(frame, event=None):
        for widget in frame.winfo_children():
            widget.destroy()
        PostManager(frame)
    
    tempTitle = ""
    urlImg = ""
    tempContent = ""
    tempCheck = 0
    def refeshPage(idPost, tempTitle, tempCheck, urlImg, tempContent, isAdd):
        if (idPost != ""):  
            exitBtn = Button(postCreation, text="Thoát", bg="#ed5e68", fg="white", font=("Arial", 11, "bold"), width=10,
                command=lambda: exitForm(managerFrame))
            exitBtn.grid(row=0, column=0, sticky="w")
        
        title = Label(postCreation, text="Lưu bài viết", font=("Arial", 20, "bold"))
        title.grid(row=0, column=1, columnspan=2, pady=30)
        
        # Hàm tải và hiển thị Thumbnail:
        def loadThumbnail(url, frame):
            if (CheckImage(url)):
                tempTitle = entryTitle.get()
                tempCheck = check.get()
                tempContent = entryContent.get('1.0', 'end-1c')
                for widget in frame.winfo_children():
                    widget.destroy()
                urlImg = url
                refeshPage("", tempTitle, tempCheck, url, tempContent, True)
            else:
                messagebox.showerror("Thất bại!", f"Đường dẫn không hợp lệ!")

        # Hàm xác thực trước khi thêm hoặc sửa bài viết:
        def Validate(id, title, isShowStatus, url, content):
            if (title == ""):
                messagebox.showerror("Thất bại!", f"Hãy nhập tiêu đề bài viết!")
                return
            if (url == ""):
                messagebox.showerror("Thất bại!", f"Hãy tải lên ảnh nền cho bài viết!")
                return
            if (content == ""):
                messagebox.showerror("Thất bại!", f"Hãy nhập nội dung bài viết!")
                return
            show = {True: 1, False: 0} [isShowStatus == 1]
            if (isAdd):
                AddPost(title, urlImg, content, show)
            else:
                UpdatePost(id, title, urlImg, content, show)
        
        # Thêm tiêu đề:
        labelTitle = Label(postCreation, text="Tiêu đề bài viết:")
        labelTitle.grid(row=1, column=0, padx=5, sticky="e")
        
        entryTitle = Entry(postCreation, width=110)
        entryTitle.grid(row=1, column=1, sticky="w")
        if tempTitle:
            entryTitle.insert(0, tempTitle)
        
        # Bật/tắt trạng thái ẩn/hiện bài viết:
        check = IntVar()
        isShow = Checkbutton(postCreation, text="Hiện bài viết", variable=check, onvalue=1, offvalue=0)
        check.set(tempCheck)
        isShow.grid(row=1, column=2, sticky="w")
        
        # Thêm Thumbnail:   
        labelThumbnail = Label(postCreation, text="Đường dẫn cho ảnh nền:")
        labelThumbnail.grid(row=2, column=0, padx=5, sticky="e")

        thumbnailInp = Entry(postCreation, width=110)
        thumbnailInp.grid(row=2, column=1, sticky="w")
        
        thumbnailBtn = Button(postCreation, text="Tải", width=10, bg="#2196f3", fg="white", font=("Arial", 11, "bold"), cursor="hand2",
            command=lambda: loadThumbnail(thumbnailInp.get(), postCreation))
        thumbnailBtn.grid(row=2, column=2, sticky="w")
        
        # Tải Thumbnail:
        if (urlImg == ""):
            Label(postCreation, text="Chưa có ảnh nền", bd=1, relief=SOLID, pady=10, width=120, height=20).grid(row=3, column=0, columnspan=3, pady=10)
        else:
            response = requests.get(urlImg)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((530, 300), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            thumbnailLabel = Label(postCreation, image=img_tk)
            thumbnailLabel.image = img_tk
            thumbnailLabel.grid(row=3, column=0, columnspan=3, pady=10)
        
        # Nhập nội dung:    
        labelContent = Label(postCreation, text="Nội dung bài viết:")
        labelContent.grid(row=4, column=0, sticky="ne")
        
        entryContent = Text(postCreation, height=20, font=("Arial", 11, "normal"))
        entryContent.grid(row=4, column=1, sticky="w")
        if tempContent:
            entryContent.insert('1.0', tempContent)
        
        # Nút lưu:
        save = Button(postCreation, text="Lưu", bg="#3ab54a", fg="white", font=("Arial", 11, "bold"), width=10, cursor="hand2",
            command=lambda: Validate(idPost, entryTitle.get(), check.get(), urlImg, entryContent.get('1.0', 'end-1c')))
        save.grid(row=5, column=0, columnspan=3, pady=10)
    
    # Xác định trạng thái của Form là đang thêm bài viết mới hay sửa bài viết cũ:
    if (id == ""):
        refeshPage(id, tempTitle, tempCheck, urlImg, tempContent, True)
    else:
        result = GetPost_byId(id)
        if (result['show'] == 0):
            refeshPage(id, result['title'], False, result['thumbnail'], result['content'], False)
        else:
            refeshPage(id, result['title'], True, result['thumbnail'], result['content'], False)

    postCreation.update_idletasks()
    return postCreation