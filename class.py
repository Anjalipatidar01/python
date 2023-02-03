class student:
	def __init__(self,name,course,subject):
		self.name=name
		self.course=course
		self.subject=subject
	def show(self):
		print("Name:",self.name)
		print("Course:",self.course)
		print("Subject:",self.subject)

s1=student("Ram","BCA","ADA")
s1.show()			