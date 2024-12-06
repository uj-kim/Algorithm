#3W_2일차_6번문제 : 완전 이진 트리
'''
[문제 분석]
- 도로의 깊이가 K인 완전 이진트리 : (2^k - 1)개의 노드
- 입력
    1. 도로의 깊이 K
    2. 상근이가 방문한 빌딩의 번호(들어간 순서대로, 중복X)
- 출력
    총 K개의 줄 : i번째 줄 -> 레벨이 i인 빌딩의 번호

[문제 해결 과정]
1. dfs 관련 문제(stack, 재귀 중 stack으로 구현/ 재귀도 가능)
깊이 우선 탐색을 한 결과가 입력값.
원래의 이진트리를 알아내야 하는 문제.
2. 리스트의 중앙값을 계속 반환.(k만큼 반복)
- 노드의 깊이. 즉 레벨별로 출력.
- 레벨별(층층이)로 따로 노드를 분리해서 담아둘 예정

'''
#코드
K = int(input())
building_nums = list(map(int, input().split()))
result = [[] for _ in range(K)]
#dfs
'''
완전이진트리의 노드 개수는 홀 수 (인덱스는 짝수로 떨어짐)
반으로 나눠서 가운데 인덱스를 맨 앞에 넣어주고
인덱스를 3씩 끊어서 가운데를 뽑아. 리스트가 빌 때까지?
'''
def original(building_nums, result, depth):
    if not building_nums:
        return
#루트 노드 뽑아주기
    mid_index = len(building_nums) // 2
    parent_node = building_nums[mid_index]
    result[depth].append(parent_node)
#루트노드를 기준으로 좌, 우 나눠주기
    left_side = building_nums[:mid_index]
    right_side = building_nums[mid_index+1:]
    
    #재귀
    original(left_side, result, depth + 1)
    original(right_side, result, depth + 1)

original(building_nums, result, 0)

for i in result:
    print(*i)