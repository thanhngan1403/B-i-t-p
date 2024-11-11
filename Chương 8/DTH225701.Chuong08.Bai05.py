from tkinter import *
from tkinter import messagebox
# Tạo cửa sổ chính
root = Tk()
root.title("Enter New Password")

stringA = StringVar()
stringB = StringVar()
stringC = StringVar()

frameButton = Frame(root)

Label(root, text="Old Password:").grid(row=0, column=1)
Entry(root, width=15, textvariable=stringA, show='*').grid(row=0, column=2)  # Che mật khẩu bằng ký tự '*'

Label(root, text="New Password:").grid(row=1, column=1)
Entry(root, width=15, textvariable=stringB, show='*').grid(row=1, column=2)  # Che mật khẩu bằng ký tự '*'

Label(root, text="Enter New Password Again:").grid(row=2, column=1)
Entry(root, width=15, textvariable=stringC, show='*').grid(row=2, column=2)  # Che mật khẩu bằng ký tự '*'

# Thêm nút OK
def ok_action():
    old_password = stringA.get() #Lấy giá trị của mật khẩu cũ
    new_password = stringB.get() #Lấy giá trị mật khẩu mới 
    confirm_password = stringC.get()# Lấy giá trị mật khẩu xác nhận
    if new_password == confirm_password: # kt mật khẩu mới và mật khẩu xác nhận khớp ko
        messagebox.showinfo("Success", "Password changed successfully!")
    else:
        messagebox.showerror("Error", "New passwords do not match!")

Button(root, text="OK", command=ok_action).grid(row=3, column=1)


# Thêm nút Cancel
def cancel_action(): # xóa nội dung của các trường nhập liệu.
    stringA.set("")
    stringB.set("")
    stringC.set("")

Button(root, text="Cancel", command=cancel_action).grid(row=3, column=2)

# Chạy vòng lặp chính
root.mainloop()

