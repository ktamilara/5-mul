n1=int(input())
s1=input()
a1=""
c1=""
for i1 in range(len(s1)):
	if s1[i1]=="1":
		a1=a1+s1[i1]+" "
	elif s1[i1]=="0":
		c1=c1+a1
		a1=""
print(c1.strip())
