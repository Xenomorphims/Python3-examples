
class employee(object):

	def __init__(self, name, salary, age):
		self.name = name
		self.salary = salary
		self.age = age
		
x = employee('Xenorm', 10000, 17)
print(x.name)
print(x.salary)
print(x.age)