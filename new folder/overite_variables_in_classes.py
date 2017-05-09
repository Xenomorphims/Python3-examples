class ParentClass:
    var1 = 'Sandwich'
    var2 = 'Fried chicken'


class ChildClass(ParentClass):
    var2 = 'Hot coffee'


parentObject = ParentClass()
childObject = ChildClass()

print(parentObject.var1, "is my favourite food."'\n')
print(parentObject.var2, "is my second favorite food."'\n')

print(childObject.var1, "is still my favorite food."'\n')
print(childObject.var2, "is what i prefer over fried chicken."'\n')
