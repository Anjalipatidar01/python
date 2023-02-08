def myfunction():
	global i
	x=int(input("enter value:"))
	y=int(input("enter value"))
	z=x+y
	 #print(z)       #being z a local variable it can't accessed out side myfunction
	# print(i)
	print(z)
	i="i am inside"
	print(id(i))

i="i am fine"
print(id(i))
print(i)	

# i="I am outside"	 #global variable 
myfunction()
print(i)
# print(z)	