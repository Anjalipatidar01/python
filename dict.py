dict1={"name":"deepak","class":"bca","subject":"commerce"}
dict2={1:"25",2:"25",3:"26",3:"27"}
# for i in dict1:
# 	# print(i)
# 	print(dict1[i])
for i,j in dict1.items():
	print(i)
	print(j)
for i,j in dict2.items():
	print(i)
	print(j)
dict1["name"]="sunny"
print(dict1)
dict1["school"]="nahi pata"
print(dict1)
dict1.pop("subject")
print(dict1)	

	