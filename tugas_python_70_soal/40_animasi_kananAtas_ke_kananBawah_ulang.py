# Soal: Animasi angka 0 berjalan dari pojok kanan atas hingga pojok kanan bawah dan kembali lagi dari pojok kanan atas ke pojok kanan bawah
# Penjelasan: Gerakan vertikal di kolom kanan, diulang 2 kali dari atas ke bawah
# Asumsi: Tinggi 10, kolom kanan (diberi spasi di depan)

import time

tinggi = 10
lebar = 20

for ulang in range(2):
    for posisi in range(tinggi):
        for i in range(tinggi):
            if i == posisi:
                # Cetak 0 di kanan
                print(" " * (lebar - 1) + "0")
            else:
                print()
        time.sleep(0.2)
        if posisi != tinggi - 1:
            for k in range(3):
                print()
