r1,s1=input().split()
t1=abs(len(r1)-len(s1))
for i1 in range(len(r1)):
    if len(s1)==1 and s[i1] in r1:
        break
    if r1[i1]!=s1[i1]:
        t1+=1
print(t1)
