# n=5
# for i in range(1,n+1):
#   	print(i*'*')
# n= int(input("Enter value:"))
# for i in range(0,n):
# 	for j in range(0,i+1):
# 		print("*",end=" ")
# print("\r")		
# n= int(input("enter value:"))
# for i in range(1,n+1):
#  	for j in range(1,i+1):
#  		print(j,end=" ")
# print("\r")
n= int(input("Enter value:"))
for i in range(1,n+1):
	num=1
	for j in range(1,(n+1)-i):
		print(end="")
	for k in range(1,i+1):
		print(num,end="")
		num=num+1	
	print("\r")	


