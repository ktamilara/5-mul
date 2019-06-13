s1,k11=map(str,input().split())
k11=int(k11)
c1=len(s1)
a1=s1
for i1 in range(0,k11):
	a1=a1[-1]+a1[:c1-1]
print(a1)
