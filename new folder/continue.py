while True:
    s = input ('Enter something: ')
    if s == 'quit':
        break
    if s == 'q':
        break
    if s == 'exit':
        break

    if len(s) < 5:
        print ('Too small')
    if len(s) > 10:
        print ('Too large')
        continue
    print ('Input is a sufficient length')
print ('Done')
print ('\t *WRITTEN BY XENORM*')
    #Do other kinds of processing here...
