# Soal: Buat Program untuk menampilkan Tahun kabisat dari n_awal hingga n_akhir yang angka terakhirnya 2
# Penjelasan: Sama seperti soal 24 tapi berakhiran 2
# Asumsi: Kabisat = habis dibagi 4

awal = int(input("Masukkan tahun awal: "))
akhir = int(input("Masukkan tahun akhir: "))

for tahun in range(awal, akhir + 1):
    if tahun % 4 == 0 and tahun % 10 == 2:
        print(tahun, end=" ")
print()
