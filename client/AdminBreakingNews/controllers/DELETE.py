import requests
from requests.auth import HTTPBasicAuth
from tkinter import messagebox

def DeletePost_byId(id):
    url = f"http://localhost:8080/posts/{id}"
    username = "admin"
    password = "root"
    try:
        response = requests.delete(url, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            messagebox.showinfo("Thành công!", "Bài viết được xóa thành công!")
        else:
            messagebox.showerror("Thất bại!", f"Lỗi: {response.status_code}\n{response.text}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def DeleteEmail_byId(id):
    url = f"http://localhost:8081/emails/{id}"
    username = "admin"
    password = "root"
    try:
        response = requests.delete(url, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            messagebox.showinfo("Thành công!", "Email được xóa thành công!")
        else:
            messagebox.showerror("Thất bại!", f"Lỗi: {response.status_code}\n{response.text}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def DeleteMessage_byId(id):
    url = f"http://localhost:8082/messages/{id}"
    username = "admin"
    password = "root"
    try:
        response = requests.delete(url, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            messagebox.showinfo("Thành công!", "Thông báo được xóa thành công!")
        else:
            messagebox.showerror("Thất bại!", f"Lỗi: {response.status_code}\n{response.text}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")