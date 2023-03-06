n = int(input())
array = list(map(int, input().split()))

sum = 0
count = 0
score = [0] * n
for i in range(n):
    if array[i] == 0:
        count = 0
    else:
        count += 1
        score[i] = count

for i in score:
    sum += i

print(sum)

