n, m = map(int, input().split())
list_long = list(map(int, input().split()))

list_long.sort()
high = max(list_long)


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for i in array:
            if i > mid:
                result += i - mid
        if result == target:
            return mid
        elif result > target:
            start = mid + 1
        else:
            end = mid - 1
    return None


print(binary_search(list_long, m, 0, high))
