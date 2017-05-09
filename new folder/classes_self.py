class ClassName:
    def create_name(self, name):
        self.name = name

    def display_name(self):
        return self.name

    def saying(self):
        print('Hello, %s' % self.name)


first = ClassName()
second = ClassName()

first.create_name('Xenorm')
print(first.display_name())
first.saying()
