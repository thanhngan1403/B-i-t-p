import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Kết nối tới cơ sở dữ liệu SQLite
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        birth_year INTEGER,
        class TEXT
    )
''')
conn.commit()

# Hàm thêm sinh viên
def add_student():
    name = entry_name.get()
    birth_year = entry_birth_year.get()
    class_name = entry_class.get()
    cursor.execute('INSERT INTO students (name, birth_year, class) VALUES (?, ?, ?)', (name, birth_year, class_name))
    conn.commit()
    messagebox.showinfo("Thông báo", "Thêm sinh viên thành công")
    clear_entries()
    display_students()

# Hàm sửa sinh viên
def update_student():
    student_id = entry_id.get()
    name = entry_name.get()
    birth_year = entry_birth_year.get()
    class_name = entry_class.get()
    cursor.execute('UPDATE students SET name = ?, birth_year = ?, class = ? WHERE id = ?', (name, birth_year, class_name, student_id))
    conn.commit()
    messagebox.showinfo("Thông báo", "Cập nhật sinh viên thành công")
    clear_entries()
    display_students()

# Hàm xóa sinh viên
def delete_student():
    student_id = entry_id.get()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    messagebox.showinfo("Thông báo", "Xóa sinh viên thành công")
    clear_entries()
    display_students()

# Hàm tìm kiếm sinh viên
def search_student():
    student_id = entry_id.get()
    cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()
    if student:
        entry_name.delete(0, tk.END)
        entry_birth_year.delete(0, tk.END)
        entry_class.delete(0, tk.END)
        entry_name.insert(0, student[1])
        entry_birth_year.insert(0, student[2])
        entry_class.insert(0, student[3])
    else:
        messagebox.showerror("Lỗi", "Không tìm thấy sinh viên")

# Hàm xóa các trường nhập liệu
def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_birth_year.delete(0, tk.END)
    entry_class.delete(0, tk.END)

# Hàm hiển thị danh sách sinh viên
def display_students():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute('SELECT * FROM students')
    for row in cursor.fetchall():
        tree.insert('', tk.END, values=row)

# Tạo giao diện ứng dụng
root = tk.Tk()
root.title("Quản Lý Sinh Viên")

tk.Label(root, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Label(root, text="Tên").grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Năm Sinh").grid(row=2, column=0)
entry_birth_year = tk.Entry(root)
entry_birth_year.grid(row=2, column=1)

tk.Label(root, text="Lớp").grid(row=3, column=0)
entry_class = tk.Entry(root)
entry_class.grid(row=3, column=1)

tk.Button(root, text="Thêm", command=add_student).grid(row=4, column=0)
tk.Button(root, text="Sửa", command=update_student).grid(row=4, column=1)
tk.Button(root, text="Xóa", command=delete_student).grid(row=4, column=2)
tk.Button(root, text="Tìm", command=search_student).grid(row=4, column=3)

# Tạo bảng hiển thị danh sách sinh viên
columns = ('id', 'name', 'birth_year', 'class')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('id', text='ID')
tree.heading('name', text='Tên')
tree.heading('birth_year', text='Năm Sinh')
tree.heading('class', text='Lớp')
tree.grid(row=5, column=0, columnspan=4)

# Hiển thị danh sách sinh viên khi khởi động
display_students()

root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi tắt ứng dụng
conn.close()
