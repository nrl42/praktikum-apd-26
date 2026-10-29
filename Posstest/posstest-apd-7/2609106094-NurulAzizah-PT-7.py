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
        "deskripsi": "mamalia terbesar yang memiliki belalai"
    },
    2: {
        "nama"          : "kelinci",
        "tempat hidup"  : "darat",
        "makanan"       : "rumput",
        "golongan"      : "mamalia",
        "deskripsi"     : "hewan bertelinga panjang"
    },
}

id_berikutnya = 3
user_aktif = None


class LoginGagalError(Exception):
    pass

class RegisterGagalError(Exception):
    pass

class HewanTidakDitemukanError(Exception):
    pass

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tampil_DataHewan(id_hewan, hewan):
    print("-" * 40)
    print("id             :", id_hewan)
    print("nama           :", hewan["nama"])
    print("tempat hidup   :", hewan["tempat hidup"])
    print("jenis makanan  :", hewan["makanan"])
    print("golongan       :", hewan["golongan"])
    print("deskripsi      :", hewan["deskripsi"])


def tampil_DaftarHewan(daftar_id, indeks):
    if indeks >= len(daftar_id):
        return
    id_hewan = daftar_id[indeks]
    tampil_DataHewan(id_hewan, data_hewan[id_hewan])
    tampil_DaftarHewan(daftar_id, indeks + 1)


def jeda():
    try:
        input("tekan enter untuk melanjutkan")
    except EOFError:
        pass


def Id_baru():
    global id_berikutnya
    id_baru = id_berikutnya
    id_berikutnya += 1
    return id_baru


def jumlah_hewan():
    jumlah = len(data_hewan)
    return jumlah


def validasi_login(username, password):
    data_user = akun.get(username)
    if data_user is None or data_user["password"] != password:
        raise LoginGagalError("username atau password salah")
    return data_user["role"]


def isi_input(label):
    teks = input(label).strip()
    if teks == "":
        print("input tidak boleh kosong")
        return isi_input(label)
    return teks


def Id_hewan(label):
    teks = input(label).strip()
    try:
        id_hewan = int(teks)
    except ValueError:
        print("input id harus berupa angka")
        return Id_hewan(label)
    if id_hewan not in data_hewan:
        raise HewanTidakDitemukanError("id hewan tidak ditemukan")
    return id_hewan


def register():
    bersihkan_layar()
    print("=====register=====")
    try:
        username = isi_input("isi username anda     :")
        if username in akun:
            raise RegisterGagalError("username sudah digunakan")
        password = isi_input("isi password anda :")
    except RegisterGagalError as e:
        print("gagal:", e)
    else:
        akun[username] = {"password": password, "role": "pengguna"}
        print("selamat register berhasil")
    finally:
        jeda()


def tambah_hewan():
    bersihkan_layar()
    print("=====tambah data hewan=====")
    nama = isi_input("nama hewan            :")
    tempat = isi_input("tempat hidup        :")
    makanan = isi_input("jenis makanan      :")
    golongan = isi_input("golongan hewan    :")
    deskripsi = isi_input("deskripsi singkat:")

    id_baru = Id_baru()
    data_hewan[id_baru] = {
        "nama": nama,
        "tempat hidup": tempat,
        "makanan": makanan,
        "golongan": golongan,
        "deskripsi": deskripsi
    }
    print("data hewan berhasil ditambahkan dengan id", id_baru)


def lihat_hewan():
    bersihkan_layar()
    print("=====Data Hewan====")
    if jumlah_hewan() == 0:
        print("belum ada data hewan")
    else:
        tampil_DaftarHewan(list(data_hewan.keys()), 0)
        print("-" * 40)


