# Soal: Animasi angka 0 berjalan dari pojok kiri bawah hingga pojok kanan bawah dan kembali lagi dari pojok kanan bawah ke kiri bawah dalam satu baris
# Penjelasan: Animasi di baris bawah dengan gerakan bolak-balik
# Asumsi: Baris bawah, lebar 20, kiri-kanan lalu kanan-kiri

import time

lebar = 20

for i in range(5):
    print()

# Ke kanan
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

# Balik ke kiri
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
