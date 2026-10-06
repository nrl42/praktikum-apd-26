# for in range(4)


# batas = 5
# for i in range(batas):
#     print("perulangan ke-", i)


# for sapa in range(5):
#     print("halo,selamat siang")

# praktikum = ["apd", "orsikon", "jarkon", 70, 89, 77]
# for i in praktikum:
#     print(i)    #menampilkann perbaris
#     #print(i, end=" ") menampilkan kalo gak perbaris

# for i in range(1,10,2):
#     print("angka ke-i adalah ", i)

# for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
# print('') #biar ada jarak tiap iterasi  

# jawab = "ya"
# hitung = 0

# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total Perulangan : {hitung}")

# username = "nurul"
# batas = 0
# while batas < 3:
#     login = input("masukkan username :")
#     if login != username:
#         batas += 1
#     else:
#        batas = 3

# for i in range(10):
#     print(i)
#     if i == 5:
#         break

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range (1,4)
#     if i == 2:
#         break
#     print(i)

tinggi = int(input("masukkan tinggi yang di mau :"))
# for i in range(1, tinggi + 1):
    # print("*" * i)

tinggi = int(input("masukkan tinggi yang dimau : "))
for i in range(tinggi):
    print(" " * (tinggi - i - 1), end="")
    print("*" * (1+1))