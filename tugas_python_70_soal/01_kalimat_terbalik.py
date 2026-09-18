kalimat = input("Masukkan kalimat: ")
hasil = ""
for i in range(len(kalimat) - 1, -1, -1):
    hasil = hasil + kalimat[i]
print(hasil)
