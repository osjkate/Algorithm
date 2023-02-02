n, k = map(int, input().split())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA.sort()
arrayB.sort(reverse=True)
for i in range(k):
    if arrayA[i] >= arrayB[i]:
        break
    arrayA[i], arrayB[i] = arrayB[i], arrayA[i]

# result = 0
# for i in arrayA:
#     result += i
#
# print(result)

print(sum(arrayA))