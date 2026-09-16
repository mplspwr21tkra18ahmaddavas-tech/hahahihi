# Soal: Animasi angka 0 berjalan dari pojok kanan atas hingga pojok kanan bawah dan kembali lagi dari pojok kanan bawah ke pojok kanan atas
# Penjelasan: Gerakan vertikal bolak-balik di kolom kanan
# Asumsi: Tinggi 10, lebar 20

import time

tinggi = 10
lebar = 20

# Atas ke bawah
for posisi in range(tinggi):
    for i in range(tinggi):
        if i == posisi:
            print(" " * (lebar - 1) + "0")
        else:
            print()
    time.sleep(0.2)
    if posisi != tinggi - 1:
        for k in range(3):
            print()

# Bawah ke atas
for posisi in range(tinggi - 1, -1, -1):
    for i in range(tinggi):
        if i == posisi:
            print(" " * (lebar - 1) + "0")
        else:
            print()
    time.sleep(0.2)
    if posisi != 0:
        for k in range(3):
            print()
