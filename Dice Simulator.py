def DiceSimulator(a):
    b = r. randint(1,6)
    print(" ")
    print("Let's start the game: ")
    print(" ")
    print("The Dice is rolling.")
    print(" ")
    print("The number on the dice is: ",b)

     

import random as r
a = input("Do you want to roll the dice? (type yes or no or cheat): ")
e = 0
f = 0
j = 0
while e == 0:
    a = a.lower()
    if a == 'yes':
        c = DiceSimulator(a)
        print(" ")
        d= input("Do you want to continue?(type yes or no or cheat) ")
        d = d.lower()
        if d == 'yes':
            e = 0
        elif d == 'cheat':
            print("Welcome to the probablity enhancer of the Dice:")
            print(" ")
            print("Press 1 of getting 1 on dice.")
            print(" ")
            print("Press 2 of getting 2 on dice.")
            print(" ")
            print("Press 3 of getting 3 on dice.")
            print(" ")
            print("Press 4 of getting 4 on dice.")
            print(" ")
            print("Press 5 of getting 5 on dice.")
            print(" ")
            print("Press 6 of getting 6 on dice.")
            print(" ")
            f = int(input("Enter your choice: "))
            if (f == 1 or f == 2 or f == 3 or f == 4 or f == 5 or f == 6):
                print("The number on the Dice is: ",f)
                print(" ")
                d= input("Do you want to continue?:(type yes or no or cheat) ")
                print(" ")
                d = d.lower()
                if d == 'yes':
                    e = 0

                else:
                    e = 1
            else:
                e = 1

            
    elif a == 'cheat':
        while f == 0:
            print("Welcome to the probablity enhancer of the Dice:")
            print(" ")
            print("Press 1 of getting 1 on dice.")
            print(" ")
            print("Press 2 of getting 2 on dice.")
            print(" ")
            print("Press 3 of getting 3 on dice.")
            print(" ")
            print("Press 4 of getting 4 on dice.")
            print(" ")
            print("Press 5 of getting 5 on dice.")
            print(" ")
            print("Press 6 of getting 6 on dice.")
            print(" ")
            f = int(input("Enter your choice: "))
            if (f == 1 or f == 2 or f == 3 or f == 4 or f == 5 or f == 6):
                print("The number on the Dice is: ",f)
                print(" ")
                d= input("Do you want to continue?: ")
                d = d.lower()
                if d == 'yes' :
                    while j == 0:
                        c = DiceSimulator(a)
                        print(" ")
                        d= input("Do you want to continue?(type yes or no or cheat) ")
                        d = d.lower()
                        if d == 'yes':
                            j = 0
                        elif d == 'cheat':
                            print("Welcome to the probablity enhancer of the Dice:")
                            print(" ")
                            print("Press 1 of getting 1 on dice.")
                            print(" ")
                            print("Press 2 of getting 2 on dice.")
                            print(" ")
                            print("Press 3 of getting 3 on dice.")
                            print(" ")
                            print("Press 4 of getting 4 on dice.")
                            print(" ")
                            print("Press 5 of getting 5 on dice.")
                            print(" ")
                            print("Press 6 of getting 6 on dice.")
                            print(" ")
                            f = int(input("Enter your choice: "))
                            if (f == 1 or f == 2 or f == 3 or f == 4 or f == 5 or f == 6):
                                print("The number on the Dice is: ",f)
                                print(" ")
                                d= input("Do you want to continue?:(type yes or no or cheat) ")
                                print(" ")
                                d = d.lower()
                                if d == 'yes':
                                    j = 0

                                else:
                                    e = 1
                            else:
                                e = 1

                else:
                    f = 0   

    else:
        print(" ")
        print("Please choose the right number for a dice")
        d= input("Do you want to continue?: ")
        d = d.lower()
        if d == 'yes':
            e = 0
        else:
            e = 1    



   
if e == 1:
    print(" ")
    print("Have a good day: ")
