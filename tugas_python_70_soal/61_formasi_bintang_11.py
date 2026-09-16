# Soal: Tampilkan formasi bintang 11
# Pola:
# 00000000000
# 0**********
# 0**********
# 0**********
# 0**********
# Penjelasan: Kotak dengan 0 di atas dan kiri
# Asumsi: Baris pertama penuh 0, sisanya 0 di kiri

print("0" * 11)
for i in range(4):
    print("0" + "*" * 10)
