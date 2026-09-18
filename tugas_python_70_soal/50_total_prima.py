awal = int(input("Masukkan n_awal: "))
akhir = int(input("Masukkan n_akhir: "))

total = 0
for i in range(awal, akhir + 1):
    if i > 1:
        prima = True
        for j in range(2, i):
            if i % j == 0:
                prima = False
                break
        if prima == True:
            total = total + i

print("Jumlah total bilangan prima: " + str(total))
