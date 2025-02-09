import sys
import os 
import time
import random as r
def type(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

class Blackjack():
    def __init__ (self):
        self.b = r.randint(1,11)
        type(" \n")
        type("Your first card is: ")
        print(self.b)
        type(" \n")
        type("Do you want to stand or hit?: ")
        self.a = input()
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
                            else:
                                e = 1
                    else:
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
            type(f"You won {self.v} money")
            type("\n")
            return self.v
            

        elif( self.s > self.d and self.s < 22):
            type(" \n")
            type("You have won the game.")
            self.v += self.v
            type(" \n")
            type ("\n")
            type(f"You won {self.v} money")
            type(" \n")
            return self.v

        elif(self.s > 21):
            print(" \n")
            type("You are bust.")
            self.v -= self.v
            print(" \n")
            type("\n")
            type(f"You won {self.v} money")
            print(" \n")
            return self.v
            

        elif(self.s == self.d):
            print(" \n")
            type("The round is draw.")
            type(" \n")
            type("\n")
            type(f"You won {self.v} money")
            type(" \n")
            return self.v 

        elif(self.s > 21):
            type(" \n")
            type("You are bust.")
            type(" \n")

        elif(self.d > 22):
            type(" \n")
            type("The Dealer is bust.")
            type(" \n")        


type("Welcome to Blackjack. \n")
type(" \n")
type("Enter the bets you want to place: ")
q = float(input())
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
            type("Thanks for playing.")
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
            type("Thanks for playing.")
            l = 1

