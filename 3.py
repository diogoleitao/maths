def a():
  n = 1
  while n < 10**9:
    st = str(n)
    if len(st) % 3 == 0:
      s1 = st[:int(len(st)/3)]
      s2 = st[int(len(st)/3):int(2*len(st)/3)]
      s3 = st[int(2*len(st)/3):int(len(st))]
      if int(s1)**3+int(s2)**3+int(s3)**3 == int(st):
        print n
        n += 1
      else:
        n += 1
    else:
      n = 10*n
a()
