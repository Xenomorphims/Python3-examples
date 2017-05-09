class className:
    def defineName(self, name):
        self.name = name
    def displayName(self):
        return 'My name is %s' % self.name
    def saying(self):
        print('I hate people')


first = className()
second = className()

first.defineName('Matende')
print(first.displayName())
first.saying()