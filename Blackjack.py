import random as r
class Blackjack():
    def __init__ (self):
        print("Welcome to Blackjack. ")
        print(" ")
        self.b = r.randint(1,11)
        print("Your first card is: ",self.b)
        print(" ")
        self.a = input("Do you want to stand or hit? ")
        self.c = r.randint(1,11)
        self.s = self.c + self.b
        print(" ")
        print("The second card is: ",self.c)
        print(" ")
        print(f"{self.s} is the sum of your cards")
        print(" ")
        e = 0 
        self.o = input("Do you want to stand or hit? ")
        self.o = self.o.lower()
        while e == 0:
            if (self.o == "hit"):
                self.d = r.randint(1,11)
                self.s = self.s + self.d
                print(" ")
                print("The third card is: ",self.d)
                print(" ")
                print(f"{self.s} is the sum of your cards")
                print(" ")
                while e == 0:    
                    self.p = input("Do you want to stand or hit? ")
                    self.p = self.p.lower()
                    if (self.p == "hit"):
                        self.m = r.randint(1,11)
                        self.s = self.s + self.m
                        print(" ")
                        print("The next card is: ",self.m)
                        print(" ")
                        print(f"{self.s} is the the sum of your cards")
                        print(" ")
                        e = 0
                    else:
                        e = 1
            else:
                    e = 1   
            
    def Dealer(self):
        print(" ")
        self.h = r.randint(1,11)
        print("The dealer first card is: ",self.h)
        self.k = r.randint(1,11)
        self.d = self.k + self.h
        print(" ")
        print("The second card is: ",self.k)
        print(" ")
        print(f"{self.d} is the sum of dealer's cards")
        if (self.d >= 13 and self.d <= 16):
            self.m = 2
            self.d =  self.d +self.m
            print(" ")
            print("The Dealer's third card is: ",self.m)
            print(" ")
            print("The total of the dealer's sum is: ",self.d)

        elif(self.d > 8 and self.d < 13):
            self.m = 5
            self.d =  self.d +self.m
            print(" ")
            print("The Dealer's third card is: ",self.m)
            print(" ")
            print("The total of the dealer's sum is: ",self.d)

        elif(self.d <= 8 ):
            self.m = 11
            self.d =  self.d +self.m
            print(" ")
            print("The Dealer's third card is: ",self.m)
            print(" ")
            print("The total of the dealer's sum is: ",self.d)    
    
    def Comparision(self,v):
        self.v = v
        self.g = 22
        if( self.d > self.s and self.d < 22):
            print(" ")
            print("The dealer has won the game.")
            self.v -= self.v
            print(" ")
            print(f"You won {self.v} money")
            return self.v
            

        elif( self.s > self.d and self.s < 22):
            print(" ")
            print("You have won the game. ")
            self.v += self.v
            print(" ")
            print(f"You won {self.v} money")
            print(" ")
            return self.v

        elif(self.s > 21):
            print(" ")
            print("You are bust.")
            self.v -= self.v
            print(" ")
            print(f"You won {self.v} money")
            print(" ")
            return self.v
            

        elif(self.s == self.d):
            print(" ")
            print("The round is draw.")
            print(" ")
            print(f"You won {self.v} money")
            print(" ")
            return self.v 

        elif(self.s > 21):
            print(" ")
            print("You are bust.")
            print(" ")

        elif(self.d > 22):
            print(" ")
            print("The Dealer is bust.")
            print(" ")        


q = float(input("Enter the bets you want to place: "))
l = 0
while l == 0: 
    w = Blackjack()
    i = w.Dealer()
    j = w.Comparision(q)

    if j == 0.0:
        print(" ")
        print("You lost the game.")
        print(" ")
        print("Please restart the game.")
        print(" ")
        A = input(("Do you want to play next round? "))
        A = A.lower()
        if(A == 'yes'):
            l = 0
        else:
            print(" ")
            print("Thanks for playing.")
            l = 1

    else:
        A = input(("Do you want to play next round? "))
        A = A.lower()
        if(A == 'yes'):
            l = 0
        else:
            print(" ")
            print("Thanks for playing.")
            l = 1
