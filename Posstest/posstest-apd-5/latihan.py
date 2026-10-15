
import os

# Data akun: [username, password, role]
akun = [
    ["admin", "admin123", "Admin"]
]

# Data hewan: [ID, nama, tempat hidup, makanan, golongan, deskripsi]
data_hewan = [
    [1, "Kucing", "Darat", "Daging/Ikan", "Mamalia",
    "Kucing adalah hewan peliharaan berkaki empat."],
    [2, "Buaya", "Air dan Darat", "Daging", "Reptil",
    "Buaya adalah reptil yang hidup di sekitar perairan."]
]

id_berikutnya = 3

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("===== SISTEM PENDATAAN HEWAN =====")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan = input("Pilih menu: ").strip()

    # REGISTERos.
    if pilihan == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("===== REGISTER =====")

        username = input("Buat username: ").strip()
        username_ada = False

        if username == "":
            print("Username tidak boleh kosong!")
        else:
            for user in akun:
                if user[0] == username:
                    username_ada = True

            if username_ada:
                print("Username sudah digunakan!")
            else:
                password = input("Buat password: ").strip()

                if password == "":
                    print("Password tidak boleh kosong!")
                else:
                    akun.append([username, password, "Pengguna"])
                    print("Register berhasil!")

        input("Tekan Enter untuk melanjutkan...")

    # LOGIN
    elif pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("===== LOGIN =====")

        username = input("Username: ").strip()
        password = input("Password: ").strip()
        role = ""

        for user in akun:
            if user[0] == username and user[1] == password:
                role = user[2]     

        if role == "":
            print("Username atau password salah!")
            input("Tekan Enter untuk melanjutkan...")
        else:
            print("Login berhasil!")

            # MENU ADMIN
            if role == "Admin":
                while True:
                    print("\n===== MENU ADMIN =====")
                    print("1. Create / Tambah Data")
                    print("2. Read / Tampilkan Data")
                    print("3. Update / Ubah Data")
                    print("4. Delete / Hapus Data")
                    print("5. Logout")

                    menu = input("Pilih menu: ").strip()

                    # CREATE
                    if menu == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("===== TAMBAH DATA HEWAN =====")

                        nama = input("Nama hewan: ").strip()
                        tempat = input("Tempat hidup: ").strip()
                        makanan = input("Jenis makanan: ").strip()
                        golongan = input("Golongan hewan: ").strip()
                        deskripsi = input("Deskripsi singkat: ").strip()

                        if (nama == "" or tempat == "" or makanan == ""
                                or golongan == "" or deskripsi == ""):
                            print("Semua data wajib diisi!")
                        else:
                            data_baru = [
                                id_berikutnya, nama, tempat,
                                makanan, golongan, deskripsi
                            ]
                            data_hewan.append(data_baru)
                            id_berikutnya += 1
                            print("Data hewan berhasil ditambahkan!")

                    # READ
                    elif menu == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("===== DATA HEWAN =====")

                        if len(data_hewan) == 0:
                            print("Belum ada data hewan.")

                        for hewan in data_hewan:
                            print("-" * 40)
                            print("ID            :", hewan[0])
                            print("Nama          :", hewan[1])
                            print("Tempat hidup  :", hewan[2])
                            print("Jenis makanan :", hewan[3])
                            print("Golongan      :", hewan[4])
                            print("Deskripsi     :", hewan[5])

                    # UPDATE
                    elif menu == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("===== UBAH DATA HEWAN =====")

                        for hewan in data_hewan:
                            print(hewan[0], "-", hewan[1])

                        id_input = input("Masukkan ID hewan: ").strip()

                        if not id_input.isdigit():
                            print("ID harus berupa angka!")
                        else:
                            ditemukan = False

                            for hewan in data_hewan:
                                if hewan[0] == int(id_input):
                                    ditemukan = True
                                    print("Kosongkan jika tidak ingin mengubah data.")

                                    nama = input("Nama baru: ").strip()
                                    tempat = input("Tempat hidup baru: ").strip()
                                    makanan = input("Jenis makanan baru: ").strip()
                                    golongan = input("Golongan baru: ").strip()
                                    deskripsi = input("Deskripsi baru: ").strip()

                                    if nama != "":
                                        hewan[1] = nama
                                    if tempat != "":
                                        hewan[2] = tempat
                                    if makanan != "":
                                        hewan[3] = makanan
                                    if golongan != "":
                                        hewan[4] = golongan
                                    if deskripsi != "":
                                        hewan[5] = deskripsi

                                    print("Data berhasil diubah!")
                                    break

                            if not ditemukan:
                                print("ID hewan tidak ditemukan!")

                    # DELETE
                    elif menu == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("===== HAPUS DATA HEWAN =====")

                        for hewan in data_hewan:
                            print(hewan[0], "-", hewan[1])

                        id_input = input("Masukkan ID hewan: ").strip()

                        if not id_input.isdigit():
                            print("ID harus berupa angka!")
                        else:
                            ditemukan = False

                            for hewan in data_hewan:
                                if hewan[0] == int(id_input):
                                    ditemukan = True
                                    konfirmasi = input(
                                        "Hapus data ini? (y/t): "
                                    ).strip().lower()

                                    if konfirmasi == "y":
                                        data_hewan.remove(hewan)
                                        print("Data berhasil dihapus!")
                                    else:
                                        print("Penghapusan dibatalkan.")
                                    break

                            if not ditemukan:
                                print("ID hewan tidak ditemukan!")

                    elif menu == "5":
                        print("Berhasil logout!")
                        break

                    else:
                        print("Pilihan tidak tersedia!")

                    input("\nTekan Enter untuk melanjutkan...")

            # MENU PENGGUNA BIASA
            elif role == "Pengguna":
                while True:
                    print("\n===== MENU PENGGUNA =====")
                    print("1. Tampilkan Data Hewan")
                    print("2. Logout")

                    menu = input("Pilih menu: ").strip()

                    if menu == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("===== DATA HEWAN =====")

                        if len(data_hewan) == 0:
                            print("Belum ada data hewan.")

                        for hewan in data_hewan:
                            print("-" * 40)
                            print("ID            :", hewan[0])
                            print("Nama          :", hewan[1])
                            print("Tempat hidup  :", hewan[2])
                            print("Jenis makanan :", hewan[3])
                            print("Golongan      :", hewan[4])
                            print("Deskripsi     :", hewan[5])

                    elif menu == "2":
                        print("Berhasil logout!")
                        break

                    else:
                        print("Pilihan tidak tersedia!")

                    input("\nTekan Enter untuk melanjutkan...")

    elif pilihan == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak tersedia!")
        input("Tekan Enter untuk melanjutkan...")
