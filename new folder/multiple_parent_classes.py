# create a class named DadClass
class DadClass:
    # Assign two variables to the class
    var1 = 'Hi I am the father class variable'
    var2 = 'Hi I am also a father class variable'


# create a class named MumClass
class MumClass:
    # Assign two variables to the class
    var1 = 'Hi I am the mother class variable'
    var2 = 'Hi I am also a mother class variable'


# create a class named ChildClass
class ChildClass(DadClass, MumClass):
    pass

# make objects
dadObject = DadClass()
mumObject = MumClass()
childObject = MumClass()

# print the objects
print(dadObject.var1)
print(dadObject.var2)

print(mumObject.var1)
print(mumObject.var2)

print(childObject.var1)
print(childObject.var2)
