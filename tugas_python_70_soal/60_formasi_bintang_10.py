# Soal: Tampilkan formasi bintang 10
# Pola:
# ******
#  *****
#   ****
#    **
#     *
#    **
#   ***
#  ****
# *****
# Penjelasan: Diamond kecil mirip formasi 7 tapi 6 bintang awal
# Asumsi: Variasi dari formasi 7

for i in range(6, 0, -1):
    spasi = " " * (6 - i)
    # Sesuaikan jumlah bintang
    if i == 4:
        bintang = "***"
    elif i == 2:
        bintang = "**"
    else:
        bintang = "*" * i
    # Sederhana pakai i saja
    print(spasi + "*" * i)
for i in range(2, 6):
    spasi = " " * (6 - i)
    print(spasi + "*" * i)
