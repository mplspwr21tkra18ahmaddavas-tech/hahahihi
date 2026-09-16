# Soal: Masukkan kalimat, kemudian tampilkan kalimat tersebut dimulai dari urutan yang paling belakang (terbalik). Contoh = Hallo -> ollaH
# Penjelasan: Program meminta kalimat dari pengguna, kemudian membalik urutan hurufnya
# Asumsi: Tidak ada asumsi tambahann

# Meminta input kalimat dari pengguna
kalimat = input("Masukkan kalimat: ")

# Membalik kalimat dengan perulangan
hasil = ""
for i in range(len(kalimat) - 1, -1, -1):
    hasil = hasil + kalimat[i]

# Menampilkan hasil
print(hasil)
