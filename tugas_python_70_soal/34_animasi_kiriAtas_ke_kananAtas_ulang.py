# Soal: Animasi angka 0 berjalan dari pojok kiri atas hingga pojok kanan atas dan kembali lagi dari pojok kiri atas ke kanan atas dalam satu baris
# Penjelasan: Angka 0 bergerak dari kiri ke kanan, kemudian mengulang lagi dari kiri ke kanan
# Asumsi: Animasi di satu baris atas, lebar 20 kolom, diulang 2 kali

import time

# Lebar baris
lebar = 20

# Ulang 2 kali dari kiri ke kanan
for ulang in range(2):
    for posisi in range(lebar):
        # Membuat baris dengan 0 di posisi tertentu
        baris = ""
        for i in range(lebar):
            if i == posisi:
                baris = baris + "0"
            else:
                baris = baris + " "
        print(baris, end="\r")
        time.sleep(0.1)
    print()
