class A():
	__prNum = 5
	def __init__(self, number, string):
		self.number = number
		self.string = string
a = 1
b = 2

obj = A(4,'Supun')


class B():
	def __init__(self, number):
		self.number = number

	@property
	def prStr(self):
		return "prStr is Private. Value is %s"%self.__prStr
	@prStr.setter
	def prStr(self, string='default'):
		if(type(string)==str):
			self.__prStr = string
		else:
			raise ValueError('Value is not a String')



c = B(7)
c.prStr = 'hi' 
print(obj.string) #Supun
print(a,b) #1 2
print('A: %s'%obj.string) #A: Supun
print("B: %s"%c.prStr) #B: prStr is Private. Value is hi
