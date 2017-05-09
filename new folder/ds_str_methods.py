# This is a string object
name = 'Xenorm'

if name.startswith('Xen'):
    print('Yes, the string starts with "Xen"')

if 'e' in name:
    print('Yes, it contains the string "e"')

if name.find('norm') != -1:
    print('Yes, it contains the string "norm"')

delimiter = '_*_'
mylist = ['Japan', 'Britain', 'Russia', 'China']
print(delimiter.join(mylist))
