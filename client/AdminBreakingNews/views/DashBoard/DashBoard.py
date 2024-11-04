from tkinter import *
from controllers.GET import GetAllStatistic

def DashBoard(master):
    dashBoard = Frame(master, width=980)
    dashBoard.pack(side="left", fill="both", expand=True)
    dashBoard.update_idletasks()
    dashBoard.grid_columnconfigure(0, weight=1)
    
    # Lấy dữ liệu từ Statistic:
    result = GetAllStatistic()
    totalPost = result[0]['totalPost']
    totalPost_show = result[0]['totalPost_show']
    totalPost_hidden = result[0]['totalPost_hidden']
    totalPost_email = result[0]['totalEmail']
    
    # Hiển thị dữ liệu:
    Label(dashBoard, text="Dash Board", font=("Arial", 20, "bold"), width=60).grid(row=0, column=0, pady=20)
    
    Label(dashBoard, text="Thống kê bài viết", font=("Arial", 16, "bold"), justify="left",
        anchor="w").grid(row=1, column=0, sticky="ew", pady=(0, 5), padx=50)
    Label(dashBoard, text=f"Tổng số bài viết: {totalPost}", font=("Arial", 12), justify="left",
        anchor="w").grid(row=2, column=0, sticky="ew", padx=50)
    Label(dashBoard, text=f"Các bài viết được hiển thị: {totalPost_show}", font=("Arial", 12), justify="left",
        anchor="w").grid(row=3, column=0, sticky="ew", padx=50)
    Label(dashBoard, text=f"Các bài viết được ẩn: {totalPost_hidden}", font=("Arial", 12), justify="left",
        anchor="w").grid(row=4, column=0, sticky="ew", padx=50)
    
    Label(dashBoard, text="Thống kê người theo dõi", font=("Arial", 16, "bold"), justify="left",
        anchor="w").grid(row=7, column=0, sticky="ew", pady=(30, 5), padx=50)
    Label(dashBoard, text=f"Tổng số người dùng đang theo dõi: {totalPost_email}", font=("Arial", 12), justify="left",
        anchor="w").grid(row=8, column=0, sticky="ew", padx=50)