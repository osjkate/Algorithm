n = int(input())
array = list(map(int, input().split()))


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        x //= 10
        res = res * 10 + t
    return res


def isPrime(x):
    if x == 1:
        return False    # 1은 약수가 없기 때문에 따로 처리를 해주어야 한다.
    for i in range(2, x // 2 + 1):  # 절반까지만 확인하면 된다!
        if x % i == 0:
            return False
    return True


for i in array:
    reNum = reverse(i)
    if isPrime(reNum):
        print(reNum, end=" ")
