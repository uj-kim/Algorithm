test_case = int(input())
for _ in range(test_case):
  input()
  n, m = map(int, input().split())
  
  sj = sorted(list(map(int, input().split())))
  sb = sorted(list(map(int, input().split())))

  while len(sj)!= 0 and len(sb)!=0:
    if sj[0] < sb[0]:
      del sj[0]
    elif sj[0] >= sb[0]:
      del sb[0]
    
  if len(sj) == 0:
    print('B')
  elif len(sb) == 0:
    print('S')
  else:
    print('C')