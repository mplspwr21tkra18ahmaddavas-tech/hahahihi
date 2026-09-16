# Soal: Buat Program untuk menampilkan Tahun kabisat dari n_awal hingga n_akhir yang angka terakhirnya 6
# Penjelasan: Kabisat berakhiran 6
# Asumsi: Kabisat = habis dibagi 4

awal = int(input("Masukkan tahun awal: "))
akhir = int(input("Masukkan tahun akhir: "))

for tahun in range(awal, akhir + 1):
    if tahun % 4 == 0 and tahun % 10 == 6:
        print(tahun, end=" ")
print()
