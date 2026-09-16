# Soal: Animasi angka 0 berjalan dari pojok kiri atas hingga pojok kiri bawah dan kembali lagi dari pojok kiri atas ke pojok kiri bawah
# Penjelasan: Gerakan vertikal di kolom kiri, dari atas ke bawah diulang 2 kali
# Asumsi: Tinggi 10 baris, kolom kiri

import time

tinggi = 10

for ulang in range(2):
    for posisi in range(tinggi):
        # Cetak baris kosong sampai posisi 0
        for i in range(tinggi):
            if i == posisi:
                print("0")
            else:
                print()
        time.sleep(0.2)
        # Bersihkan dengan baris kosong (sederhana)
        if posisi != tinggi - 1:
            for k in range(5):
                print()
