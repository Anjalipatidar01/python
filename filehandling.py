var1=open("intro2.py","a")
var1.write("marks")
var1.close()
f=open("teliphon2.txt","w")
english=int(input("enter english marks:"))
hindi=int(input("enter hindi marks:"))
maths=int(input("enter maths marks:"))
detail="ENGLISH={}\nHINDI={}\nMATHS={}".format(english,hindi,maths)
print(detail)
f.write(detail)
total=(english+hindi+maths)
average=total/3
print("total of these subjects are",total)
print("average of these subjects are",average)
f.close()