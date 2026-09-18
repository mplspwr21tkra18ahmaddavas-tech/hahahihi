awal = int(input("Masukkan n_awal: "))
akhir = int(input("Masukkan n_akhir: "))

total = 0
for i in range(awal, akhir + 1):
    if i % 2 == 0:
        total = total + i

print("Total bilangan genap: " + str(total))
