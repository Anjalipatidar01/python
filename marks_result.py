#step1:writinig marks to marks.txt
marks=open("marks.txt","w")
student_name=input("Enter student Name:")
english_marks=int(input("Enter marks obtained in English:"))
hindi_marks=int(input("Enter marks obtained in  Hindi:"))
maths_marks=int(input("Enter marks obtained in Maths:"))
details="{},{},{},{}".format(student_name,english_marks,hindi_marks,maths_marks)
marks.write(details)
marks.close()

#step2:reading marks from marks.txt and calculating average and total marks 
data_file=open("marks.txt","r")
data=data_file.read()
#print(data)
record=data.split(",")
#print(record)
total=0
for i in range(1,len(record)):
	total=total+int(record[i])
average=total/(len(record)-1)
#print(total,average)
data_file.close()

#step3:writing data in results.txt
file=open("result.txt","w")
record.append(str(total))
record.append(str(average))
#print(record)
details=record[0]
for i in range(1,len(record)):
	details=details+","+record[i]
#print(datails)
file.write(details)
file.close()

#step4:read result data and display to the user
file=open("result.txt","r")
data=file.read()
record=data.split(",")
#print("======================================")
print("Welcome to Our Poratal")
#print("======================================")
print("Here is your results")
print("Student Name:",record[0])
print("Marks in English:{} out of {}".format(record[1],20))
print("Marks in Hindi:{} out of {}".format(record[2],20))
print("Marks in Maths:{} out of {}".format(record[3],20))
print("Total Marks:{} out of {}".format(record[4],60))
print("Average Marks:",record[5])
#print("======================================")
file.close()



