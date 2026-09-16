# Soal: Tampilkan formasi bintang 15
# Pola:
# 000000*
# 00000**
# 0000***
# 000****
# 00*****
# 0******
# Penjelasan: 0 di kiri bintang di kanan diagonal
# Asumsi: Mirip 13 tapi bintang di kanan bawah lebih banyak

for i in range(6, 0, -1):
    nol = "0" * i
    bintang = "*" * (7 - i)
    print(nol + bintang)
