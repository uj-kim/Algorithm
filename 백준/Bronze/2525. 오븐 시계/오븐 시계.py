h, m = map(int, input().split())
t = int(input())

total_minutes = h * 60 + m + t
h = (total_minutes // 60) % 24
m = total_minutes % 60

print(h, m)
