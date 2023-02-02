n = int(input())
list_shop = list(map(int, input().split()))
m = int(input())
list_customer = list(map(int, input().split()))

list_shop.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"


for i in list_customer:
    print(binary_search(list_shop, i, 0, n - 1), end=" ")
