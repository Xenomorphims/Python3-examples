#'ab' is short for 'a'dress'b'ook

ab = {
    'Innocent' : 'innocentmsakala@gmail.com',
    'Chris' : 'wailesichris@gmail.com',
    'Larry' : 'larrywhatsoon@hotmail.com',
    'Matsumoto' : 'matz@ruby-lang.org',
    'Spammer' : 'spammer@yahoo.com'
    }

print("Innocent's adress is", ab['Innocent'])

#Deleting a key-value pair
del ab['Spammer']

print('\nThere are {} contacts in the adress-book\n' .format(len(ab)))

for name, adress in ab.items():
    print('Contact {} at {}' .format(name, adress))

#Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's adress is", ab['Guido'])
