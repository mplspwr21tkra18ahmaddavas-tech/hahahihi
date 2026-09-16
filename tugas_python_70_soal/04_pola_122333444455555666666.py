# Soal: Buat tampilan angka berikut : 122333444455555666666
# Penjelasan: Menampilkan angka 1 sebanyak 1 kali, 2 sebanyak 2 kali, sampai 6 sebanyak 6 kali
# Asumsi: Pola untuk n=1 sampai 6

# Perulangan untuk angka 1 sampai 6
for i in range(1, 7):
    # Tampilkan angka i sebanyak i kali
    for j in range(i):
        print(i, end="")
# Ganti baris di akhir
print()
