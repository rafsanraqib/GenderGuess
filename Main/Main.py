name = input()
NameLen = len(name)-1

if name[NameLen] == 'a':
    print("Gender: Female/Girl")

if name[NameLen-1] == 'a' and name[NameLen] == 'h':
    print("Gender: Female/Girl")

else :
    print("Gender: Male/Boy")
