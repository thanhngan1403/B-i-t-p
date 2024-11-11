from tkinter import *

# Tạo cửa sổ chính
root = Tk()
root.title("Example Interface")
root.geometry("400x300")

# Tạo khung nhập văn bản
frame_input = LabelFrame(root, text="Input Section", padx=100, pady=100)
frame_input.pack(padx=100, pady=100)

# Tạo ô nhập văn bản đầu tiên
text_input1 = Text(frame_input, width=30, height=2)
text_input1.pack(pady=5)

# Tạo ô nhập văn bản thứ hai
text_input2 = Text(frame_input, width=30, height=2)
text_input2.pack(pady=5)

# Tạo nút bấm
submit_button = Button(frame_input, text="Submit")
submit_button.pack(pady=10)


# Chạy vòng lặp chính
root.mainloop()

# Tạo label input
frame_input = LabelFrame(root, text="Nhập ngôn ngữ ")
frame_input.place(x=40, y=70)

# Tạo text input
text_input = Text(frame_input, width=35, height=6, font=('arial', 12))
text_input.pack()

# Tạo label output
frame_output = LabelFrame(root, text="Xuất ngôn ngữ ")
frame_output.place(x=40, y=200)

# Tạo text output
text_output = Text(frame_output, width=35, height=6, font=('arial', 12))
text_output.pack()

frame_option = LabelFrame(root, text="Options")
frame_option.place(x=40, y=350)

lang = ["Vietnamese to English", "English to Vietnamese"]
x = IntVar()
x.set("0")

for index in range(len(lang)):
    radiobutton = Radiobutton(frame_option, text=lang[index], variable=x, value=index, font=('arial', 12))
    radiobutton.pack(anchor=W)

btn_trans = Button(root, text="Translate", width=15, command=trans)
btn_trans.place(x=247, y=358)
btn_clear = Button(root, text="Clear", width=15, command=clear)
btn_clear.place(x=249, y=395)

# Tạo nút đọc ngôn ngữ cho input
read_input_button = Button(root, text="Đọc ngôn ngữ nhập",width=15, command=lambda: translate_text(text_input.get("1.0", END)))
read_input_button.place(x=250,y=432)

# Tạo nút đọc ngôn ngữ cho output
read_output_button = Button(root, text="Đọc ngôn ngữ xuất",width=15, command=lambda: translate_text(text_output.get("1.0", END)))
read_output_button.place(x=60,y=432)

