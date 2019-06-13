n1=int(input())
astr1=input()
a1=""
c11=""
for i1 in range(len(astr1)):
	if astr1[i1]=="1":
		a1=a1+astr1[i1]+" "
	elif astr1[i1]=="0":
		c11=c11+a1
		a1=""
print(c11.strip())
