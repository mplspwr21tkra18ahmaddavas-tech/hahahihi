# Soal: Masukkan kalimat, cari huruf yang diinginkan dan menghitung jumlah huruf tersebut dalam kalimat
# Penjelasan: Program meminta kalimat dan satu huruf, lalu menghitung berapa kali huruf itu muncul
# Asumsi: Perhitungan membedakan huruf besar dan kecil

# Memasukkan kalimat
kalimat = input("Masukkan kalimat: ")

# Memasukkan huruf yang dicari
huruf = input("Masukkan huruf yang dicari: ")

# Menghitung jumlah huruf
jumlah = 0
for c in kalimat:
    if c == huruf:
        jumlah = jumlah + 1

# Menampilkan hasil
print("Jumlah huruf '" + huruf + "' adalah: " + str(jumlah))
