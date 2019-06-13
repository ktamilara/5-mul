n1 = int(input())
a1 = []
if n1%2 == 0:
  for i1 in range(1,n1):
    if n1%i1 == 0 and (i1==1 or i1==2):
      a1.append(i1)
    elif n1%i1 == 0 and i1%2!=0:
      a1.append(i1)
else:
  for i1 in range(1,n1+1):
    if n1%i1 == 0 and (i1==1 or i1==2):
      a1.append(i1)
    elif n1%i1 == 0 and i1%2!=0:
      a1.append(i1)
print(*a1)
