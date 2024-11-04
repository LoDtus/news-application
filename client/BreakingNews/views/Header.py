from tkinter import *
from PIL import Image, ImageTk
import os

def Header(master, pageMaster, movePage, Content):
    header = Frame(master, height=100)
    header.pack(side="top", fill='x')
    
    # Logo: ------------------------------------
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_folder = str(current_dir + r"\assets")
    
    image = Image.open(f"{assets_folder}\\logo.png")
    resized_image = image.resize((60, 60), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_image)
    
    label = Label(header, image=tk_image, cursor="hand2")
    label.image = tk_image
    label.pack(side="left", padx=15, pady=10)
    
    # Tên ứng dụng: ----------------------------
    title = Label(header, text="Breaking News App", font=("Arial", 16), cursor="hand2")
    title.pack(side="left")
    
    # Handle sự kiện click: --------------------
    label.bind("<Button-1>", lambda event: movePage(pageMaster, Content, -1))
    title.bind("<Button-1>", lambda event: movePage(pageMaster, Content, -1))
    
    return header