# Soal: Program untuk menghitung total bilangan ganjil dari n_awal hingga n_akhir
# Penjelasan: Menjumlahkan hanya bilangan ganjil
# Asumsi: Termasuk batas

awal = int(input("Masukkan n_awal: "))
akhir = int(input("Masukkan n_akhir: "))

total = 0
for i in range(awal, akhir + 1):
    if i % 2 == 1:
        total = total + i

print("Total bilangan ganjil: " + str(total))
