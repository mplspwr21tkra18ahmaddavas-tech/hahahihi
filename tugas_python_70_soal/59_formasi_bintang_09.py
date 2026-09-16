# Soal: Tampilkan formasi bintang 9
# Pola:
# **********0
# **********0
# **********0
# **********0
# 00000000000
# Penjelasan: Kebalikan formasi 8, 0 di kanan
# Asumsi: Sama tapi 0 di kolom terakhir

for i in range(4):
    print("*" * 10 + "0")
print("0" * 11)
