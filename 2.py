def a():
  n = 1
  while n < 10**9:
    st = str(n)
    if len(st) % 2 == 0:
      s1 = st[:int(len(st)/2)]
      s2 = st[int(len(st)/2):int(2*len(st)/2)]
      if int(s1)**2+int(s2)**2 == int(st):
        print n
        n += 1
      else:
        n += 1
    else:
      n = 10*n
a()
