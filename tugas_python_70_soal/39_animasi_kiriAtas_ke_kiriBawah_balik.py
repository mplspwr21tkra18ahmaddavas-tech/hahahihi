# Soal: Animasi angka 0 berjalan dari pojok kiri atas hingga pojok kiri bawah dan kembali lagi dari pojok kiri bawah ke pojok kiri atas
# Penjelasan: Gerakan vertikal bolak-balik di kolom kiri
# Asumsi: Tinggi 10 baris

import time

tinggi = 10

# Dari atas ke bawah
for posisi in range(tinggi):
    for i in range(tinggi):
        if i == posisi:
            print("0")
        else:
            print()
    time.sleep(0.2)
    if posisi != tinggi - 1:
        for k in range(3):
            print()

# Dari bawah ke atas
for posisi in range(tinggi - 1, -1, -1):
    for i in range(tinggi):
        if i == posisi:
            print("0")
        else:
            print()
    time.sleep(0.2)
    if posisi != 0:
        for k in range(3):
            print()
