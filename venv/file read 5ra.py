pass

while True:
    try:
        i = int(input('Select: '))
        if i in range(4):
            files(i)
            break
    except:    
        pass

    print ('\nIncorrect input, try again')