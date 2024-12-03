#최소비용구하기(두 파일을 합쳐나가는 과정)
# 최소니까 heap을 사용할 예정

import heapq

t = int(input()) #테스트케이스개수
for _ in range(t):
    k = int(input()) #파일의 장수
    files = list(map(int,input().split()))
    heapq.heapify(files)

    total = 0

    while len(files) > 1:
        f1 = heapq.heappop(files)
        f2 = heapq.heappop(files)
        temp = f1 + f2
        total += temp

        heapq.heappush(files, temp)
        
    print(total)
    
