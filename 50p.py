a11=int(input())
f1=0
for i1 in range(2,a11):
	if a11%i1==0:
		f1=1
print("yes" if f1==1 else "no")
