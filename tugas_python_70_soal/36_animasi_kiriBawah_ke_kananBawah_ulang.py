# Soal: Animasi angka 0 berjalan dari pojok kiri bawah hingga pojok kanan bawah dan kembali lagi dari pojok kiri bawah ke kanan bawah dalam satu baris
# Penjelasan: Sama seperti soal 34 tapi di baris bawah (diberi beberapa baris kosong di atas)
# Asumsi: Menampilkan beberapa baris kosong agar terlihat di bawah, lalu animasi 2 kali kiri ke kanan

import time

lebar = 20

# Memberi jarak agar terlihat di bawah
for i in range(5):
    print()

for ulang in range(2):
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
