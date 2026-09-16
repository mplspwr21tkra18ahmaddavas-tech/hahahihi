# Soal: Tampilkan formasi bintang 19
# Pola:
# 0000000
# 0*****0
# 0*****0
# 0*****0
# 0*****0
# 0000000
# Penjelasan: Kotak dengan border 0 dan isi bintang
# Asumsi: Lebar 7 tinggi 6

print("0" * 7)
for i in range(4):
    print("0" + "*" * 5 + "0")
print("0" * 7)
