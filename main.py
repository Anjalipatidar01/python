# import sample1
import sample1 as s
# from sample1 import * 
#calculating permutation

n,r = int(input("enter value of n:")),int(input("enter value of r:"))
if n>=r:
	result=s.fact(n)/s.fact(n-r)
	print(result)
else:	
	print("n should be greater than r")

#claculating combination
n,r=int(input("enter your value:")),int(input("enter value of r:"))
if n>r:
	result=s.fact(n)/(s.fact(r)*s.fact(n-r))
	print(result)
else:
	print("n should be greater than r")	

	