def ubah_hewan():
    bersihkan_layar()
    print("=====Ubah Data Hewan=====")
    if jumlah_hewan() == 0:
        print("belum ada data hewan")
        return

    for id_hewan, hewan in data_hewan.items():
        print(id_hewan, "-", hewan["nama"])

    try:
        id_ubah = Id_hewan("masukkan id hewan   :")
    except HewanTidakDitemukanError as e:
        print(e)
        return

    hewan = data_hewan[id_ubah]
    print("\n=====Data sebelum diubah=====")
    tampil_DataHewan(id_ubah, hewan)

    print("\nkosongkan jika tidak ingin mengubah data")
    for kolom, label in [
        ("nama", "nama baru"),
        ("tempat hidup", "tempat hidup baru"),
        ("makanan", "jenis makanan baru"),
        ("golongan", "golongan baru"),
        ("deskripsi", "deskripsi baru"),
    ]:
        isi_baru = input(label + ":").strip()
        if isi_baru != "":
            hewan[kolom] = isi_baru

    print("\n=====Data setelah diubah=====")
    tampil_DataHewan(id_ubah, hewan)
    print("data berhasil diubah")


def hapus_hewan():
    bersihkan_layar()
    print("=====Hapus data hewan=====")
    if jumlah_hewan() == 0:
        print("belum ada data hewan")
        return

    for id_hewan, hewan in data_hewan.items():
        print(id_hewan, "-", hewan["nama"], "-", hewan["golongan"])
    try:
        id_hapus = Id_hewan("masukkan id hewan  :")
    except HewanTidakDitemukanError as e:
        print(e)
        return

    konfirmasi = input(
        "hapus data " + data_hewan[id_hapus]["nama"] + "? (y/t) : "
    ).strip().lower()

    if konfirmasi == "y":
        del data_hewan[id_hapus]
        print("data berhasil dihapus")
    else:
        print("hapus data hewan batal")


def menu_admin():
    while True:
        bersihkan_layar()
        print("=====Menu admin(" + str(user_aktif) + ")====")
        print("1. create")
        print("2. read")
        print("3. update")
        print("4. delete")
        print("5. logout")

        try:
            menu = input("pilih menu    :").strip()
            if menu == "1":
                tambah_hewan()
            elif menu == "2":
                lihat_hewan()
            elif menu == "3":
                ubah_hewan()
            elif menu == "4":
                hapus_hewan()
            elif menu == "5":
                print("berhasil logout")
                jeda()
                break
            else:
                print("pilihan tidak tersedia")
        except (KeyboardInterrupt, EOFError):
            print("\ninput dibatalkan, kembali ke menu")
        jeda()


def menu_pengguna():
    while True:
        bersihkan_layar()
        print("=====menu pengguna (" + str(user_aktif) + ")=====")
        print("1. tampilkan data hewan")
        print("2. logout")

        try:
            menu = input("pilih menu : ").strip()

            if menu == "1":
                lihat_hewan()
            elif menu == "2":
                print("berhasil logout")
                jeda()
                break
            else:
                print("pilihan tidak tersedia")
        except (KeyboardInterrupt, EOFError):
            print("\ninput dibatalkan, kembali ke menu")
        jeda()


def login():
    global user_aktif
    bersihkan_layar()
    print("=====Login=====")

    username = input("masukkan username :").strip()
    password = input("masukkan password :").strip()

    try:
        role = validasi_login(username, password)
    except LoginGagalError as e:
        print(e)
        jeda()
        return

    user_aktif = username
    print("selamat login anda berhasil")
    jeda()

    try:
        if role == "admin":
            menu_admin()
        else:
            menu_pengguna()
    finally:
        user_aktif = None


def main():
    while True:
        bersihkan_layar()
        print("=====SISTEM PENDATAAN HEWAN=====")
        print("1. login")
        print("2. register")
        print("3. keluar")

        try:
            pilihan = input("pilih menu [1-3] : ").strip()
            if pilihan == "1":
                login()
            elif pilihan == "2":
                register()
            elif pilihan == "3":
                print("terima kasih")
                break
            else:
                raise ValueError("pilihan tidak tersedia")
        except ValueError as e:
            print(e)
            jeda()
        except (KeyboardInterrupt, EOFError):
            print("\nprogram dihentikan oleh pengguna")
            break


if __name__ == "__main__":
    main()