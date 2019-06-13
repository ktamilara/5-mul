a1=raw_input().split()
y1=[]
for i1 in range(0,len(a1)):
	g1=a1[i1]
	r1=len(g1)
	for j1 in range(0,r1):
		u1=g1.count(g1[j1])
		y1.append(u1)
	w1=max(y1)
	for k1 in range(0,r1):
		if w1==y1[k1]:
			print g1[k1],
			break
	y1=[]
