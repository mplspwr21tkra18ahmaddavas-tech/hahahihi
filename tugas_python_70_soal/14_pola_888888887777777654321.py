# Soal: Buat tampilan angka berikut : 888888887777777654321543214444333211
# Penjelasan: Pola menurun campuran, menampilkan angka besar ke kecil dengan aturan tertentu
# Asumsi: Untuk i=8 sampai 1, gabungan pola berulang dan menurun, disesuaikan agar output sesuai contoh

# Pola ini menampilkan 88888888 7777777 654321 54321 4444 333 21 1
for i in range(8, 0, -1):
    if i == 8 or i == 7 or i == 4 or i == 3:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
print()
