# Soal: Tampilkan formasi bintang 18
# Pola:
# *000000
# 0*00000
# 00*0000
# 000*000
# 0000*00
# 00000*0
# Penjelasan: Kebalikan formasi 17, bintang diagonal dari kiri atas ke kanan bawah
# Asumsi: Diagonal berlawanan

for i in range(6):
    nol_kiri = "0" * i
    nol_kanan = "0" * (5 - i)
    print(nol_kiri + "*" + nol_kanan)
