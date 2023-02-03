var_1=input("entar value:")
world_list=[]
temp_word=""
for i in range(len(var_1)):
	if var_1[i]==" ":
		world_list.append(temp_word)
		temp_word=" "
	else:
		temp_word=temp_word+var_1[i]

world_list.append(temp_word)
print("user defined sentence:",var_1)
print("world list:",world_list)		
