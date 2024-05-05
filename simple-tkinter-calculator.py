##simple-tkinter-calculator
##X-Projetion
##Lutfifakee
import tkinter as tk

def tambah():
    result = int(float(entry_num1.get()) + float(entry_num2.get()))
    label_result.config(text="Hasil: " + str(result))
    
def kurang():
    result = int(float(entry_num1.get()) - float(entry_num2.get()))
    label_result.config(text="Hasil: " + str(result))

def kali():
    result = int(float(entry_num1.get()) * float(entry_num2.get()))
    label_result.config(text="Hasil: " + str(result))

def bagi():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 == 0:
        label_result.config(text="Tidak dapat melakukan pembagian dengan nol.")
    else:
        result = num1 / num2
        if result.is_integer():  # Memeriksa apakah hasil pembagian adalah bilangan bulat
            result = int(result)
        label_result.config(text="Hasil: " + str(result))

# Membuat jendela
root = tk.Tk()
root.title("Calculator | X-Projetion")

# Menambahkan padding
root.geometry("300x200")

# Label dan input untuk bilangan pertama
label_num1 = tk.Label(root, text="Bilangan Pertama:")
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

# Label dan input untuk bilangan kedua
label_num2 = tk.Label(root, text="Bilangan Kedua:")
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Menambahkan padding pada tombol
padx_btn = 10
pady_btn = 5

# Tombol untuk operasi penambahan
button_add = tk.Button(root, text="Tambah", command=tambah)
button_add.grid(row=2, column=0, padx=padx_btn, pady=pady_btn)

# Tombol untuk operasi pengurangan
button_subtract = tk.Button(root, text="Kurang", command=kurang)
button_subtract.grid(row=2, column=1, padx=padx_btn, pady=pady_btn)

# Tombol untuk operasi perkalian
button_multiply = tk.Button(root, text="Kali", command=kali)
button_multiply.grid(row=3, column=0, padx=padx_btn, pady=pady_btn)

# Tombol untuk operasi pembagian
button_divide = tk.Button(root, text="Bagi", command=bagi)
button_divide.grid(row=3, column=1, padx=padx_btn, pady=pady_btn)

# Label untuk menampilkan hasil
label_result = tk.Label(root, text="Hasil: ")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Menjalankan loop Tkinter
root.mainloop()
