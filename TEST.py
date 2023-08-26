print("welcome to my quiz! ")
ask  = input("do you want to play my game? ")
if ask == "yes":
    print("you have 5 quastion to answore")
    quastion_1 = input("what is the biggest mount in the world? ")
    if quastion_1 == "Everest":
        print("successyfuly")
        print("lets go to the next quastion ")
        quastion_2 = input("what is the biggest country in the world? ")
        if quastion_2 == "Russa":
            print("successyfuly")
            print("lets go to the next quastion ")
        else:
            print("sorry you loss ")
            print("have a good day")
    else:
        print("sorry you loss ")
        print("have a good day")
elif ask == "no":
    print("have a good day")