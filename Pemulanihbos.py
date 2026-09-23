n = int(input())
m = int(input())

total = 0
for i in range (n):
    x = int(input())
    total += x

print(total)
if total >= m:
    print("Menang")
else: print ("Kalah")