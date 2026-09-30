nama= "nurul"
NIM= 94
print("selamat datang di penyewaan playstation")
biodata= str(input("masukkan nama anda:")).lower()
nim = int(input("masukkan nim anda: "))

if biodata != nama or nim != NIM :
    print("maaf login gagal ")
    exit()
else :
    print("login anda berhasil")

PS4 = 10000
PS4_pro= 15000
PS5 = 20000
print("Pilihan Penyewaan playstation")
print ("pengguna memilih jenis konsol: ")
print("1.PS4 : Rp.", PS4)
print("2.PS4_pro: Rp.", PS4_pro)
print("3.PS5 : Rp.", PS5)
playstation = int(input("silahkan pilih jenis penyewaan playstation sesuai angka :"))

if playstation == 1:
    nama_playstation = "PS4"
    harga_ps = 10000
elif playstation == 2:
    nama_playstation = "PS4_pro"
    harga_ps = 15000
elif playstation == 3:
    nama_playstation = "PS5"
    harga_ps = 20000
else :
    print("\nprogram berhenti")
    exit()

if playstation == 1:
    jumlah_jam = float(input("masukkan jumlah jam sewa : "))

    total_harga = harga_ps * jumlah_jam

    if jumlah_jam >= 5:
        diskon_durasi = 0.08 * total_harga
    elif jumlah_jam >= 3:
        diskon_durasi = 0.05 * total_harga
    else :
        diskon_durasi = 0


print("waktu sewa weekday/weekend")
print("1. weekday")
print("2. weekend")

waktu = float(input("pilih waktu sewa : "))
if waktu == 1 :
    waktu_sewa = "weekday"
    biaya_waktu = 0
elif waktu == 2:
    waktu_sewa = "weekend"
    biaya_waktu = 0.1 * total_harga
else:
    print("program berhenti")
    exit()

total_bayar = total_harga - diskon_durasi + biaya_waktu

print("\n=====================================================")
print("                    transaksi penyewaan                ")
print("nama Penyewa : ", biodata)
print("Nim : ", nim)
print("jenis konsol : ", nama_playstation)
print("jumlah jam : ", jumlah_jam)
print("waktu sewa : ", waktu_sewa)
print("total harga : ", total_harga)
print("Jumlah diskon : ", diskon_durasi)
print("biaya Tambahan: ", biaya_waktu)
print("total bayar : ", total_bayar)
print("======================terima kasih=============================")
