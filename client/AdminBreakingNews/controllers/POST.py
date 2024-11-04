from datetime import datetime
from tkinter import messagebox
import requests
from requests.auth import HTTPBasicAuth

def AddPost(title, thumbnail, content, isShow):
    url = "http://localhost:8080/posts"
    username = "admin"
    password = "root"
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    data = {
        "title": title,
        "thumbnail": thumbnail,
        "content": content,
        "creationDate": current_time,
        "show": isShow
    }

    try:
        response = requests.post(url, json=data, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200 or response.status_code == 201:
            messagebox.showinfo("Thành công!", "Bài viết được thêm mới thành công!")
        else:
            messagebox.showerror("Thất bại!", f"Lỗi: {response.status_code}\n{response.text}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def AddEmail(email):
    url = "http://localhost:8081/emails"
    username = "admin"
    password = "root"
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    data = {
        "email": email,
        "joinDate": current_time
    }

    try:
        response = requests.post(url, json=data, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200 or response.status_code == 201:
            messagebox.showinfo("Thành công!", "Email được thêm mới thành công!")
        else:
            messagebox.showerror("Thất bại!", f"Lỗi: {response.status_code}\n{response.text}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def SaveMessage(subject, content, author, listReceiver):
    url = "http://localhost:8082/messages"
    username = "admin"
    password = "root"
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    data = {
        "post": None,
        "sendDate": current_time,
        "subject": subject,
        "content": content,
        "author": author,
        "idReceiverJson": str(listReceiver),
        "idReceiver": listReceiver
    }

    try:
        response = requests.post(url, json=data, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200 or response.status_code == 201:
            messagebox.showinfo("Thành công!", "Thông báo được gửi thành công!")
        else:
            messagebox.showerror("Thất bại!", f"Lỗi: {response.status_code}\n{response.text}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []