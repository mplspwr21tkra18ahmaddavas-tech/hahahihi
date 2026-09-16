# Soal: Animasi angka 0 berjalan dari pojok kiri atas hingga pojok kanan atas dan kembali lagi dari pojok kanan atas ke kiri atas dalam satu baris
# Penjelasan: Angka 0 bergerak kiri ke kanan lalu balik kanan ke kiri
# Asumsi: Satu baris, lebar 20

import time

lebar = 20

# Gerak ke kanan
for posisi in range(lebar):
    baris = ""
    for i in range(lebar):
        if i == posisi:
            baris = baris + "0"
        else:
            baris = baris + " "
    print(baris, end="\r")
    time.sleep(0.1)
print()

# Gerak balik ke kiri
for posisi in range(lebar - 1, -1, -1):
    baris = ""
    for i in range(lebar):
        if i == posisi:
            baris = baris + "0"
        else:
            baris = baris + " "
    print(baris, end="\r")
    time.sleep(0.1)
print()
