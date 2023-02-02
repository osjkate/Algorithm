n, m = map(int, input().split())
list_long = list(map(int, input().split()))

list_long.sort()
high = max(list_long)
result = 0

while True:
    result = 0
    high -= 1
    for i in list_long:
        n = i - high
        if n <= 0:
            continue
        else:
            result += n
    if result >= m:
        break

print(high)
