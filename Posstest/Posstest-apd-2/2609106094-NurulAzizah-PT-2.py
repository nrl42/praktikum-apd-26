merchandise_1 = 45000
merchandise_2 = 50000
merchandise_3 = 60000
merchandise_4 = 75000
merchandise_5 = 90000
merchandise_6 = 120000
biaya_bungkus= 7500

harga_merchandise = [merchandise_1,merchandise_2,merchandise_3,merchandise_4,merchandise_5,merchandise_6]

total_harga= merchandise_1 + merchandise_2 + merchandise_3 + merchandise_4 + merchandise_5 + merchandise_6 + biaya_bungkus

rata_rata= total_harga / len(harga_merchandise)

hitung_dolar= total_harga * 0.000056

nim= 94

bolean= nim > rata_rata

barang_merchandise = harga_merchandise[-5:-2]  


print("merchandise 1=", merchandise_1)
print("merchandise 2=", merchandise_2)
print("merchandise 3=", merchandise_3)
print("merchandise 4=", merchandise_4)
print("merchandise 5=", merchandise_5)
print("merchandise 6=", merchandise_6)


print("total merchandise:", "Rp", total_harga)
print("rata rata:", rata_rata)
print("total harga menjadi dolar:", hitung_dolar)

print("merchandise seadanya sports:", harga_merchandise)
print("nim:", nim)
print("perbandingan:", bolean)
print("list merchandise:", barang_merchandise)