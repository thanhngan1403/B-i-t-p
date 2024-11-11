from tkinter import *
from gtts import gTTS
import os

# Tạo cửa sổ chính
root = Tk()
root.title("Google Translate")

# Tạo hàm chuyển đổi văn bản thành giọng nói
def translate_text():
    text = text_entry.get("1.0", END)
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

# Tạo nhãn và ô nhập văn bản
text_label = Label(root, text="Nhập văn bản:", font=('arial', 14))
text_label.pack(pady=10)

text_entry = Text(root, height=10, width=50, font=('arial', 12))
text_entry.pack(pady=10)

# Tạo nút chuyển đổi
translate_button = Button(root, text="Chuyển đổi", command=translate_text, font=('arial', 14))
translate_button.pack(pady=20)

# Chạy vòng lặp chính
root.mainloop()
