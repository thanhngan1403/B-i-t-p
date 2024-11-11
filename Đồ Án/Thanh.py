from tkinter import *
import googletrans
from PIL import Image,ImageTk 
from googletrans import Translator
from gtts import gTTS 
import os
root = Tk()
root.title("Google Translate")
root.geometry("400x500")
root.resizable(False, False)
# Sử dụng dấu gạch chéo hoặc dấu gạch chéo ngược kép trong đường dẫn tệp 
root.iconbitmap('D:\\logo.ico') 
# Mở và hiển thị hình ảnh nền 
load = Image.open('D:\\background.jpg') 
render = ImageTk.PhotoImage(load) 
img = Label(root, image=render) 
img.place(x=0, y=0)

def clear():
    text_input.delete(1.0, END)
    text_output.delete(1.0, END)

def trans():
    src_lang = 'vi'
    dest_lang = 'en'
    if x.get() == 0:
        src_lang = 'vi'
        dest_lang = 'en'
    elif x.get() == 1:
        src_lang = 'en'
        dest_lang = 'vi'
    else:
        pass
    in_put = text_input.get(1.0, END)
    tran_slate = Translator()
    out_put = tran_slate.translate(text=in_put, src=src_lang, dest=dest_lang)
    text_output.insert(END, out_put.text)


# Tạo hàm chuyển đổi văn bản thành giọng nói
def translate_text(text):
    if is_english(text):
        tts = gTTS(text=text, lang='en')
    else:
        tts = gTTS(text=text, lang='vi')
    tts.save("output.mp3")
    os.system("start output.mp3")

# Hàm kiểm tra xem văn bản có phải là tiếng Anh không
def is_english(text):
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

# Code tạo label Google Translate
lbl = Label(root, text="Google Translate",
 font=('arial', 20), fg="#ff6347",bd=0)
lbl.pack(pady=10)  

# Code tạo khung nhập & xuất 
frame_input = LabelFrame(root, text="Nhập ngôn ngữ ")
frame_input.place(x=40, y=70)
frame_output = LabelFrame(root, text="Xuất ngôn ngữ ")
frame_output.place(x=40, y=200)

# Code Tạo text input & text output
text_input = Text(frame_input, width=35, height=6,
                   font=('arial', 12))
text_input.pack()
text_output = Text(frame_output, width=35, height=6,
                    font=('arial', 12))
text_output.pack()

# Code tạo khung tùy chọn ngôn ngữ
frame_option = LabelFrame(root, text="Options")
frame_option.place(x=40, y=350)

# Code tạo ra nút chọn ngôn ngữ (radiobutton) 
lang = ["Vietnamese to English", "English to Vietnamese"]
x = IntVar()
x.set("0")

for index in range(len(lang)):
    radiobutton = Radiobutton(frame_option,text=lang[index],variable=x,
                              value=index,font=('arial', 12))
    radiobutton.pack(anchor=W)

#Code tạo các nút Button: Dịch, xóa, đọc ngôn ngữ 
btn_trans = Button(root, text="Translate", width=15, command=trans)
btn_trans.place(x=247, y=358)
btn_clear = Button(root, text="Clear", width=15, command=clear)
btn_clear.place(x=249, y=395)
read_input_button = Button(root, text="Đọc ngôn ngữ nhập",width=15,
                           command=lambda: translate_text(text_input.get("1.0", END)))
read_input_button.place(x=250,y=432)
read_output_button = Button(root, text="Đọc ngôn ngữ xuất",width=15, 
                            command=lambda: translate_text(text_output.get("1.0", END)))
read_output_button.place(x=60,y=432)

root.mainloop()