a11,b1=input().split()
c1=0
for i1 in range(15):
    if int(b1)**i1==int(a11):
        c1+=1
        break
if c1==1:
    print("yes")
else:
    print("no")
