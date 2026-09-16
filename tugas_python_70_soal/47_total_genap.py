# Soal: Program untuk menghitung total bilangan genap dari n_awal hingga n_akhir
# Penjelasan: Menjumlahkan hanya bilangan genap di rentang tersebut
# Asumsi: Termasuk batas

awal = int(input("Masukkan n_awal: "))
akhir = int(input("Masukkan n_akhir: "))

total = 0
for i in range(awal, akhir + 1):
    if i % 2 == 0:
        total = total + i

print("Total bilangan genap: " + str(total))
