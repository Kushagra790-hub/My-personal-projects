import sys
import os 
import time
import random as r
def type(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

class Blackjack():
    def __init__ (self):
        self.b = r.randint(1,11)
        type("\n")
        type("Do you know the rules of Blackjack: ")
        self.ru = input()
        type("\n")
        self.ru = self.ru.lower()

        if (self.ru == "no"):
            type("Rule 1: The cards are ranged from 1 to 11.\n\
\n\
Rule 2: You have to approach the sum of 21 by adding all the cards.\n\
\n\
Rule 3: The provided cards will be random.\n\
\n\
Rule 4: If the sum of the cards is greater than 21. You cards will be bust and you will lose the game.\n\
\n\
Rule 5: You will be playing against the dealer.\n\
\n\
Rule 6: The sum of the cards of dealer will also be less than 22.\n\
\n\
Rule 7: If the sum of the dealer is greater than 21 than you will win the game.\n\
\n\
Rule 8: If both the player and the dealer sum is less than 21 than a comparision will done to check which sum is greater between them.\n\
\n\
Rule 9: The greatest sum between them will win.\n\
\n\
Rule 10: If you win you will recieve double the amount of your principle money.\n\
\n\
Rule 11: If you lose you will get nothing.\n ")
            type(" \n")
            type("Your first card is: ")
            print(self.b)
            type(" \n")
            type("Do you want to stand or hit?: ")
            self.a = input()
            self.a = self.a.lower()
            if(self.a == 'hit'): 
                self.c = r.randint(1,11)
                self.s = self.c + self.b
                type(" \n")
                type("The second card is: ")
                print(self.c)
                type(" \n")
                type(f"{self.s} is the sum of your cards.")
                type("  \n")
                e = 0 
                if(self.s > 21 or self.s == 21):
                    e = 1
                else:
                    type(" \n")
                    type("Do you want to stand or hit?: ")
                    self.o = input()
                    self.o = self.o.lower()
                    if self.o == 'hit':   
                        while e == 0:
                            if self.s > 21 or self.s == 21:
                                e = 1
                            elif (self.o == "hit"):
                                self.d = r.randint(1,11)
                                self.s = self.s + self.d
                                type("\n")
                                type("The third card is: ")
                                print(self.d)
                                type(" \n")
                                type(f"{self.s} is the sum of your cards.")
                                type(" \n")
                                type("\n")
                                while e == 0:    
                                    if self.s > 21 or self.s == 21:
                                        e = 1
                                    else:
                                        type("Do you want to stand or hit?: ")
                                        self.p = input()
                                        self.p = self.p.lower()
                                        if (self.p == "hit"):
                                            self.m = r.randint(1,11)
                                            self.s = self.s + self.m
                                            type(" \n")
                                            type("The next card is: ")
                                            print(self.m)
                                            type(" \n")
                                            type(f"{self.s} is the the sum of your cards.")
                                            type(" \n")
                                            type("\n")
                                            e = 0
                                        elif self.p == "stand":
                                            self.s = self.b +self.c + self.d
                                            e = 1
                                        
                                        elif(self.p == "cheat"):
                                            self.m = r.randint(1,11)
                                            self.h = 21 - self.s
                                            self.s = self.h + self.s
                                            type(" \n")
                                            type("The next card is: ")
                                            print(self.h)
                                            type(" \n")
                                            type(f"{self.s} is the sum of your cards.")
                                            type("  \n")
                                            e = 1

                                        else:
                                            type("\n")
                                            type("Please enter valid input.")
                                            type("\n")
                                            type("\n")
                                            self.p = False
                                            e = 1    
                    elif self.o =="stand":
                        self.s = self.b + self.c
                        e = 1
                    elif(self.o == "cheat"):
                        self.d = r.randint(1,11)
                        self.h = 21 - self.s
                        self.s = self.h + self.s
                        type(" \n")
                        type("The third card is: ")
                        print(self.h)
                        type(" \n")
                        type(f"{self.s} is the sum of your cards.")
                        type("  \n")
                        e = 1
                    else:
                        type("\n")
                        type("Please enter valid input.")
                        type("\n")
                        type("\n")
                        self.o = False
                        e = 1                 
            elif self.a == "stand":
                self.s = self.b
                e = 1
            elif(self.a == "cheat"):
                self.c = r.randint(1,11)
                self.h = 21 - self.b
                self.s = self.h + self.b
                type(" \n")
                type("The second card is: ")
                print(self.h)
                type(" \n")
                type(f"{self.s} is the sum of your cards.")
                type("  \n")
                e = 1
            else:
                type("\n")
                type("Please enter valid input.")
                type("\n")
                type("\n")
                self.a = False
                e = 1    
        else:
            type(" \n")
            type("Your first card is: ")
            print(self.b)
            type(" \n")
            type("Do you want to stand or hit?: ")
            self.a = input()
            self.a = self.a.lower()
            if(self.a == 'hit'): 
                self.c = r.randint(1,11)
                self.s = self.c + self.b
                type(" \n")
                type("The second card is: ")
                print(self.c)
                type(" \n")
                type(f"{self.s} is the sum of your cards.")
                type("  \n")
                e = 0 
                if(self.s > 21 or self.s == 21):
                    e = 1
                else:
                    type(" \n")
                    type("Do you want to stand or hit?: ")
                    self.o = input()
                    self.o = self.o.lower()
                    if self.o == 'hit':   
                        while e == 0:
                            if self.s > 21 or self.s == 21:
                                e = 1
                            elif (self.o == "hit"):
                                self.d = r.randint(1,11)
                                self.s = self.s + self.d
                                type("\n")
                                type("The third card is: ")
                                print(self.d)
                                type(" \n")
                                type(f"{self.s} is the sum of your cards.")
                                type(" \n")
                                type("\n")
                                while e == 0:    
                                    if self.s > 21 or self.s == 21:
                                        e = 1
                                    else:
                                        type("Do you want to stand or hit?: ")
                                        self.p = input()
                                        self.p = self.p.lower()
                                        if (self.p == "hit"):
                                            self.m = r.randint(1,11)
                                            self.s = self.s + self.m
                                            type(" \n")
                                            type("The next card is: ")
                                            print(self.m)
                                            type(" \n")
                                            type(f"{self.s} is the the sum of your cards.")
                                            type(" \n")
                                            type("\n")
                                            e = 0
                                        elif self.p == "stand":
                                            self.s = self.b +self.d + self.c
                                            e = 1
                                        
                                        elif(self.p == "cheat"):
                                            self.m = r.randint(1,11)
                                            self.h = 21 - self.s
                                            self.s = self.h + self.s
                                            type(" \n")
                                            type("The next card is: ")
                                            print(self.h)
                                            type(" \n")
                                            type(f"{self.s} is the sum of your cards.")
                                            type("  \n")
                                            e = 1

                                        else:
                                            type("\n")
                                            type("Please enter valid input.")
                                            type("\n")
                                            type("\n")
                                            self.p = False
                                            e = 1    
                    elif self.o =="stand":
                        self.s = self.b + self.c
                        e = 1
                    elif(self.o == "cheat"):
                        self.d = r.randint(1,11)
                        self.h = 21 - self.s
                        self.s = self.h + self.s
                        type(" \n")
                        type("The third card is: ")
                        print(self.h)
                        type(" \n")
                        type(f"{self.s} is the sum of your cards.")
                        type("  \n")
                        e = 1
                    else:
                        type("\n")
                        type("Please enter valid input.")
                        type("\n")
                        type("\n")
                        self.o = False
                        e = 1                 
            elif self.a == "stand":
                self.s = self.b
                e = 1
            elif(self.a == "cheat"):
                self.c = r.randint(1,11)
                self.h = 21 - self.b
                self.s = self.h + self.b
                type(" \n")
                type("The second card is: ")
                print(self.h)
                type(" \n")
                type(f"{self.s} is the sum of your cards.")
                type("  \n")
                e = 1
            else:
                type("\n")
                type("Please enter valid input.")
                type("\n")
                type("\n")
                self.a = False
                e = 1   

    def Dealer(self):
        type(" \n")
        self.h = r.randint(1,11)
        type("The dealer first card is: ")
        print(self.h)
        self.k = r.randint(1,11)
        self.d = self.k + self.h
        type(" \n")
        type("The second card is: ")
        print(self.k)
        type(" \n")
        type(f"{self.d} is the sum of dealer's cards.")
        type("\n")
        if (self.d >= 13 and self.d <= 16):
            self.m = 2
            self.d =  self.d +self.m
            type(" \n")
            type("The Dealer's third card is: ")
            print(self.m)
            type(" \n")
            type("The total of the dealer's sum is: ")
            print(self.d)

        elif(self.d > 8 and self.d < 13):
            self.m = 5
            self.d =  self.d +self.m
            type(" \n")
            type("The Dealer's third card is: ")
            print(self.m)
            type(" \n")
            type("The total of the dealer's sum is: ")
            print(self.d)

        elif(self.d <= 8 ):
            self.m = 11
            self.d =  self.d +self.m
            type(" \n")
            type("The Dealer's third card is: ")
            print(self.m)
            type(" \n")
            type("The total of the dealer's sum is: ")
            print(self.d)    
    
    def Comparision(self,v):
        self.v = v
        self.g = 22
        
        if( self.d > self.s and self.d < 22):
            type(" \n")
            type("The dealer has won the game.")
            self.v -= self.v
            type(" \n")
            type("\n")
            type(f"You won {self.v}$ money")
            type("\n")
            return self.v
            

        elif( self.s > self.d and self.s < 22):
            type(" \n")
            type("You have won the game.")
            self.v += self.v
            type(" \n")
            type ("\n")
            type(f"You won {self.v}$ money")
            type(" \n")
            return self.v

        elif(self.s > 21):
            print(" \n")
            type("You are bust.")
            self.v -= self.v
            print(" \n")
            type("\n")
            type(f"You won {self.v}$ money")
            print(" \n")
            return self.v
            

        elif(self.s == self.d):
            print(" \n")
            type("The round is draw.")
            type(" \n")
            type("\n")
            type(f"You won {self.v}$ money")
            type(" \n")
            return self.v 

        elif(self.s > 21):
            type(" \n")
            type("You are bust.")
            type(" \n")
            type("\n")
            type(f"You won {self.v}$ money")
            type(" \n")
            return self.v

        if(self.a == 0 or self.o == 0 or self.p == 0):
            type("\n")
            type("You lost the game.")
            type("\n")
            type("\n")
            self.v -= self.v
            type(f"You won {self.v}$ money")
            type("\n")
            return self.v

        elif(self.d > 21):
            type(" \n")
            type("The Dealer is bust.")
            type(" \n")
            type("\n")
            type(f"You won {self.v}$ money")
            type(" \n")
            return self.v        


type("Welcome to Blackjack. \n")
type(" \n")
type("Enter the bets/money you want to place/put in $: ")
q = float(input())
type("\n ")
l = 0
while l == 0: 
    w = Blackjack()
    i = w.Dealer()
    j = w.Comparision(q)

    if j == 0.0:
        type(" \n")
        type("You lost the game.")
        type(" \n")
        type("\n")
        type("Please restart the game.")
        type(" \n")
        type("\n")
        type("Do you want to play next round?: ")
        A = input()
        A = A.lower()
        if(A == 'yes'):
            l = 0
        else:
            type(" \n")
            type("Please give us your rating(out of five): ")
            ra = float(input())
            if ra == 1:
                type("\n")
                type("⭐")
                type("\n")
                type("\n")               
                type("Rating: 😐")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                l = 1
            
            elif ra >= 1.1 and ra <= 1.5:
                type("\n")
                type("⭐🌟")
                type("\n")
                type("\n")               
                type("Rating: 👍")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                l = 1
            
            elif ra >= 1.6 and ra <= 1.9:
                type("\n")
                type("⭐⭐⭐⭐🌟🌟")
                type("\n")
                type("\n")               
                type("Rating: 👊")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1 
            
            elif ra == 2:
                type("\n")
                type("⭐⭐")
                type("\n")
                type("\n")
                type("Rating: 😊")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1
            
            elif ra >= 2.1 and ra <= 2.5:
                type("\n")
                type("⭐⭐🌟")
                type("\n")
                type("\n")
                type("Rating: ✌️")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

            elif ra >= 2.6 and ra <= 2.9:
                type("\n")
                type("⭐⭐⭐⭐🌟🌟")
                type("\n")
                type("\n")               
                type("Rating: 🤌")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1 
            
            elif ra == 3:
                type("\n")
                type("⭐⭐⭐")               
                type("\n")
                type("\n")
                type("Rating: 😁")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

            elif ra >= 3.1 and ra <= 3.5:
                type("\n")
                type("⭐⭐⭐🌟")               
                type("\n")
                type("\n")
                type("Rating: 🤘")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

            elif ra >= 3.6 and ra <= 3.9:
                type("\n")
                type("⭐⭐⭐⭐🌟🌟")
                type("\n")
                type("\n")               
                type("Rating: 💪")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1 

            elif ra  == 4:
                type("\n")
                type("⭐⭐⭐⭐")
                type("\n")
                type("\n")               
                type("Rating: ❤️")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

            elif ra >= 4.1 and ra <= 4.5:
                type("\n")
                type("⭐⭐⭐⭐🌟")
                type("\n")
                type("\n")               
                type("Rating: 🫰")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

            elif ra >= 4.6 and ra <= 4.9:
                type("\n")
                type("⭐⭐⭐⭐🌟🌟")
                type("\n")
                type("\n")               
                type("Rating: 😂")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1    

            elif ra == 5:
                type("\n")
                type("⭐⭐⭐⭐⭐")
                type("\n")
                type("\n")               
                type("Rating: 🎉")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

    else:
        type("\n")
        type("Do you want to play next round?: ")
        A = input()
        A = A.lower()
        if(A == 'yes'):
            l = 0
        else:
            type(" \n")
            type("Please give us your rating(out of five): ")
            ra = float(input())
            if ra == 1:
                type("\n")
                type("⭐")
                type("\n")
                type("\n")               
                type("Rating: 😐")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                l = 1
            
            elif ra >= 1.1 and ra <= 1.5:
                type("\n")
                type("⭐🌟")
                type("\n")
                type("\n")               
                type("Rating: 👍")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                l = 1
            
            elif ra >= 1.6 and ra <= 1.9:
                type("\n")
                type("⭐⭐⭐⭐🌟🌟")
                type("\n")
                type("\n")               
                type("Rating: 👊")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1 
            
            elif ra == 2:
                type("\n")
                type("⭐⭐")
                type("\n")
                type("\n")
                type("Rating: 😊")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1
            
            elif ra >= 2.1 and ra <= 2.5:
                type("\n")
                type("⭐⭐🌟")
                type("\n")
                type("\n")
                type("Rating: ✌️")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

            elif ra >= 2.6 and ra <= 2.9:
                type("\n")
                type("⭐⭐⭐⭐🌟🌟")
                type("\n")
                type("\n")               
                type("Rating: 🤌")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1 
            
            elif ra == 3:
                type("\n")
                type("⭐⭐⭐")               
                type("\n")
                type("\n")
                type("Rating: 😁")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

            elif ra >= 3.1 and ra <= 3.5:
                type("\n")
                type("⭐⭐⭐🌟")               
                type("\n")
                type("\n")
                type("Rating: 🤘")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

            elif ra >= 3.6 and ra <= 3.9:
                type("\n")
                type("⭐⭐⭐⭐🌟🌟")
                type("\n")
                type("\n")               
                type("Rating: 💪")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1 

            elif ra  == 4:
                type("\n")
                type("⭐⭐⭐⭐")
                type("\n")
                type("\n")               
                type("Rating: ❤️")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

            elif ra >= 4.1 and ra <= 4.5:
                type("\n")
                type("⭐⭐⭐⭐🌟")
                type("\n")
                type("\n")               
                type("Rating: 🫰")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1

            elif ra >= 4.6 and ra <= 4.9:
                type("\n")
                type("⭐⭐⭐⭐🌟🌟")
                type("\n")
                type("\n")               
                type("Rating: 😂")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1    

            elif ra == 5:
                type("\n")
                type("⭐⭐⭐⭐⭐")
                type("\n")
                type("\n")               
                type("Rating: 🎉")
                type("\n")
                type("\n")
                type("Thanks for playing.")
                type("\n")
                type("\n")
                type("Credits: \n\
\n\
Developer: Kushagra Agarwal")
                type("\n")
                type("\n")
                l = 1
