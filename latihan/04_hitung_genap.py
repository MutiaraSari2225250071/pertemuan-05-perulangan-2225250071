# Input: bilangan bulat positif n
# Proses: menghitung banyak bilangan genap dari 1 sampai n dengan for dan if
# Output: banyak bilangan genap

n = int(input("n: "))

jumlah_genap = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += 1

print(f"Banyak bilangan genap = {jumlah_genap}")