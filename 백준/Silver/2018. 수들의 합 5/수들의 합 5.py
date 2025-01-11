'''
문제 : 수들의 합
[상황]
임의의 자연수 N은 몇 개의 연속된 자연수의 합으로 나타낼 수 있다.
그 가지수를 구하고 싶음.
ex. 15 => 15, 7+8, 4+5+6, 1+2+3+4+5 // 4가지

[입력]
- 첫째 줄 : 정수 N

[출력]
N을 몇 개의 연속된 자연수의 합으로 나타낼 수 있는지 출력

[의사결정과정]
0. 투포인터 : 배열에서 원소들의 합이 x인 연속 부분배열의 개수를 구하는 문제
1. 목표값 N
2. 1~N 의 자연수가 담긴 배열 생성
3-1. sum < N : right++
3-2. sum > N : left++
3-3. sum == N : count++. count 출력

'''
import sys
input = sys.stdin.readline

N = int(input())

left = 1
right = 1
cur_sum = 0
count = 0

while left <= N:
    if cur_sum < N:
        if right > N:
            break
        cur_sum += right
        right += 1
        
    elif cur_sum > N:
        cur_sum -= left
        left += 1
    else:
        count += 1
        cur_sum -= left
        left += 1

print(count)


