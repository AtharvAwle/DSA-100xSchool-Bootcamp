n = int(input())
original = n
var = 0

while n != 0:
    var = (var * 10) + (n % 10)
    n //= 10

if original == var:
    print("YES")
else:
    print("NO")
    