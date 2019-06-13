a1,b1=input().split()
c1=0
if len(a1)==len(b1):
    for i1 in range(len(a1)):
        if a1[i1]==b1[i1]:
            c1+=1
    if c1==len(b1):
        print("yes")
    else:
        print("no")
else:
    print("no")
