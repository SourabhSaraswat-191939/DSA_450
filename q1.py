first = input()
second = input()
i = input().lower()
countF = 0
countS = 0
for ch in first:
    if i==ch:
        countF+=1

for ch in second:
    if i==ch.lower():
        countS+=1

if countF>countS:
    print(first)
    print(countF)

elif countF<countS:
    print(second)
    print(countS)

else:
    print("Both strindgs have same frequency of given character")