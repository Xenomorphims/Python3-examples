class Girl:
    gender = 'Female'

    def __init__(self, name):
        self.name = name

r = Girl('\nRachel')
m = Girl('\nMary')

print(r.name)
print(r.gender)

print(m.name)
print(m.gender)