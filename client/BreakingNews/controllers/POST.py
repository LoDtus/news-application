from tkinter import messagebox
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

def AddEmail(email):
    url = "http://localhost:8081/emails"
    username = "user"
    password = ""
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