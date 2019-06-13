try:
	p11=int(input())
	if(p11>=-2**15+1  and p11<=2**15+1):
	    print ("INT")
	elif p11>=-2**31+1 and p11<=2**31+1:
	    print("LONG")  
	else:
	    print ("LONG LONG")
except ValueError:
	print("invalid")

