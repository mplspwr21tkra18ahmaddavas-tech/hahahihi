# Soal: Tampilkan formasi bintang 7
# Pola:
# *****
#  ****
#   ***
#    **
#     *
#    **
#   ***
#  ****
# *****
# Penjelasan: Panah ke kiri / diamond horizontal
# Asumsi: 9 baris, mengerucut ke kanan lalu melebar

# Atas
for i in range(5, 0, -1):
    spasi = " " * (5 - i)
    print(spasi + "*" * i)
# Bawah
for i in range(2, 6):
    spasi = " " * (5 - i)
    print(spasi + "*" * i)
