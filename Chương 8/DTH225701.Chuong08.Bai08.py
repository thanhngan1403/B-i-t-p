from tkinter import *
import ctypes

def btnChuyen_click():
    degF = float(strInPut.get())
    degC = (degF-32) * 5/9
    result = f"{degC:.2f}"
    strOutPut.set(result)

def center_window(root, w, h):
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = screen_w//2 - w//2
    y = screen_h//2 - h//2
    root.geometry(f"{w}x{h}+{x}+{y}")

if __name__ == "__main__":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = Tk()
    root.title("Chuyển độ F")
    root.config(bg="yellow")
    center_window(root, 600, 250)

    strInPut = StringVar()
    strOutPut = StringVar()

    Label(root, text="Nhập độ F:", font=("",15), bg="yellow").grid(row=0, column=0, sticky="w")
    Entry(root, textvariable=strInPut, fg="red", justify="center").grid(row=0, column=1)

    Button(root,text="Chuyển", relief="solid",font=("", 13), fg="blue", command=btnChuyen_click).grid(row=1, column=1, pady= 20)

    Label(root, text="Độ C:", font=("", 15), bg="yellow").grid(row=2, column=0, sticky="w")
    Label(root, textvariable=strOutPut, text="",font=("", 15), bg="yellow").grid(row=2, column=1)
    root.mainloop()