username_input = "nurul"
password_input = "094"
uang_bulanan = 3500000 
total_pengeluaran = 0
status = True
status_pilihan = True

print("-----------validasi Login -----------")
for i in range(1,4):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == username_input and password == password_input:
        print("\nLogin berhasil! Selamat Datang di rekapitulasi Keuangan")
        while status == True:
            print("\nMenu Pilihan:")
            print("1. Catat Pengeluaran")
            print("2. Cek Sisa Uang Saku")
            print("3. Keluar")
            pilihan = input("Silahkan Pilih menu (1-3): ")
            if pilihan == "1":
                while status_pilihan == True:
                    pengeluaran = float(input("\nMasukkan jumlah pengeluaran: "))
                    total_pengeluaran += pengeluaran
                    print("\n------------------ Catatan Pengeluaran -----------------------")
                    print(f"Pengeluaran Anda sebesar: Rp{pengeluaran} telah ditambahkan.")
                    print(f"Total pengeluaran Anda saat ini: Rp{total_pengeluaran}")
                    print("---------------------------------------------------------------")
                    pilihan_lagi = input("\nApakah Anda ingin rekapitulasi pengeluaran lagi? (YA/TIDAK): ").upper()
                    if pilihan_lagi == "YA":
                        continue
                    elif pilihan_lagi == "TIDAK":
                        status_pilihan = False
                        continue
            elif pilihan == "2":
                    print("\n----------------- Sisa Uang Saku ---------------------")
                    uang_saku = uang_bulanan - total_pengeluaran
                    print(f"Sisa uang saku Anda adalah: Rp{uang_saku}")
                    print("---------------------------------------------------------------")
                    continue
            elif pilihan == "3":
                    print("\nTerima kasih telah menggunakan rekapitulasi Keuangan.")
                    status = False
                    break
        break
    else:
        sisa_percobaan = 3 - i
        print("\nusername atau password salah, silahkan coba lagi.")
        if sisa_percobaan > 0:
            print(f"\nusername atau password salah. Anda memiliki {sisa_percobaan}x percobaan lagi.")
        else:
            print("\nAnda telah gagal login sebanyak 3 kali. Akun Anda telah diblokir.")