n = int(input())
arr = list(map(int, input().split()))

positive = 0
negative = 0
even = 0
odd = 0

for x in arr:
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1

    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print(positive)
print(negative)
print(even)
print(odd)