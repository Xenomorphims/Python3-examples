class ParentClass:
    var1 = 'I am var1'
    var2 = 'I am var2'


class ChildClass(ParentClass):
    pass


parentObject = ParentClass
print('\n\t', parentObject.var1, '\nwith the parent class')

childObject = ChildClass
print('\n\t', childObject.var2, '\nwith the child class')
