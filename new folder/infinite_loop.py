print("Type in 'quit' to exit")
while 1:
    name = input('Enter a name: ')
    print("Word you typed in has", len(name), "characters")
    print("Type in 'quit' to exit")
    if name == 'quit':
        print("you typed in 'quit', Goodbye")
        break