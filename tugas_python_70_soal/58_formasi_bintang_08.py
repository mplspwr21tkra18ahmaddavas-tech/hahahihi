# Soal: Tampilkan formasi bintang 8
# Pola:
# 0**********
# 0**********
# 0**********
# 0**********
# 00000000000
# Penjelasan: Kotak dengan border 0 di kiri dan bawah
# Asumsi: 5 baris, tinggi 5 lebar 11, 0 di kolom pertama dan baris terakhir penuh 0

for i in range(4):
    print("0" + "*" * 10)
print("0" * 11)
