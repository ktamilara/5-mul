import math
n1=int(input())
s1=math.radians(n1)
if(s1>0 and s1<1):
	print(round(math.sin(s1),2))
else:
	print(round(math.sin(s1)))
