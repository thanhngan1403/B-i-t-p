from tkinter import *
import ctypes

def btnTinhBMI_click():
    chieuCao = float(strChieuCao.get())
    canNang = float(strCanNang.get())
    bmi = canNang/(chieuCao**2)
    tinhTrang = nguyCo = ""
    if bmi < 18.5:
        tinhTrang = "Gầy"
        nguyCo = "Thấp"
    elif bmi <= 24.9:
        tinhTrang = "Binh thường"
        nguyCo = "Trung bình"
    elif bmi <= 29.9:
        tinhTrang = "Hơi béo"
        nguyCo = "Cao"
    elif bmi <= 34.9:
        tinhTrang = "Béo phì cấp độ 1"
        nguyCo = "Cao"
    elif bmi <= 39.9:
        tinhTrang = "Béo phì cấp độ 2"
        nguyCo = "Rất cao"
    else:
        tinhTrang = "Béo phì cấp độ 3"
        nguyCo = "Nguy hiểm"

    strBMI.set(f"{bmi:.2f}")
    strTinhTrang.set(tinhTrang)
    strNguyCo.set(nguyCo)


def center_window(root, w, h):
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = screen_w//2 - w//2
    y = screen_h//2 - h//2
    root.geometry(f"{w}x{h}+{x}+{y}")

if __name__ == "__main__":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = Tk()
    root.config(bg="yellow")
    root.title("Tính BMI")
    center_window(root, 500, 500)

    strChieuCao = StringVar()
    strCanNang = StringVar()
    strBMI = StringVar()
    strNguyCo = StringVar()
    strTinhTrang = StringVar()

    Label(root, text="Nhập chiều cao:", bg="yellow", font=("", 15)).grid(row=0, column=0, pady=10, sticky="w")
    Entry(root, textvariable=strChieuCao, fg="red", justify="center").grid(row=0, column=1, pady=10)

    Label(root, text="Nhập cân nặng:", bg="yellow", font=("", 15)).grid(row=1, column=0, pady=10, sticky="w")
    Entry(root, textvariable=strCanNang, fg="red", justify="center").grid(row=1, column=1, pady=10)

    Button(root, text="Tính BMI", justify="center", relief="solid",fg="white", bg="blue", width=15, command=btnTinhBMI_click).grid(row=2, column=1, pady=10, sticky="w")

    Label(root, text="BMI của bạn:", bg="yellow", font=("", 15)).grid(row=3, column=0, pady=10, sticky="w")
    Entry(root, textvariable=strBMI, fg="red", justify="center").grid(row=3, column=1, pady=10)

    Label(root, text="Tình trạng:", bg="yellow", font=("", 15)).grid(row=4, column=0, pady=10, sticky="w")
    Entry(root, textvariable=strTinhTrang, fg="red", justify="center").grid(row=4, column=1, pady=10)

    Label(root, text="Nguy cơ:", bg="yellow", font=("", 15)).grid(row=5, column=0, pady=10, sticky="w")
    Entry(root, textvariable=strNguyCo, fg="red", justify="center").grid(row=5, column=1, pady=10)

    Button(root, text="Thoát", justify="center", relief="solid",fg="white", bg="blue", width=15, command=exit).grid(row=6, column=1, pady=10, sticky="w")

    root.mainloop()