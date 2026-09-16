# Soal: Tampilkan formasi bintang 20
# Pola:
# 0000000
# *******
# =======
# 0000000
# *******
# =======
# Penjelasan: Tiga jenis baris berulang
# Asumsi: Mengikuti sumber, 6 baris bergantian 0, bintang, =

pola = ["0" * 7, "*" * 7, "=" * 7]
for i in range(6):
    print(pola[i % 3])
