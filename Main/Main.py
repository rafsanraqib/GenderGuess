while 1 == 1:
    name = input()
    NameLength = len(name) -1

    if name[NameLength] == 'a':
        print("Gender: Female/Girl")

    if name[NameLength-1] == 'a' and name[NameLength] == 'h':
        print("Gender: Female/Girl")

    if name[0] == 'q':
        print("Have a nice day")
        break
    else :
        print ("Gender: Male/Boy")
