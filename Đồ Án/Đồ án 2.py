import tkinter as tk
from tkinter import messagebox, ttk
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import playsound 
import os

# Khởi tạo trình dịch và các thiết bị nhận dạng giọng nói
translator = Translator()
recognizer = sr.Recognizer()

# Hàm dịch ngôn ngữ
def translate_text():
    input_text = text_input.get("1.0", tk.END)
    src_lang = src_lang_combobox.get()
    dest_lang = dest_lang_combobox.get()
    try:
        translated = translator.translate(input_text, src=src_lang, dest=dest_lang)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Hàm nhận diện giọng nói
def recognize_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            recognized_text = recognizer.recognize_google(audio)
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, recognized_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Hàm đọc văn bản
def speak_text():
    text = text_output.get("1.0", tk.END)
    tts = gTTS(text=text, lang=dest_lang_combobox.get())
    tts.save("output.mp3")
    playsound.playsound("output.mp3")
    os.remove("output.mp3")

# Tạo giao diện ứng dụng
root = tk.Tk()
root.title("Google Translate with Voice")

# Nhãn và vùng nhập liệu
tk.Label(root, text="Ngôn ngữ gốc:").grid(row=0, column=0)
src_lang_combobox = ttk.Combobox(root, values=list(translator.LANGUAGES.keys()))
src_lang_combobox.grid(row=0, column=1)
src_lang_combobox.set("en")

tk.Label(root, text="Ngôn ngữ đích:").grid(row=1, column=0)
dest_lang_combobox = ttk.Combobox(root, values=list(translator.LANGUAGES.keys()))
dest_lang_combobox.grid(row=1, column=1)
dest_lang_combobox.set("vi")

tk.Label(root, text="Văn bản nhập:").grid(row=2, column=0)
text_input = tk.Text(root, height=10, width=50)
text_input.grid(row=2, column=1, columnspan=2)

tk.Label(root, text="Văn bản dịch:").grid(row=3, column=0)
text_output = tk.Text(root, height=10, width=50)
text_output.grid(row=3, column=1, columnspan=2)

# Các nút chức năng
tk.Button(root, text="Dịch", command=translate_text).grid(row=4, column=0)
tk.Button(root, text="Nhận diện giọng nói", command=recognize_speech).grid(row=4, column=1)
tk.Button(root, text="Đọc văn bản", command=speak_text).grid(row=4, column=2)

# Khởi động ứng dụng
root.mainloop()

