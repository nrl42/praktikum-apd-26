import os

akun = [["nurul", "nurul123", "admin"]]

data_hewan = [
    [1, "kucing", "darat", "ikan", "mamalia",
    "kucing adalah hewan berkaki empat yang suka dipelihara"],
    [2, "buaya", "air", "daging", "reptil",
    "buaya adalah hewan yang hidup di air"],
]

id_berikutnya = 3

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=====SISTEM PENDATAAN HEWAN=====")
    print("1. login")
    print("2. register")
    print("3. keluar")

    pilihan = input("pilih menu : ").strip()

    if pilihan == "2":
        os.system("cls" if os.name == "nt" else "cle1.ar")
        print("=====register=====")
        username = input("isi username anda : ").strip()
        username_input = False

        if username == "":
            print("maaf username tidak boleh kosong")
        else:
            for user in akun:
                if user[0] == username:
                    username_input = True

            if username_input:
                print("username sudah digunakan")
            else:
                password = input("isi password anda : ").strip()

                if password == "":
                    print("password tidak boleh kosong")
                else:
                    akun.append([username, password, "pengguna"])
                    print("selamat register berhasil")

        input("tekan enter untuk melanjutkan")

    elif pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=====LOGIN=====")

        username = input("masukkan username : ").strip()
        password = input("masukkan password : ").strip()
        role = ""

        for user in akun:
            if user[0] == username and user[1] == password:
                role = user[2]

        if role == "":
            print("username atau password salah")
            input("tekan enter untuk melanjutkan ")
        else:
            print("selamat login berhasil")
            input("tekan enter untuk melanjutkan ")

            if role == "admin":
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=====menu admin=====")
                    print("1. create")
                    print("2. read")
                    print("3. update")
                    print("4. delete")
                    print("5. logout")

                    menu = input("pilih menu : ").strip()

                    if menu == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=====tambah data hewan=====")

                        nama = input("nama hewan : ").strip()
                        tempat = input("tempat hidup : ").strip()
                        makanan = input("jenis makanan : ").strip()
                        golongan = input("golongan hewan (mamalia/reptil/dll) : ").strip()
                        deskripsi = input("deskripsi singkat : ").strip()

                        if (nama == "" or tempat == "" or makanan == ""
                                or golongan == "" or deskripsi == ""):
                            print("semua data wajib diisi")
                        else:
                            data_baru = [
                                id_berikutnya, nama, tempat, makanan, golongan, deskripsi
                            ]
                            data_hewan.append(data_baru)
                            id_berikutnya += 1
                            print("data hewan berhasil ditambahkan")

                        input("tekan enter untuk melanjutkan")


                    elif menu == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=====DATA HEWAN=====")

                        if len(data_hewan) == 0:
                            print("belum ada data hewan")
                        else:
                            for hewan in data_hewan:
                                print("-" * 40)
                                print("id               :", hewan[0])
                                print("nama             :", hewan[1])
                                print("tempat hidup     :", hewan[2])
                                print("jenis makanan    :", hewan[3])
                                print("golongan         :", hewan[4])
                                print("deskripsi        :", hewan[5])

                        input("\ntekan enter untuk melanjutkan")

                    elif menu == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=====UBAH DATA HEWAN=====")

                        if len(data_hewan) == 0:
                            print("belum ada data hewan")
                        else:
                            for hewan in data_hewan:
                                print(hewan[0], "-", hewan[1])

                            id_input = input("masukkan id hewan : ").strip()

                            if not id_input.isdigit():
                                print("id harus berupa angka")
                            else:
                                ditemukan = False

                                for hewan in data_hewan:
                                    if hewan[0] == int(id_input):
                                        ditemukan = True

                                        print("\n=====DATA HEWAN SEBELUM DIUBAH=====")
                                        print("id           :", hewan[0])
                                        print("nama         :", hewan[1])
                                        print("tempat hidup :", hewan[2])
                                        print("makanan      :", hewan[3])
                                        print("golongan     :", hewan[4])
                                        print("deskripsi    :", hewan[5])

                                        print("\nkosongkan jika tidak ingin mengubah data")
                                        nama = input("nama baru          : ").strip()
                                        tempat = input("tempat hidup baru  : ").strip()
                                        makanan = input("jenis makanan baru : ").strip()
                                        golongan = input("golongan baru      : ").strip()
                                        deskripsi = input("deskripsi baru     : ").strip()

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

                                        print("\n=====DATA SETELAH DIUBAH=====")
                                        print("id           :", hewan[0])
                                        print("nama         :", hewan[1])
                                        print("tempat hidup :", hewan[2])
                                        print("makanan      :", hewan[3])
                                        print("golongan     :", hewan[4])
                                        print("deskripsi    :", hewan[5])
                                        print("data berhasil diubah")
                                        break

                                if not ditemukan:
                                    print("id hewan tidak ditemukan")

                        input("\ntekan enter untuk melanjutkan")

                    elif menu == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=====HAPUS DATA HEWAN=====")

                        if len(data_hewan) == 0:
                            print("belum ada data hewan")
                        else:
                            for hewan in data_hewan:
                                print(hewan[0], "-", hewan[1], "-", hewan[4])

                            id_input = input("masukkan id hewan : ").strip()

                            if not id_input.isdigit():
                                print("id harus berupa angka")
                            else:
                                ditemukan = False

                                for hewan in data_hewan:
                                    if hewan[0] == int(id_input):
                                        ditemukan = True
                                        konfirmasi = input(
                                            "hapus data " + hewan[1] + "? (y/t) : "
                                        ).strip().lower()

                                        if konfirmasi == "y":
                                            data_hewan.remove(hewan)
                                            print("data berhasil dihapus")
                                        else:
                                            print("penghapusan dibatalkan")
                                        break

                                if not ditemukan:
                                    print("id hewan tidak ditemukan")

                        input("\ntekan enter untuk melanjutkan")

                    elif menu == "5":
                        print("berhasil logout")
                        input("tekan enter untuk melanjutkan")
                        break

                    else:
                        print("pilihan tidak tersedia")
                        input("\ntekan enter untuk melanjutkan")

            elif role == "pengguna":
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=====menu pengguna=====")
                    print("1. tampilkan data hewan")
                    print("2. logout")

                    menu = input("pilih menu : ").strip()

                    if menu == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=====DATA HEWAN=====")

                        if len(data_hewan) == 0:
                            print("belum ada data hewan")
                        else:
                            for hewan in data_hewan:
                                print("-" * 40)
                                print("id               :", hewan[0])
                                print("nama             :", hewan[1])
                                print("tempat hidup     :", hewan[2])
                                print("jenis makanan    :", hewan[3])
                                print("golongan         :", hewan[4])
                                print("deskripsi        :", hewan[5])

                        input("\ntekan enter untuk melanjutkan")

                    elif menu == "2":
                        print("berhasil logout")
                        input("tekan enter untuk melanjutkan")
                        break

                    else:
                        print("pilihan tidak tersedia")
                        input("tekan enter untuk melanjutkan")

    elif pilihan == "3":
        print("terima kasih")
        break

    else:
        print("pilihan tidak tersedia")
        input("tekan enter untuk melanjutkan ")