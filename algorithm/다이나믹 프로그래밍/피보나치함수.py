def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))
# O(2^n) 만큼의 시간 복잡도를 가짐
# fibo(100)을 연산하려면 수백억 년이 걸림