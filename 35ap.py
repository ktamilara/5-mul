import string
a1=input()
a1.split()
a1=a1.replace(" ","")
b1=[i1 for i1 in a1 if a1.count(i1)==1]
c1=' '.join(b1)
print(c1.lower())
