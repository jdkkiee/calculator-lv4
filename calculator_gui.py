import tkinter as tk




window = tk.Tk()

window.title("Kalkulator Python")
window.geometry("320x450")




display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right"
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    sticky="nsew"
)



def klik_angka(angka):
    display.insert(tk.END, angka)




def klik_operator(operator):
    display.insert(tk.END, operator)




def clear():
    display.delete(0, tk.END)

def hapus_satu():
    isi = display.get()

    display.delete(0, tk.END)

    display.insert(tk.END, isi[:-1])




def hitung():
    try:
        ekspresi = display.get()

        hasil = eval(ekspresi)

        display.delete(0, tk.END)
        display.insert(tk.END, hasil)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


# =========================
# TOMBOL
# =========================

tombol = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),

    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),

    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),

    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),

    ("C", 5, 0)
]


for teks, baris, kolom in tombol:

    if teks.isdigit() or teks == ".":

        command = lambda x=teks: klik_angka(x)

    elif teks in "+-*/":

        command = lambda x=teks: klik_operator(x)

    elif teks == "=":

        command = hitung

    elif teks == "C":

        command = clear

    button = tk.Button(
        window,
        text=teks,
        font=("Arial", 18),
        command=command
    )

    button.grid(
        row=baris,
        column=kolom,
        padx=5,
        pady=5,
        sticky="nsew"
    )


# =========================
# MEMBUAT GRID RESPONSIVE
# =========================

for i in range(4):
    window.columnconfigure(i, weight=1)

for i in range(6):
    window.rowconfigure(i, weight=1)




window.mainloop()