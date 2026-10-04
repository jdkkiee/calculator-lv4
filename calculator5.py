riwayat = []


def tampilkan_menu():
    print("\n=== KALKULATOR PYTHON ===")
    print("1. Hitung")
    print("2. Lihat riwayat")
    print("3. Keluar")


def hitung():
    angka1 = float(input("Masukkan angka pertama: "))
    operator = input("Masukkan operator (+, -, *, /): ")
    angka2 = float(input("Masukkan angka kedua: "))

    if operator == "+":
        hasil = angka1 + angka2

    elif operator == "-":
        hasil = angka1 - angka2

    elif operator == "*":
        hasil = angka1 * angka2

    elif operator == "/":
        if angka2 == 0:
            return None, "Tidak bisa membagi dengan 0."

        hasil = angka1 / angka2

    else:
        return None, "Operator tidak valid."

    return hasil, f"{angka1} {operator} {angka2} = {hasil}"


def tampilkan_riwayat():
    print("\n=== RIWAYAT PERHITUNGAN ===")

    if len(riwayat) == 0:
        print("Belum ada riwayat.")
    else:
        for item in riwayat:
            print(item)


def main():
    while True:
        tampilkan_menu()

        pilihan = input("Pilih menu: ")

        if pilihan == "1":

            try:
                hasil, teks_riwayat = hitung()

                if hasil is not None:
                    print("Hasil:", hasil)
                    riwayat.append(teks_riwayat)
                else:
                    print(teks_riwayat)

            except ValueError:
                print("Input angka harus berupa angka!")

        elif pilihan == "2":
            tampilkan_riwayat()

        elif pilihan == "3":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


main()