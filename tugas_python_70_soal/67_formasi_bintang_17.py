# Soal: Tampilkan formasi bintang 17
# Pola:
# 000000*
# 00000*0
# 0000*00
# 000*000
# 00*0000
# 0*00000
# Penjelasan: Bintang diagonal dari kanan atas ke kiri bawah dengan 0 sebagai background
# Asumsi: Satu bintang bergerak diagonal

for i in range(6):
    nol_kiri = "0" * (5 - i)
    nol_kanan = "0" * i
    print(nol_kiri + "*" + nol_kanan)
