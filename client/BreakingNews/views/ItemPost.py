import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
from controllers.ShortenText import ShortenText

def ItemPost(master, pageMaster, movePage, Post, id, title, thumbnail, createdAt):
    itemPost = Frame(master, cursor="hand2")
    itemPost.pack(side='left', anchor="w")

    def update_image(width):
        if width > 0:
            response = requests.get(thumbnail)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))

            # Tính toán kích thước cần cắt để đạt tỷ lệ 16:9
            ratio = 16 / 9
            img_width, img_height = image.size
            img_aspect_ratio = img_width / img_height

            if img_aspect_ratio > ratio:
                new_width = int(img_height * ratio)
                offset = (img_width - new_width) // 2
                crop_area = (offset, 0, offset + new_width, img_height)
            else:
                new_height = int(img_width / ratio)
                offset = (img_height - new_height) // 2
                crop_area = (0, offset, img_width, offset + new_height)

            image = image.crop(crop_area)

            # Thay đổi kích thước ảnh theo chiều rộng mới
            aspect_ratio = image.height / image.width
            new_size = (width, int(width * aspect_ratio))
            if new_size[1] > 0:  # Đảm bảo chiều cao không bằng 0
                image_resized = image.resize(new_size, Image.LANCZOS)
                tk_image = ImageTk.PhotoImage(image_resized)

                image_label.config(image=tk_image)
                image_label.image = tk_image
    
    image_label = Label(itemPost)
    image_label.pack(expand=True, fill='both')

    title = ShortenText(title, 16)
    title_label = Label(itemPost, text=title, wraplength=300, justify="left")
    title_label.pack()
    
    itemPost.update_image = update_image
    itemPost.after(10, lambda: itemPost.update_image(master.winfo_width() // 3))
    
    # Gán sự kiện Click vào itemPost:
    itemPost.bind("<Button-1>", lambda event: movePage(pageMaster, Post, id))
    image_label.bind("<Button-1>", lambda event: movePage(pageMaster, Post, id))
    title_label.bind("<Button-1>", lambda event: movePage(pageMaster, Post, id))
    
    return itemPost