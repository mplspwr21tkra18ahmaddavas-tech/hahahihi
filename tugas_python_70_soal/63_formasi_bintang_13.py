# Soal: Tampilkan formasi bintang 13
# Pola:
# 0******
# 00*****
# 000****
# 0000***
# 00000**
# 000000*
# Penjelasan: Diagonal 0 dari kiri atas, bintang di kanan
# Asumsi: Lebar 7, 0 bertambah bintang berkurang

for i in range(1, 7):
    nol = "0" * i
    bintang = "*" * (7 - i)
    print(nol + bintang)
