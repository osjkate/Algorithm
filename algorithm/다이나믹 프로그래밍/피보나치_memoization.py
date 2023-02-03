# 한 번 계산된 결과를 Memoization하기 위한 리스트 초기화
d = [0] * 100


# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    print('f(' + str(x) + ')', end=" ") # 현재의 피보나치 수를 출력하도록 함
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(6))


# 이전에 계산했던 적이 있는 결과값을 메모리 공간에 메모해두고 같은 식을 호출하면 메모한 결과를 가져온다!
