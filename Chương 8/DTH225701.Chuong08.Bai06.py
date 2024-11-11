from tkinter import *
import ctypes

def center_window(root, w, h):
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = screen_w//2 - w//2
    y = screen_h//2 - h//2
    root.geometry(f"{w}x{h}+{x}+{y}")


if __name__ == "__main__":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    root = Tk()
    root.title("Các loại type của button")
    center_window(root, 900, 400)

    Label(root, text="Borderwidth = 0").grid(row=0, column=0, pady=20)
    Button(root,text="raised", relief="raised", width= 10, bd=0).grid(row=0, column=1, padx=5)
    Button(root,text="sunken", relief="sunken", width= 10, bd=0).grid(row=0, column=2, padx=5)
    Button(root,text="flat", relief="flat", width= 10, bd=0).grid(row=0, column=3, padx=5)
    Button(root,text="ridge", relief="ridge", width= 10, bd=0).grid(row=0, column=4, padx=5)
    Button(root,text="groove", relief="groove", width= 10, bd=0).grid(row=0, column=5, padx=5)
    Button(root,text="solid", relief="solid", width= 10, bd=0).grid(row=0, column=6, padx=5)

    Label(root, text="Borderwidth = 1").grid(row=1, column=0, pady=20)
    Button(root,text="raised", relief="raised", width= 10, bd=1).grid(row=1, column=1, padx=5)
    Button(root,text="sunken", relief="sunken", width= 10, bd=1).grid(row=1, column=2, padx=5)
    Button(root,text="flat", relief="flat", width= 10, bd=1).grid(row=1, column=3, padx=5)
    Button(root,text="ridge", relief="ridge", width= 10, bd=1).grid(row=1, column=4, padx=5)
    Button(root,text="groove", relief="groove", width= 10, bd=1).grid(row=1, column=5, padx=5)
    Button(root,text="solid", relief="solid", width= 10, bd=1).grid(row=1, column=6, padx=5)


    Label(root, text="Borderwidth = 2").grid(row=2, column=0, pady=20)
    Button(root,text="raised", relief="raised", width= 10, bd=2).grid(row=2, column=1, padx=5)
    Button(root,text="sunken", relief="sunken", width= 10, bd=2).grid(row=2, column=2, padx=5)
    Button(root,text="flat", relief="flat", width= 10, bd=2).grid(row=2, column=3, padx=5)
    Button(root,text="ridge", relief="ridge", width= 10, bd=2).grid(row=2, column=4, padx=5)
    Button(root,text="groove", relief="groove", width= 10, bd=2).grid(row=2, column=5, padx=5)
    Button(root,text="solid", relief="solid", width= 10, bd=2).grid(row=2, column=6, padx=5)

    Label(root, text="Borderwidth = 3").grid(row=3, column=0, pady=20)
    Button(root,text="raised", relief="raised", width= 10, bd=3).grid(row=3, column=1, padx=5)
    Button(root,text="sunken", relief="sunken", width= 10, bd=3).grid(row=3, column=2, padx=5)
    Button(root,text="flat", relief="flat", width= 10, bd=3).grid(row=3, column=3, padx=5)
    Button(root,text="ridge", relief="ridge", width= 10, bd=3).grid(row=3, column=4, padx=5)
    Button(root,text="groove", relief="groove", width= 10, bd=3).grid(row=3, column=5, padx=5)
    Button(root,text="solid", relief="solid", width= 10, bd=3).grid(row=3, column=6, padx=5)

    Label(root, text="Borderwidth = 4").grid(row=4, column=0, pady=20)
    Button(root,text="raised", relief="raised", width= 10, bd=4).grid(row=4, column=1, padx=5)
    Button(root,text="sunken", relief="sunken", width= 10, bd=4).grid(row=4, column=2, padx=5)
    Button(root,text="flat", relief="flat", width= 10, bd=4).grid(row=4, column=3, padx=5)
    Button(root,text="ridge", relief="ridge", width= 10, bd=4).grid(row=4, column=4, padx=5)
    Button(root,text="groove", relief="groove", width= 10, bd=4).grid(row=4, column=5, padx=5)
    Button(root,text="solid", relief="solid", width= 10, bd=4).grid(row=4, column=6, padx=5)

    root.mainloop()