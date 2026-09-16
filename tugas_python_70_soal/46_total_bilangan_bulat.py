# Soal: Program untuk menghitung total bilangan bulat positif dari n_awal hingga n_akhir
# Penjelasan: Menjumlahkan semua bilangan dari awal sampai akhir
# Asumsi: Termasuk batas awal dan akhir

awal = int(input("Masukkan n_awal: "))
akhir = int(input("Masukkan n_akhir: "))

total = 0
for i in range(awal, akhir + 1):
    total = total + i

print("Total: " + str(total))
