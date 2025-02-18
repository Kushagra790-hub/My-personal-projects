#include <iostream>
#include <cstdlib>
#include <string>
#include <ctime>
#include <cctype>
using namespace std;

int main(){
int e = 0;
while(e == 0){
srand(time(0));
int min = 1, max = 100;
int r = min + (rand() % (max - min + 1));
int e = 0,g,o = 0,sum = 0;
string ch,nk; 
cout << " " << endl;
cout << "Welcome to Guess Game"<< endl;
cout << " " << endl;
cout << "Do you know the rules of this game?" << endl;
cout << "Type y for yes or n for no:"<< endl;
cin >> ch;
for(char &c : ch){
ch = towlower(c);
}
if(ch == "no" or ch == "n"){
cout << " " << endl;
cout << "Rule 1: There will be a random integer developed by the computer." << endl;
cout << " " << endl;
cout << "Rule 2: You have to guess it, till your guess is right." << endl;
cout << " " << endl;
cout << "Rule 3: If your guess is less than the number then it will show that it is low. " << endl;
cout << " " << endl;
cout << "Rule 4: If your guess is greater than the number then it will show that it is high. " << endl;
cout << " " << endl;
cout << "Rule 5: The range of numbers will be from 1 to 100." << endl;
cout << " " << endl;
    while (o == 0){
    cout << " " << endl;
    cout << "Enter your guess: ";
    cin >> g;
    sum += 1;
    if (g < r and g < r-10){
    cout << " " << endl;
    cout << "This is too low." <<endl;
    cout << " " << endl;
    cout << "Please try again." << endl;
    cout << " " << endl;
    o = 0;
    }
    else if (g < r){
    cout << " " << endl;
    cout << "This is low." <<endl;
    cout << " " << endl;
    cout << "Please try again." << endl;
    cout << " " << endl;
    o = 0;
    }
    else if (g > r and g > r+10){
    cout << " " << endl;
    cout << "This is too high." <<endl;
    cout << " " << endl;
    cout << "Please try again." << endl;
    cout << " " << endl;
    o = 0;
    }
    else if (g > r ){
    cout << " " << endl;
    cout << "This is high." <<endl;
    cout << " " << endl;
    cout << "Please try again." << endl;
    cout << " " << endl;
    o = 0;
    }
    else if (g == r){
    cout << " " << endl;
    cout << "Excellent! You guessed the number!" <<endl;
    cout << " " << endl;
    cout << "Your total guesses are: " << sum << endl;
    cout << " " << endl;
    cout << "Would like to play again (y or n)?" << endl;
    cout << " " << endl;
    cin >> nk;
    if (nk == "no" or nk == "n"){
    cout << "Have a good day" << endl;
    cout << " " << endl;
    cout << "Credits:" <<endl;
    cout << " " << endl;
    cout << "Developer: Kushagra Agarwal" << endl;
    cout << " " << endl;
    o = 1;
    e = 1;
    } 
else if (nk == "yes" or nk == "y")
{
o = 1;
}

}
}
}

else if(ch == "yes" or ch == "y")
{
    while (o == 0){
        cout << " " << endl;
        cout << "Enter your guess: ";
        cin >> g;
        sum += 1;
        if (g < r and g < r-10){
        cout << " " << endl;
        cout << "This is too low." <<endl;
        cout << " " << endl;
        cout << "Please try again." << endl;
        cout << " " << endl;
        o = 0;
        }
        else if (g < r){
        cout << " " << endl;
        cout << "This is low." <<endl;
        cout << " " << endl;
        cout << "Please try again." << endl;
        cout << " " << endl;
        o = 0;
        }
        else if (g > r and g > r+10){
        cout << " " << endl;
        cout << "This is too high." <<endl;
        cout << " " << endl;
        cout << "Please try again." << endl;
        cout << " " << endl;
        o = 0;
        }
        else if (g > r ){
        cout << " " << endl;
        cout << "This is high." <<endl;
        cout << " " << endl;
        cout << "Please try again." << endl;
        cout << " " << endl;
        o = 0;
        }
        else if (g == r){
        cout << " " << endl;
        cout << "Excellent! You guessed the number!" <<endl;
        cout << " " << endl;
        cout << "Your total guesses are: " << sum << endl;
        cout << " " << endl;
        cout << "Would like to play again (y or n)?" << endl;
        cout << " " << endl;
        cin >> nk;
        if (nk == "no" or nk == "n"){
        cout << "Have a good day" << endl;
        cout << " " << endl;
        cout << "Credits:" <<endl;
        cout << " " << endl;
        cout << "Developer: Kushagra Agarwal" << endl;
        cout << " " << endl;
        o = 1;
        e = 1;
        } 
    else if (nk == "yes" or nk == "y")
    {
    o = 1;
    }
    
    }
    }
    }
else{
    cout << " " << endl;
    cout << "The input is wrong" << endl;
    cout << " " << endl;
    cout << "Please try again!" << endl;
    cout << " " << endl;
    e = 0;
}

}
}

