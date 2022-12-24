# var1=open("intro.txt","a")
# var1.write("anjali patidar")
# var1.close()

# var1=open("intro.txt","r")
# data=var1.read()
# print(data)
# var1.close()

f=open("teliphone.txt","a")
name=input("enter you name:")
age=input("enter your age:")
city=input("enter youe city:")
detail="Hi i am {}.\ni am {} year old.\ni live in{}.".format(name,age,city)

print(detail)
f.write(detail)
f.close()

f=open("teliphone.txt","r")
data=f.read()
print(data)
f.close()