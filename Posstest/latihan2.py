import os

# =====================================================
# VARIABEL GLOBAL
# =====================================================
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

id_berikutnya = 3        # global: penghitung id hewan
MIN_USERNAME = 3         # global: batas minimal panjang username
MIN_PASSWORD = 4         # global: batas minimal panjang password


# =====================================================
# PROSEDUR (tidak mengembalikan nilai)
# =====================================================
def bersihkan_layar():
    """Prosedur tanpa parameter: membersihkan layar terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_detail(id_hewan, hewan):
    """Prosedur dengan parameter: menampilkan detail satu hewan."""
    print("-" * 40)
    print("id               :", id_hewan)
    print("nama             :", hewan["nama"])
    print("tempat hidup     :", hewan["tempat hidup"])
    print("jenis makanan    :", hewan["makanan"])
    print("golongan         :", hewan["golongan"])
    print("deskripsi        :", hewan["deskripsi"])


def tampilkan_semua_hewan():
    """Prosedur: menampilkan seluruh data hewan + statistik golongan (rekursif)."""
    bersihkan_layar()
    print("=====DATA HEWAN=====")

    if len(data_hewan) == 0:
        print("belum ada data hewan")
        return

    for id_hewan, hewan in data_hewan.items():
        tampilkan_detail(id_hewan, hewan)

    # statistik jumlah per golongan memakai fungsi rekursif
    daftar_id = list(data_hewan.keys())
    daftar_golongan = sorted({h["golongan"] for h in data_hewan.values()})
    print("-" * 40)
    print("jumlah hewan per golongan:")
    for golongan in daftar_golongan:
        print(" -", golongan, ":", hitung_per_golongan(daftar_id, golongan))


def register_akun():
    """Prosedur: registrasi akun baru dengan error handling."""
    bersihkan_layar()
    print("=====register=====")

    try:
        username = input("isi username anda : ").strip()
        if username == "":
            raise ValueError("username tidak boleh kosong")
        if len(username) < MIN_USERNAME:
            raise ValueError("username minimal " + str(MIN_USERNAME) + " karakter")
        if username in akun:
            raise ValueError("username sudah digunakan")

        password = validasi_password(input("isi password anda : ").strip())
    except ValueError as e:
        print("register gagal :", e)
    else:
        akun[username] = {"password": password, "role": "pengguna"}
        print("selamat register berhasil")
    finally:
        input("tekan enter untuk melanjutkan")


def menu_pengguna(username):
    """Prosedur dengan parameter: menu untuk role pengguna."""
    while True:
        bersihkan_layar()
        print("=====menu pengguna=====")
        print("halo,", username)
        print("1. tampilkan data hewan")
        print("2. logout")

        menu = input("pilih menu : ").strip()

        if menu == "1":
            tampilkan_semua_hewan()
            input("\ntekan enter untuk melanjutkan")
        elif menu == "2":
            print("berhasil logout")
            input("tekan enter untuk melanjutkan")
            break
        else:
            print("pilihan tidak tersedia")
            input("tekan enter untuk melanjutkan")


def menu_admin(username):
    """Prosedur dengan parameter: menu CRUD untuk role admin."""
    while True:
        bersihkan_layar()
        print("=====menu admin=====")
        print("halo,", username)
        print("1. create")
        print("2. read")
        print("3. update")
        print("4. delete")
        print("5. logout")

        menu = input("pilih menu : ").strip()

        # ---------- CREATE ----------
        if menu == "1":
            bersihkan_layar()
            print("=====tambah data hewan=====")

            try:
                nama = input("nama hewan : ").strip()
                tempat = input("tempat hidup : ").strip()
                makanan = input("jenis makanan : ").strip()
                golongan = input("golongan hewan : ").strip()
                deskripsi = input("deskripsi singkat : ").strip()

                if "" in (nama, tempat, makanan, golongan, deskripsi):
                    raise ValueError("semua data wajib diisi")
            except ValueError as e:
                print("gagal menambah data :", e)
            else:
                id_baru = buat_id_baru()
                data_hewan[id_baru] = {
                    "nama": nama,
                    "tempat hidup": tempat,
                    "makanan": makanan,
                    "golongan": golongan,
                    "deskripsi": deskripsi,
                }
                print("data hewan berhasil ditambahkan dengan id", id_baru)
            finally:
                input("tekan enter untuk melanjutkan")

        # ---------- READ ----------
        elif menu == "2":
            tampilkan_semua_hewan()
            input("\ntekan enter untuk melanjutkan")

        # ---------- UPDATE ----------
        elif menu == "3":
            bersihkan_layar()
            print("=====UBAH DATA HEWAN=====")

            if len(data_hewan) == 0:
                print("belum ada data hewan")
            else:
                for id_hewan, hewan in data_hewan.items():
                    print(id_hewan, "-", hewan["nama"])

                try:
                    id_ubah = ambil_id_valid(input("masukkan id hewan : ").strip())
                except ValueError as e:
                    print(e)
                except KeyError:
                    print("id hewan tidak ditemukan")
                else:
                    hewan = data_hewan[id_ubah]
                    print("\n=====DATA HEWAN SEBELUM DIUBAH=====")
                    tampilkan_detail(id_ubah, hewan)

                    print("\nkosongkan jika tidak ingin mengubah data")
                    baru = {
                        "nama": input("nama baru          : ").strip(),
                        "tempat hidup": input("tempat hidup baru  : ").strip(),
                        "makanan": input("jenis makanan baru : ").strip(),
                        "golongan": input("golongan baru      : ").strip(),
                        "deskripsi": input("deskripsi baru     : ").strip(),
                    }
                    for kunci, nilai in baru.items():
                        if nilai != "":
                            hewan[kunci] = nilai

                    print("\n=====DATA SETELAH DIUBAH=====")
                    tampilkan_detail(id_ubah, hewan)
                    print("data berhasil diubah")

            input("\ntekan enter untuk melanjutkan")

        # ---------- DELETE ----------
        elif menu == "4":
            bersihkan_layar()
            print("=====HAPUS DATA HEWAN=====")

            if len(data_hewan) == 0:
                print("belum ada data hewan")
            else:
                for id_hewan, hewan in data_hewan.items():
                    print(id_hewan, "-", hewan["nama"], "-", hewan["golongan"])

                try:
                    id_hapus = ambil_id_valid(input("masukkan id hewan : ").strip())
                except ValueError as e:
                    print(e)
                except KeyError:
                    print("id hewan tidak ditemukan")
                else:
                    konfirmasi = input(
                        "hapus data " + data_hewan[id_hapus]["nama"] + "? (y/t) : "
                    ).strip().lower()

                    if konfirmasi == "y":
                        data_hewan.pop(id_hapus)
                        print("data berhasil dihapus")
                    else:
                        print("penghapusan dibatalkan")

            input("\ntekan enter untuk melanjutkan")

        # ---------- LOGOUT ----------
        elif menu == "5":
            print("berhasil logout")
            input("tekan enter untuk melanjutkan")
            break

        else:
            print("pilihan tidak tersedia")
            input("\ntekan enter untuk melanjutkan")


# =====================================================
# FUNGSI TANPA PARAMETER (mengembalikan nilai)
# =====================================================
def menu_utama():
    """Fungsi tanpa parameter: tampilkan menu utama, kembalikan pilihan user."""
    bersihkan_layar()
    print("=====SISTEM PENDATAAN HEWAN=====")
    print("1. login")
    print("2. register")
    print("3. keluar")
    return input("pilih menu [1-3] : ").strip()


def buat_id_baru():
    """Fungsi tanpa parameter: menghasilkan id hewan baru (memakai variabel global)."""
    global id_berikutnya
    id_baru = id_berikutnya
    id_berikutnya += 1
    return id_baru


def login():
    """Fungsi tanpa parameter: proses login, kembalikan (username, role) atau None."""
    bersihkan_layar()
    print("=====LOGIN=====")

    try:
        username = input("masukkan username : ").strip()
        password = input("masukkan password : ").strip()

        if username not in akun:
            raise KeyError("username tidak ditemukan")
        if akun[username]["password"] != password:
            raise ValueError("password salah")
    except (KeyError, ValueError):
        # pesan dibuat sama agar tidak membocorkan username yang valid
        print("username atau password salah")
        hasil = None
    else:
        print("selamat login berhasil")
        hasil = (username, akun[username]["role"])
    finally:
        input("tekan enter untuk melanjutkan ")

    return hasil


# =====================================================
# FUNGSI DENGAN PARAMETER (mengembalikan nilai)
# =====================================================
def validasi_password(password):
    """Fungsi dengan parameter: validasi password, raise ValueError jika tidak valid."""
    if password == "":
        raise ValueError("password tidak boleh kosong")
    if len(password) < MIN_PASSWORD:
        raise ValueError("password minimal " + str(MIN_PASSWORD) + " karakter")
    return password


def ambil_id_valid(id_input):
    """Fungsi dengan parameter: ubah input id menjadi int yang valid."""
    if not id_input.isdecimal():
        raise ValueError("id harus berupa angka")

    id_hewan = int(id_input)
    if id_hewan not in data_hewan:
        raise KeyError(id_hewan)
    return id_hewan


def hitung_per_golongan(daftar_id, golongan):
    """Fungsi REKURSIF dengan parameter: hitung jumlah hewan pada suatu golongan."""
    # basis: daftar kosong -> 0
    if len(daftar_id) == 0:
        return 0

    # rekursi: cek elemen pertama + hitung sisanya
    cocok = 1 if data_hewan[daftar_id[0]]["golongan"] == golongan else 0
    return cocok + hitung_per_golongan(daftar_id[1:], golongan)


# =====================================================
# PROGRAM UTAMA
# =====================================================
while True:
    try:
        pilihan = menu_utama()

        if pilihan == "1":
            hasil = login()
            if hasil is not None:
                username, role = hasil
                if role == "admin":
                    menu_admin(username)
                elif role == "pengguna":
                    menu_pengguna(username)

        elif pilihan == "2":
            register_akun()

        elif pilihan == "3":
            print("terima kasih")
            break

        else:
            print("pilihan tidak tersedia")
            input("tekan enter untuk melanjutkan ")

    except (KeyboardInterrupt, EOFError):
        print("\nprogram dihentikan oleh pengguna")
        break