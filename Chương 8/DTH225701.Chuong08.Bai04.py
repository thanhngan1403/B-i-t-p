from tkinter import *
from tkinter import messagebox
import ctypes

ketQua = f_num = 0  #Khởi tạo các biến toàn cục
input = operator = ""#lưu trữ kết quả, số đầu tiên, đầu vào và toán tử.
#để xử lý khi nhấn các nút số
def btn_num_click(items):
    global input #Sử dụng biến toàn cục input
    input += str(items)#Thêm ký tự của nút được nhấn vào biểu thức hiện tại
    strInput.set(input)#Cập nhật biểu thức trên hộp nhập liệu.

def add_click():
    global input, operator, f_num
    if input != '':#Nếu input không rỗng, chuyển đổi input thành số thực và lưu vào f_num
        f_num = float(input)
        operator = "+"#Đặt operator là "+" và xóa input
        input = ''
        strInput.set(input)
            
def minus_click():
    global input, operator, f_num
    if input != '':
        f_num = float(input)
        operator = "-"
        input = ''
        strInput.set(input)

def multi_click():
    global input, operator, f_num
    if input != '':
        f_num = float(input)
        operator = "*"
        input = ''
        strInput.set(input)

def div_click():
    global input, operator, f_num
    if input != '':
        f_num = float(input)
        operator = "/"
        input = ''
        strInput.set(input)

def equal_click():
    global f_num, input, operator, ketQua
    if f_num != 0 and  input != "":#Nếu f_num khác 0 và input không rỗng, chuyển đổi input thành số thực và lưu vào s_num
        s_num = float(input)
        if operator == "+":
            ketQua = f_num + s_num
        elif operator == "-":
            ketQua = f_num - s_num
        elif operator == "*":
            ketQua = f_num * s_num
        else:
            ketQua = f_num / s_num
         #Cập nhật input và strInput với kết quả   
        input = str(ketQua)
        operator = ""
        strInput.set(str(ketQua))                 
                               
def clear_click():
    global ketQua, f_num, operator, input
    ketQua = 0
    f_num = operator = input = ''
    strInput.set(input)

def center_window(root, w, h):
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
   #Tính toán tọa độ x và y để đặt cửa sổ vào giữa màn hình
    x = screen_w//2 - w//2
    y = screen_h//2 - h//2
    root.geometry(f"{w}x{h}+{x}+{y}")#đặt kích thước và vị trí của cửa sổ.
    
if __name__ == "__main__":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = Tk()
    root.title("Calculator")
    center_window(root, 400, 450)
    root.resizable(False,False)
    root.config(bg = "light blue")    

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    strInput = StringVar()# liên kết với hộp nhập liệu
    Entry(root, textvariable=strInput, width=350, justify="right").grid(row=0, columnspan=3, pady=10)

    Button(root, command=lambda:btn_num_click(1) , text="1", relief="raised", font=("", 13), fg="red", anchor="center",width=10).grid(row=1, column=0)
    Button(root, command=lambda:btn_num_click(2) , text="2", relief="raised", font=("", 13), fg="red", anchor="center",width=10).grid(row=1, column=1)
    Button(root, command=lambda:btn_num_click(3) , text="3", relief="raised", font=("", 13), fg="red", anchor="center",width=10).grid(row=1, column=2)
    Button(root, command=lambda:btn_num_click(4) , text="4", relief="raised", font=("", 13), fg="red", anchor="center",width=10).grid(row=2, column=0)
    Button(root, command=lambda:btn_num_click(5) , text="5", relief="raised", font=("", 13), fg="red", anchor="center",width=10).grid(row=2, column=1)
    Button(root, command=lambda:btn_num_click(6) , text="6", relief="raised", font=("", 13), fg="red", anchor="center",width=10).grid(row=2, column=2)
    Button(root, command=lambda:btn_num_click(7) , text="7", relief="raised", font=("", 13), fg="red", anchor="center",width=10).grid(row=3, column=0)
    Button(root, command=lambda:btn_num_click(8) , text="8", relief="raised", font=("", 13), fg="red", anchor="center",width=10).grid(row=3, column=1)
    Button(root, command=lambda:btn_num_click(9) , text="9", relief="raised", font=("", 13), fg="red", anchor="center",width=10).grid(row=3, column=2)
    
    phepToanFrame = Frame(root)
    Button(phepToanFrame, command=lambda:btn_num_click(".") , text=".", relief="raised", font=("", 13), fg="red", anchor="center",width=6).grid(row=0, column=0)
    Button(phepToanFrame, command=lambda:btn_num_click(0) , text="0", relief="raised", font=("", 13), fg="red", anchor="center",width=6).grid(row=0, column=1)
    Button(phepToanFrame, command=lambda:btn_num_click("-"), text="-", relief="raised", font=("", 13), fg="red", anchor="center",width=6).grid(row=0, column=2)
    Button(phepToanFrame, command=equal_click, text="=", relief="raised", font=("", 13), fg="red", anchor="center",width=6).grid(row=0, column=3)

    Button(phepToanFrame, command=add_click, text="+", relief="raised", font=("", 13), fg="red", anchor="center",width=6).grid(row=1, column=0)
    Button(phepToanFrame, command=minus_click, text="-", relief="raised", font=("", 13), fg="red", anchor="center",width=6).grid(row=1, column=1)
    Button(phepToanFrame, command=multi_click, text="*", relief="raised", font=("", 13), fg="red", anchor="center",width=6).grid(row=1, column=2)
    Button(phepToanFrame, command=div_click, text="/", relief="raised", font=("", 13), fg="red", anchor="center",width=6).grid(row=1, column=3)
    phepToanFrame.grid(row=4,columnspan=3)

    Button(phepToanFrame, command=clear_click, text="Clear", relief="raised", font=("", 13), fg="red", anchor="center",width=6).grid(row=5, columnspan=4, sticky="we")
    
    root.mainloop()