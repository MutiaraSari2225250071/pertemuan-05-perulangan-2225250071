# Input: bilangan bulat positif n
# Proses: menjumlahkan bilangan dari 1 sampai n dengan for
# Output: jumlah bilangan dari 1 sampai n

n = int(input("n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah = {total}")