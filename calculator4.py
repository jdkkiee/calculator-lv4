def tampilkan_menu():
    print("\n=== KALKULATOR PYTHON ===")
    print("1. Hitung")
    print("2. Keluar")


def hitung():
    angka1 = float(input("Masukkan angka pertama: "))
    operator = input("Masukkan operator (+, -, *, /): ")
    angka2 = float(input("Masukkan angka kedua: "))

    if operator == "+":
        return angka1 + angka2

    elif operator == "-":
        return angka1 - angka2

    elif operator == "*":
        return angka1 * angka2

    elif operator == "/":
        if angka2 == 0:
            return "Tidak bisa membagi dengan 0."

        return angka1 / angka2

    else:
        return "Operator tidak valid."


def main():
    while True:
        tampilkan_menu()

        pilihan = input("Pilih menu: ")

        if pilihan == "1":

            try:
                hasil = hitung()
                print("Hasil:", hasil)

            except ValueError:
                print("Input angka harus berupa angka!")

        elif pilihan == "2":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


main()