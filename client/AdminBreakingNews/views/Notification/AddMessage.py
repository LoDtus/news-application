from tkinter import *
from tkinter import messagebox
from controllers.GET import GetAllFollower
from controllers.POST import SaveMessage
from controllers.reFormat import reFormat

def AddMessage(master, refeshPage):
    # Gửi thông báo:
    def SendMessage(subject, content, author, listStatus):
        count = 0
        listReceiver = []
        for i in range(len(listStatus)):
            if (listStatus[i].get() == 0):
                count = count + 1
            else:
                id = listStatus[i].get() - 1
                listReceiver.append(result[id]['id'])
            if (count == len(listStatus)):
                messagebox.showerror("Thất bại!", "Bạn phải chọn tối thiểu 1 người nhận!")
                return 0
        if (content == ""):
            messagebox.showerror("Thất bại!", "Hãy nhập nội dung thông báo!")
            return
        if (subject == ""):
            subject = "No Subject"
        if (author == ""):
            author = "Breaking News"
        SaveMessage(subject, content, author, listReceiver)
    
    # Thoát khỏi Form hiện tại, trở về trang trước:
    def ExitForm(frame):
        for widget in frame.winfo_children():
            widget.destroy()
        refeshPage()
    
    title = Label(master, text="Soạn thông báo", font=("Arial", 20, "bold"))
    title.grid(row=0, column=0, columnspan=4, pady=30)
    
    # Soạn thông báo:
    exitBtn = Button(master, text="Thoát", bg="#ed5e68", fg="white", font=("Arial", 11, "bold"), cursor="hand2",
        width=10, command=lambda: ExitForm(master))
    exitBtn.grid(row=1, column=0, sticky="e", padx=(0, 2))
    sendBtn = Button(master, text="Gửi", bg="#0b57d4", fg="white", width=10, font=("Arial", 11, "bold"), cursor="hand2",
        command=lambda: SendMessage(titleInp.get('1.0', 'end-1c'), contentInp.get('1.0', 'end-1c'), authorInp.get('1.0', 'end-1c'), status))
    sendBtn.grid(row=1, column=1, sticky="w")
    
    # Nhập tiêu đề:
    Label(master, text="Tiêu đề:", justify="right").grid(row=2, column=0, sticky="e", pady=(10, 0))
    titleInp = Text(master, width=100, height=1, font=("Arial", 11, "normal"))
    titleInp.grid(row=2, column=1, columnspan=3, sticky="w")
    
    # Nhập nội dung thông báo:
    Label(master, text="Nội dung email:", justify="right").grid(row=3, column=0, sticky="e")
    Label(master, text="Hi there,", justify="left").grid(row=3, column=1, sticky="w")
    contentInp = Text(master, width=100, height=10, font=("Arial", 11, "normal"))
    contentInp.grid(row=4, column=1, columnspan=3, sticky="w")
    Label(master, text="Best regards,", justify="left").grid(row=5, column=1, sticky="w")
    
    # Nhập người gửi:
    Label(master, text="Tác giả:", justify="right").grid(row=6, column=0, sticky="e")
    authorInp = Text(master, width=100, height=1, font=("Arial", 11, "normal"))
    authorInp.grid(row=6, column=1, columnspan=3, sticky="w")
    
    # Người nhận:
    Label(master, text="Người nhận", justify="left", font=("Arial", 14, "bold")).grid(row=8, column=0, pady=(30, 10))
    result = GetAllFollower() 
    
    # Header danh sách người nhận:
    Label(master, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
        text="STT").grid(row=9, column=0, sticky="ew", padx=2, pady=2)
    Label(master, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
        text="Email").grid(row=9, column=1, sticky="ew", padx=2, pady=2)
    Label(master, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
        text="Ngày tham gia").grid(row=9, column=2, sticky="ew", padx=2, pady=2)
    Label(master, width=10, bd=1, relief="solid", bg="white", font=("Arial", 12, "bold"), 
        text="Chọn").grid(row=9, column=3, sticky="ew", padx=2, pady=2)

    # Danh sách người nhận:
    status = []
    for i in range(len(result)):
        temp = IntVar()
        status.append(temp)
        
        Label(master, width=5, bd=1, relief="solid", font=(12), 
            text=str(i+1)).grid(row=(i+10), column=0, sticky="ew", padx=2, pady=2)
        Label(master, width=50, bd=1, relief="solid", font=(12), 
            text=str(result[i]['email'])).grid(row=(i+10), column=1, sticky="ew", padx=2, pady=2)
        Label(master, width=30, bd=1, relief="solid", font=(12), 
            text=str(reFormat(result[i]['joinDate']))).grid(row=(i+10), column=2, sticky="ew", padx=2, pady=2)
        chooseBtn = Checkbutton(master, variable=status[i], onvalue=i+1, offvalue=0)
        chooseBtn.grid(row=(i+10), column=3, padx=2, pady=2)