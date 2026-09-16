# Soal: Tampilkan formasi bintang 16
# Pola:
# 000000*
# 00000**
# 0000***
# 000****
# 00*****
# 0******
# Penjelasan: Sama seperti formasi 15 (variasi)
# Asumsi: Pola segitiga 0 dan bintang

for i in range(6, 0, -1):
    nol = "0" * i
    bintang = "*" * (7 - i)
    print(nol + bintang)
