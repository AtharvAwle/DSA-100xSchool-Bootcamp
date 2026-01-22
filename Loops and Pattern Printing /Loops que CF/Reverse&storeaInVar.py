n = int(input())
var = 0

if n == 0:
    print(0)
else:
    while n != 0:
        var = (var * 10) + (n % 10)
        n = n // 10
    print(var)