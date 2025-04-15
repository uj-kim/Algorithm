h, m = map(int, input().split())

if m < 45:
  m = m+60
  if h == 0:
    h = 23
  else: h -= 1

print(h, m-45)

