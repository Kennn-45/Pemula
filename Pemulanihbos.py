n = int(input())
m = int(input())

total = 0
for i in range (n):
    x = int(input())
    total += x

print ("input N = ", n, "\t input M = ", m)
print("Total damage = ", total)
print ("If damage lebih besar atau sama dengan HP Musuh:")
if total >= m:
    print("Menang")
else: print ("Kalah")