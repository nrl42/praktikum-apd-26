import os

akun = {
    "nurul": {"password": "94", "role": "admin"},
}

data_hewan = {
    1: {
        "nama": "gajah",
        "tempat hidup": "hutan",
        "makanan": "buah",
        "golongan": "mamalia",
        "deskripsi": "mamalia terbesar yang memiliki belalai",
    },
    2: {
        "nama": "kelinci",
        "tempat hidup": "darat",
        "makanan": "rumput",
        "golongan": "mamalia",
        "deskripsi": "hewan bertelinga panjang",
    },
}

id_berikutnya = 3

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=====SISTEM PENDATAAN HEWAN=====")
    print("1. login")
    print("2. register")
    print("3. keluar")

    pilihan = input("pilih menu [1-3] : ").strip()

    if pilihan == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=====register=====")
        username = input("isi username anda : ").strip()

        if username == "":
            print("maaf username tidak boleh kosong")
        elif username in akun:
            print("username sudah digunakan")
        else:
            password = input("isi password anda : ").strip()

            if password == "":
                print("password tidak boleh kosong")
            else:
                akun[username] = {"password": password, "role": "pengguna"}
                print("selamat register berhasil")

        input("tekan enter untuk melanjutkan")

    elif pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=====LOGIN=====")

        username = input("masukkan username : ").strip()
        password = input("masukkan password : ").strip()

        data_user = akun.get(username)

        if data_user is None or data_user["password"] != password:
            print("username atau password salah")
            input("tekan enter untuk melanjutkan ")
        else:
            role = data_user["role"]
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
                        golongan = input("golongan hewan : ").strip()
                        deskripsi = input("deskripsi singkat : ").strip()

                        if (nama == "" or tempat == "" or makanan == ""
                                or golongan == "" or deskripsi == ""):
                            print("semua data wajib diisi")
                        else:
                            data_hewan[id_berikutnya] = {
                                "nama": nama,
                                "tempat hidup": tempat,
                                "makanan": makanan,
                                "golongan": golongan,
                                "deskripsi": deskripsi,
                            }
                            id_berikutnya += 1
                            print("data hewan berhasil ditambahkan")

                        input("tekan enter untuk melanjutkan")

                    elif menu == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=====DATA HEWAN=====")

                        if len(data_hewan) == 0:
                            print("belum ada data hewan")
                        else:
                            for id_hewan, hewan in data_hewan.items():
                                print("-" * 40)
                                print("id               :", id_hewan)
                                print("nama             :", hewan["nama"])
                                print("tempat hidup     :", hewan["tempat hidup"])
                                print("jenis makanan    :", hewan["makanan"])
                                print("golongan         :", hewan["golongan"])
                                print("deskripsi        :", hewan["deskripsi"])

                        input("\ntekan enter untuk melanjutkan")

                    elif menu == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=====UBAH DATA HEWAN=====")

                        if len(data_hewan) == 0:
                            print("belum ada data hewan")
                        else:
                            for id_hewan, hewan in data_hewan.items():
                                print(id_hewan, "-", hewan["nama"])

                            id_input = input("masukkan id hewan : ").strip()

                            if not id_input.isdecimal():
                                print("id harus berupa angka")
                            elif int(id_input) not in data_hewan:
                                print("id hewan tidak ditemukan")
                            else:
                                id_ubah = int(id_input)
                                hewan = data_hewan[id_ubah]

                                print("\n=====DATA HEWAN SEBELUM DIUBAH=====")
                                print("id           :", id_ubah)
                                print("nama         :", hewan["nama"])
                                print("tempat hidup :", hewan["tempat hidup"])
                                print("makanan      :", hewan["makanan"])
                                print("golongan     :", hewan["golongan"])
                                print("deskripsi    :", hewan["deskripsi"])

                                print("\nkosongkan jika tidak ingin mengubah data")
                                nama = input("nama baru          : ").strip()
                                tempat = input("tempat hidup baru  : ").strip()
                                makanan = input("jenis makanan baru : ").strip()
                                golongan = input("golongan baru      : ").strip()
                                deskripsi = input("deskripsi baru     : ").strip()

                                if nama != "":
                                    hewan["nama"] = nama
                                if tempat != "":
                                    hewan["tempat hidup"] = tempat
                                if makanan != "":
                                    hewan["makanan"] = makanan
                                if golongan != "":
                                    hewan["golongan"] = golongan
                                if deskripsi != "":
                                    hewan["deskripsi"] = deskripsi

                                print("\n=====DATA SETELAH DIUBAH=====")
                                print("id           :", id_ubah)
                                print("nama         :", hewan["nama"])
                                print("tempat hidup :", hewan["tempat hidup"])
                                print("makanan      :", hewan["makanan"])
                                print("golongan     :", hewan["golongan"])
                                print("deskripsi    :", hewan["deskripsi"])
                                print("data berhasil diubah")

                        input("\ntekan enter untuk melanjutkan")

                    elif menu == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("=====HAPUS DATA HEWAN=====")

                        if len(data_hewan) == 0:
                            print("belum ada data hewan")
                        else:
                            for id_hewan, hewan in data_hewan.items():
                                print(id_hewan, "-", hewan["nama"], "-", hewan["golongan"])

                            id_input = input("masukkan id hewan : ").strip()

                            if not id_input.isdecimal():
                                print("id harus berupa angka")
                            elif int(id_input) not in data_hewan:
                                print("id hewan tidak ditemukan")
                            else:
                                id_hapus = int(id_input)
                                konfirmasi = input(
                                    "hapus data " + data_hewan[id_hapus]["nama"] + "? (y/t) : "
                                ).strip().lower()

                                if konfirmasi == "y":
                                    data_hewan.pop(id_hapus)
                                    print("data berhasil dihapus")
                                else:
                                    print("penghapusan dibatalkan")

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
                            for id_hewan, hewan in data_hewan.items():
                                print("-" * 40)
                                print("id               :", id_hewan)
                                print("nama             :", hewan["nama"])
                                print("tempat hidup     :", hewan["tempat hidup"])
                                print("jenis makanan    :", hewan["makanan"])
                                print("golongan         :", hewan["golongan"])
                                print("deskripsi        :", hewan["deskripsi"])

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