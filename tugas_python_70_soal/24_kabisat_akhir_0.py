# Soal: Buat Program untuk menampilkan Tahun kabisat dari n_awal hingga n_akhir yang angka terakhirnya 0
# Penjelasan: Menampilkan tahun kabisat di rentang tertentu yang berakhiran 0
# Asumsi: Tahun kabisat adalah yang habis dibagi 4

# Memasukkan rentang tahun
awal = int(input("Masukkan tahun awal: "))
akhir = int(input("Masukkan tahun akhir: "))

# Perulangan dari awal sampai akhir
for tahun in range(awal, akhir + 1):
    # Cek kabisat dan angka terakhir 0
    if tahun % 4 == 0 and tahun % 10 == 0:
        print(tahun, end=" ")
print()
