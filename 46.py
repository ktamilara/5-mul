n12,r1=map(int,input().split())
p1=(n12//2)-1
for i1 in range(1,p1+1):
  if i1*p1==r1:
    print("yes")
    break
  else:
    p1-=1
else:
  print("no")
