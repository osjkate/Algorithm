n = int(input())
list_shop = set(map(int, input().split()))
m = int(input())
list_customer = list(map(int, input().split()))

for i in list_customer:
    if i in list_shop:
        print("yes", end=" ")
    else:
        print("no", end=" ")