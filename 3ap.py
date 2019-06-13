import sys, string, math
s11,s12 = input().split()
m11 = len(s11)
m12 = len(s12)
if m12 > m11 :
    j1 = 0
    while j1<m11 and s11[j1] == s12[j1] :
        j1 += 1
    print(m12-j1)
elif m12 == m11 :
    j1 = 0
    while j1<m12 and s11[j1] == s12[j1] :
        j1 += 1
    print(m12-j1)
else :
    j1 = 0
    while j1<m12 and s11[j1] == s12[j1] :
        j1 += 1
    s131 = s11[j1:]
    s132 = s12[j1:]
    L1 = list(s131)
    k1 = 0
    for c1 in s132 :
        if c1 in L1 :
            k1 += 1
            L1.remove(c1)
    print(m11-j1-k1)
