#Special cases
n1 = "abdullah"
n2 = "isa"
n3 = "hamza"
n4 = "aunt"
n5 = "uncle"
n6 = "dad"
n7 = "mom"
n8 = "cousin"
n9 = "dadu"
n10 = "chacchi"
n11 = "bhabi"
n12 = "bhaiya"
n13 = "baba"
n14 = "ammu"
default = "quit"
while True:
    UserInput = input()
    name = UserInput.lower()          #Converts the UserInput to lowercase
    NameLength = len(name) -1

    if name[0] == ' ' or name == " ": #prevents the program from crashing
        continue

    if name == n4 or name == n5 or name == n6 or name == n7 or name == n8 or name == n9 or name == n10 or name == n11 or name == n12 or name == n13 or name == n14:
        print("Silly! Thats not even a name")
        continue

    if name == n1 or name == n2 or name == n3 :
        print("Gender: Male/Boy")
        continue

    if name[NameLength] == 'a':
        print("Gender: Female/Girl")
        continue

    if name[NameLength-1] == 'a' and name[NameLength] == 'h':
        print("Gender: Female/Girl")
        continue

    if name[NameLength-1] == 'i' and name[NameLength] == 'e':
        print("Gender: Female/Girl")
        continue

    if name == n1 or name == n2 or name == n3:
        print("Gender: Male/Boy")
        continue

    if name[NameLength-1] == 's' and name[NameLength] == 'y':
        print("Gender: Female/Girl")
        continue
    #Checks if user typed quit
    if name == default:
        print("Thank you for using my app, Have a nice day")
        print("Created by Rafsan, The Greatest of all Time")
        break
    else :
        print ("Gender: Male/Boy")
