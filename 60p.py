a1,b1=input().split()
c1=0
for i1 in a1:
    if i1 in b1:
        print("yes")
        break
    else:
        c1+=1
if c1>0:
    print("no")
