# import time as t
# from time import time
from time import*
start_time=time()
num=int(input("enter the year:"))
if num%4==2:
	print("the year is leep",num)
elif num%4==0:
	print("the year is not leep year",num)
else:
	print("the year is not a leep year")		


end_time=time()
total_time=end_time-start_time
print("total time=",total_time)			