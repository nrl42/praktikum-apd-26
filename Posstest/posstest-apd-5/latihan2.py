
import os

akun = [["nurul", "nurul123", "Admin"]]

data_hewan = [
    [1, "Kucing", "Darat", "Ikan", "Mamalia",
    "Hewan berkaki empat yang sering dipelihara."],
    [2, "Buaya", "Air dan darat", "Daging", "Reptil",
    "Hewan reptil yang memiliki rahang kuat."]
]

id_berikutnya = 3

while True:
    os.system("cls")

    print("=== SISTEM PENDATAAN HEWAN ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan = input("Pilih menu: ").strip()

    if pilihan == "1":
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        login = False

        for data in akun:
            if data[0] == username and data[1] == password:
                login = True
                role = data[2]

        if login:
            print("Login berhasil!")
            input("Tekan Enter untuk lanjut...")

            while True:
                os.system("cls")

                print("=== MENU UTAMA ===")
                print("Login sebagai:", username, "-", role)
                print("1. Create / Tambah Hewan")
                print("2. Read / Lihat Data Hewan")
                print("3. Update / Ubah Data Hewan")
                print("4. Delete / Hapus Data Hewan")
                print("5. Logout")

                menu = input("Pilih menu: ").strip()
                
                if menu == "1":
                    if role != "Admin":
                        print("Hanya Admin yang boleh menambah data!")
                    else:
                        nama = input("Nama hewan: ").strip()
                        tempat = input("Tempat hidup: ").strip()
                        makanan = input("Jenis makanan: ").strip()
                        golongan = input(
                            "Golongan : "
                        ).strip().title()
                        deskripsi = input("Deskripsi hewan: ").strip()

                        if (nama == "" or tempat == "" or
                            makanan == "" or golongan == "" or
                            deskripsi == ""):
                            print("Semua data wajib diisi!")
                        else:
                            hewan_baru = [
                                id_berikutnya, nama, tempat,
                                makanan, golongan, deskripsi
                            ]

                            data_hewan.append(hewan_baru)
                            id_berikutnya += 1

                            print("Data hewan berhasil ditambahkan!")

                    input("Tekan Enter untuk lanjut...")

                # READ
                elif menu == "2":
                    print("\n=== DATA HEWAN ===")

                    if len(data_hewan) == 0:
                        print("Belum ada data hewan.")
                    else:
                        for hewan in data_hewan:
                            print("--------------------------")
                            print("ID            :", hewan[0])
                            print("Nama          :", hewan[1])
                            print("Tempat hidup  :", hewan[2])
                            print("Makanan       :", hewan[3])
                            print("Golongan      :", hewan[4])
                            print("Deskripsi     :", hewan[5])

                    input("Tekan Enter untuk lanjut...")

                elif menu == "3":
                    if role != "Admin":
                        print("Hanya Admin yang boleh mengubah data!")
                    else:
                        for hewan in data_hewan:
                            print(
                                "ID:", hewan[0],
                                "| Nama:", hewan[1]
                            )

                        id_input = input(
                            "Masukkan ID hewan yang ingin diubah: "
                        ).strip()

                        if not id_input.isdigit():
                            print("ID harus berupa angka!")
                        else:
                            id_cari = int(id_input)
                            ditemukan = False

                            for hewan in data_hewan:
                                if hewan[0] == id_cari:
                                    ditemukan = True

                                    print("Kosongkan input jika tidak diubah.")

                                    nama = input(
                                        "Nama baru (" + hewan[1] + "): "
                                    ).strip()
                                    tempat = input(
                                        "Tempat hidup baru (" + hewan[2] + "): "
                                    ).strip()
                                    makanan = input(
                                        "Makanan baru (" + hewan[3] + "): "
                                    ).strip()
                                    golongan = input(
                                        "Golongan baru (" + hewan[4] + "): "
                                    ).strip()
                                    deskripsi = input(
                                        "Deskripsi baru (" + hewan[5] + "): "
                                    ).strip()

                                    if nama != "":
                                        hewan[1] = nama
                                    if tempat != "":
                                        hewan[2] = tempat
                                    if makanan != "":
                                        hewan[3] = makanan
                                    if golongan != "":
                                        hewan[4] = golongan.title()
                                    if deskripsi != "":
                                        hewan[5] = deskripsi

                                    print("Data hewan berhasil diubah!")

                            if not ditemukan:
                                print("ID hewan tidak ditemukan!")

                    input("Tekan Enter untuk lanjut...")

                elif menu == "4":
                    if role != "Admin":
                        print("Hanya Admin yang boleh menghapus data!")
                    else:
                        for hewan in data_hewan:
                            print(
                                "ID:", hewan[0],
                                "| Nama:", hewan[1]
                            )

                        id_input = input(
                            "Masukkan ID hewan yang ingin dihapus: "
                        ).strip()

                        if not id_input.isdigit():
                            print("ID harus berupa angka!")
                        else:
                            id_cari = int(id_input)
                            ditemukan = False

                            for hewan in data_hewan:
                                if hewan[0] == id_cari:
                                    ditemukan = True
                                    data_hewan.remove(hewan)
                                    print("Data hewan berhasil dihapus!")
                                    break

                            if not ditemukan:
                                print("ID hewan tidak ditemukan!")

                    input("Tekan Enter untuk lanjut...")

                elif menu == "5":
                    break

                else:
                    print("Pilihan menu tidak valid!")
                    input("Tekan Enter untuk lanjut...")

        else:
            print("Username atau password salah!")
            input("Tekan Enter untuk lanjut...")

    elif pilihan == "2":
        os.system("cls")

        print("=== REGISTER AKUN ===")
        username_baru = input("Buat username: ").strip()
        password_baru = input("Buat password: ").strip()

        username_ada = False

        for data in akun:
            if data[0] == username_baru:
                username_ada = True

        if username_baru == "" or password_baru == "":
            print("Username dan password wajib diisi!")
        elif username_ada:
            print("Username sudah digunakan!")
        else:
            akun.append([username_baru, password_baru, "Pengguna"])
            print("Register berhasil!")
            print("Role akun: Pengguna Biasa")

        input("Tekan Enter untuk lanjut...")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan program!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")