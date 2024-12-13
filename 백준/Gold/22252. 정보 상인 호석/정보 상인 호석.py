import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

gorillas = defaultdict(list)
result = 0

Q = int(input())

for _ in range(Q):
    cmd = input().split()

    # 명령어 유형 확인
    if cmd[0] == '1':  # 정보 추가
        name = cmd[1]
        infos = list(map(int, cmd[3:]))
        for val in infos:
            heapq.heappush(gorillas[name], -val)

    elif cmd[0] == '2':  # 정보 구매
        name = cmd[1]
        b = int(cmd[2])
        
        # 힙이 비어있는지 확인
        if gorillas[name]:
            for _ in range(b):
                if gorillas[name]:  # 힙에 값이 있을 때만 pop
                    result += -heapq.heappop(gorillas[name])
                else:
                    break  # 더 이상 pop할 값이 없으면 중단

print(result)
