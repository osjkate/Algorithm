n = int(input())
list_shop = list(map(int, input().split()))
m = int(input())
list_customer = list(map(int, input().split()))

count = [0] * 1000001
for i in list_shop:
    count[i] += 1

for i in list_customer:
    if count[i] == 0:
        print("no", end=" ")
    else:
        print("yes", end=" ")

