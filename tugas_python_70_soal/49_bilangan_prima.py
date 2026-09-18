awal = int(input("Masukkan n_awal: "))
akhir = int(input("Masukkan n_akhir: "))

for i in range(awal, akhir + 1):
    # Cek prima
    if i > 1:
        prima = True
        for j in range(2, i):
            if i % j == 0:
                prima = False
                break
        if prima == True:
            print(i, end=" ")
print()
