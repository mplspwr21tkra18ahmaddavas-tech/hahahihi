# Soal: Tampilkan formasi bintang 14
# Pola:
# *000000
# **00000
# ***0000
# ****000
# *****00
# ******0
# Penjelasan: Kebalikan formasi 13, bintang di kiri 0 di kanan
# Asumsi: Bintang bertambah 0 berkurang

for i in range(1, 7):
    bintang = "*" * i
    nol = "0" * (7 - i)
    print(bintang + nol)
