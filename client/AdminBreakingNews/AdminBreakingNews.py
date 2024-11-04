import tkinter as tk
from tkinter import *
from views.Home import Home

def main():
    root = tk.Tk()
    root.title("Admin of Breaking News App")
    
    # Set kích thước mặc định của ứng dụng: -------------------------------------------------------
    screen_width  = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Tính vị trí hiển thị của ứng dụng
    position_x = int((screen_width - 1280) // 2)
    position_y = int((screen_height - 800) // 2)
    root.geometry(f"1280x720+{position_x}+{position_y}")

    # Hiển thị ứng dụng: -------------------------------------------------------------------------
    def handlePosition(event):
        posX = (event.width - app.winfo_reqwidth()) // 2
        canvas.coords(frame, posX, 0)

    canvas = Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)
    
    scrollbar = Scrollbar(root, orient="vertical", command = canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    app = Home(canvas)
    frame = canvas.create_window((0, 0), window=app, anchor='nw')
    canvas.bind("<Configure>", handlePosition)

    app.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    root.mainloop()

if __name__ == "__main__":
    main()