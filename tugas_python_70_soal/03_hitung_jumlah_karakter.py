# Soal: Masukkan kalimat, hitung jumlah karakter yang ada di kalimat
# Penjelasan: Program meminta kalimat lalu menghitung jumlah karakter termasuk spasi
# Asumsi: Menghitung semua karakter termasuk spasi

# Memasukkan kalimat
kalimat = input("Masukkan kalimat: ")

# Menghitung jumlah karakter dengan perulangan sederhana
jumlah = 0
for c in kalimat:
    jumlah = jumlah + 1

# Menampilkan hasil
print("Jumlah karakter: " + str(jumlah))
