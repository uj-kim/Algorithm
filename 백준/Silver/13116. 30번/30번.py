T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a_list = []
    if a > b:
        a, b = b, a
    
    while a >= 1:
        a_list.append(a)
        a //= 2
    while b >= 1:
        if b in a_list:
            print(b*10)
            break;
        b //= 2


