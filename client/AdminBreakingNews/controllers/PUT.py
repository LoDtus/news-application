from datetime import datetime
from tkinter import messagebox
import requests
from requests.auth import HTTPBasicAuth

def UpdatePost(id, title, thumbnail, content, isShow):
    url = "http://localhost:8080/posts"
    username = "admin"
    password = "root"
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    data = {
        "id": id,
        "title": title,
        "thumbnail": thumbnail,
        "content": content,
        "creationDate": current_time,
        "show": isShow
    }

    try:
        response = requests.put(url, json=data, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200 or response.status_code == 201:
            messagebox.showinfo("Thành công!", "Bài viết được thay đổi thành công!")
        else:
            messagebox.showerror("Thất bại!", f"Lỗi: {response.status_code}\n{response.text}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []