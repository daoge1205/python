#!/usr/bin/python3.5
class studentManage:
	def __init__(self,student):
		"""
			menu为输入菜单选项的变量
			并且每个class函数必须有一个self变量
		"""
		if type(student) != type({}):
			print("构建存储的学生信息的存储结构有误，请使用字典结构")
		self.menu=-1
		self.students=student
	def menuBook(self):
		print ("\n")
		print("***************")
		print("欢迎使用学生管理系统")
		print("1.增添学生信息")
		print("2.查找学生信息")
		print("3.删除学生信息")
		print("0.退出")
		print("***************")
		print("\n")
	def select(self):
		self.menu=input("请输入选型:")
	def addstudent(self):
		name=input('请输入学生姓名:')
		number=input('请输入学生学号:')
		self.students[number]=name
		print("插入信息成功!")
	def findstudent(self):
		try:
			name=input("请输入学号:")
			print('名字为%s' %self.students[name])
		except KeyError:
			print("没有此学号")
	def deleteStudent(self):
		try:
			name=input("请输入学号:")
			student=self.students.pop(name)
			print ("学生姓名为:%s,学号为：%s,已经被删除" %(student,name))
		except KeyError:
			print("没有此学号")
			
members={}
stu=studentManage(members)
stu.menuBook()

while stu.menu != '0':
	stu.select()
	if stu.menu == '1':
		stu.addstudent()
		stu.menuBook()
	elif stu.menu == '2':
		stu.findstudent()
		stu.menuBook()
	elif stu.menu == '3':
		stu.deleteStudent()
		stu.menuBook()
	else:
		print("输入非法选项，请重新输入！")
		stu.menuBook()
		 
print("感谢使用")
	

	
	
	


