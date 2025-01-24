#1003번 문제 : 피보나치
'''
[상황]
- N번째 피보나치 수를 구하는 함수
def fibonacci(n) : 
    if n == 0:
        print('0')
    elif n == 1:
        print('1')
    else:
        return fibonacci(n-1) + fibonacci(n-2)

[입력]
1. 첫번째 줄 : 테스트케이스의 개수 T
2. T개의 줄 : N (0<= N <= 40)

[출력]
각 테스트케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수(공백 구분)

[문제 해결 과정]
0. dp => 한 번 계산된 값이 저장되기 때문에 재귀호출로 인한
   중복계산을 안 해주고 비어있는 부분만 갱신됨
1. 규칙발견
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(2) => fibonacci(1) + 0
    fibonacci(3) => fibonacci(2) + fibonacci(1)
                    fibonacci(1) + fibonacci(0) + fibonacci(1)
    fibonacci(5) => fibonacci(4) + fibonacci(3)
                    fibonacci(3) + fibonacci(2) + fibonacci(3)
    결국 f(5) =  f(1) + f(0) + f(1) + f(1) + f(0) + f(1) + f(0) + f(1)
    
    f(5)가 0을 출력하는 횟수는 3
    f(5)가 1을 출력하는 횟수는 5


'''
#fibonacci, dp
def fibonacci(N):
    zero = [0]*(N+2)
    one = [0]*(N+2)

    #fibonacci(0)
    zero[0], one[0] = 1, 0
    #fibonacci(1)
    zero[1], one[1] = 0, 1

    for i in range(2, N+1):
        zero[i] = zero[i-2] + zero[i-1]
        one[i] = one[i-2] + one[i-1]

    print(zero[N], one[N])

#입력값처리
T = int(input())
for _ in range(T):
    N = int(input())
    #테스트케이스 함수 실행
    fibonacci(N)
