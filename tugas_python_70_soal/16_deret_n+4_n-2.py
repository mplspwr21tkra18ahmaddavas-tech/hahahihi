# Soal: Buat tampilan angka berikut : 1 5 3 7 5 9 7 11 9 13 11 15 , => n+4,n-2,...
# Penjelasan: Deret dengan dua langkah selang-seling +4 dan -2
# Asumsi: Menampilkan 12 angka pertama sesuai pola

# Angka awal
angka = 1
# Jumlah yang ditampilkan
jumlah = 12
for i in range(jumlah):
    print(angka, end=" ")
    # Jika posisi genap (0,2,4..) tambah 4, jika ganjil kurang 2
    if i % 2 == 0:
        angka = angka + 4
    else:
        angka = angka - 2
print()
