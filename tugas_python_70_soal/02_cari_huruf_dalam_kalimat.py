kalimat = input("Masukkan kalimat: ")
huruf = input("Masukkan huruf yang dicari: ")
jumlah = 0
for c in kalimat:
    if c == huruf:
        jumlah = jumlah + 1
print("Jumlah huruf '" + huruf + "' adalah: " + str(jumlah))
