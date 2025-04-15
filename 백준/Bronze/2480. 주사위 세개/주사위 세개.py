a, b, c = map(int, input().split())
price = 0

if a == b == c:
  price = 10000 + a * 1000

elif len({a, b, c}) < 3:
  if a == b or a == c:
    num = a
  else:
    num = b
  price = 1000 + num * 100

else:
  price = max(a, b, c) * 100

print(price)