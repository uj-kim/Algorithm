#3W_1일차_3번문제
'''
[문제 분석]
- 입력
    1. 첫째 줄 : N
    2. 둘째 줄 : X1,...,XN (공백으로 구분)

- 출력 : 좌표 압축을 적용한 결과 출력
    => X'1, ... , X'N

[문제 풀이 과정]
1. 배열에서 자신보다 작은 수의 개수를 찾는게 목적(중복없이)
2. set으로 중복되는 수를 제거해주고,=> new_nums
3. sorted()로 오름차순 정렬을 해준다
4. for문으로 입력값배열을 순회하면서 new_nums에서 같은 값의 인덱스를 반환.
cf. 해쉬로 매핑하는 방법이 더 효율적. 그런데 아직 모르는 방법이므로 공부해서 시도해볼 것.
'''
#코드
import sys
N = int(sys.stdin.readline())

original_nums = list(map(int,input().split()))

new_nums = sorted(set(original_nums))

#근데 시간복잡도는 n^2으로 안 좋은 방법
# result = list(map(lambda x: new_nums.index(x), original_nums))
mapping = {value: index for index, value in enumerate(new_nums)}

result = [mapping[i] for i in original_nums]


print(" ".join(map(str,result)))

