import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import controllers.GET as GET

def Post(master, id):
    post = Frame(master)
    post.pack(side="top", fill='x', expand=True)
    
    result = GET.getPost_byId(id)
    # Title Post:
    titleText = result['title']
    title = Label(post, text=titleText, font=("Arial", 16), wraplength=900, justify="left")
    title.pack(side="top")
    
    # createdDate:
    creationDate = result['creationDate']
    
    # Thumbnail Post:
    response = requests.get(result['thumbnail'])
    response.raise_for_status()
    image = Image.open(BytesIO(response.content))
    resized_image = image.resize((720, 405), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_image)
    
    label = Label(post, image=tk_image)
    label.image = tk_image
    label.pack(side="top", padx=15, pady=10)
    
    # Content Post:
    contentText = result['content']
    content = Label(post, text=contentText, font=("Arial", 12), wraplength=700, justify="left")
    content.pack(side="bottom")
