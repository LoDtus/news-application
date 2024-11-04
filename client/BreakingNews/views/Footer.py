from tkinter import *
from controllers.POST import AddEmail

def Footer(master):
    footer = Frame(master, height=100)
    footer.pack(side="top", fill='x', pady=(20, 80))
    
    # Left Side:
    leftSide = Frame(footer, height=100)
    leftSide.pack(side="left", fill="both")
    
    appTitle = Label(leftSide, text="Project: Breaking News", font=("Arial", 16, "bold"), anchor="w")
    appTitle.pack(side="top", fill="both")
    
    appDesc = Label(leftSide, text="Breaking News là một ứng dụng blog cá nhân đơn giản, cho phép người dùng dễ dàng đăng tải và chia sẻ những bài viết mới nhất về các chủ đề đa dạng như công nghệ, kinh tế, văn hóa và đời sống.",
        anchor="w", wraplength=400, justify="left", font=("Arial", 11))
    appDesc.pack(side="top", fill="both")
    
    # Right Side:
    rightSide = Frame(footer, height=100)
    rightSide.pack(side="right", fill="both")

    newsletterTitle = Label(rightSide, text="Nhận thêm các thông báo về bài viết mới của chúng tôi tại đây!",
        anchor="e", font=("Arial", 11))
    newsletterTitle.pack(side="top", fill="both")

    newsletterFrame = Frame(rightSide)
    newsletterFrame.pack(side="top", fill="both", anchor="e", pady=(5, 30))
    
    newsletterBtn = Button(newsletterFrame, text="Đăng ký", bg="#24a0ed", fg="white", cursor="hand2",
        width=10, font=("Arial", 11, "bold"), command=lambda: AddEmail(newsletterInp.get()))
    newsletterBtn.pack(side="right")
    
    newsletterInp = Entry(newsletterFrame, width=40)
    newsletterInp.pack(side="right", fill="both", padx=(0, 5))
    
    designFrame = Frame(rightSide)
    designFrame.pack(side="top", anchor="e")

    Label(designFrame, text="Nguyễn Trung Long, Nguyễn Hữu Hưng", font=("Arial", 11, "bold")).pack(side="right")
    Label(designFrame, text="Thiết kế bởi", font=("Arial", 11)).pack(side="right")
    
    return footer