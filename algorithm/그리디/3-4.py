n, k = map(int, input().split())
count = 0
result = 0

# while n != 1:
#     if n % k != 0:
#         n -= 1
#         count += 1
#         print(n)
#     else:
#         n /= k
#         count += 1
#         print(n)


while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)



