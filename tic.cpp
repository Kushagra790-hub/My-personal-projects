#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;

char ar[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};
int row,column,q,rn;
char token = 'X';
bool tie = false;
string p1 = "";
string p2 = "";



void functionOne(){

    
    cout<< "_________________________" << endl;
    cout<< "|       |       |       |" << endl;
    cout<< "|   "<< ar[0][0]<<"   |   "<< ar[0][1]<<"   |   "<< ar[0][2]<<"   |" << endl;
    cout<< "|_______|_______|_______|" << endl;
    cout<< "|       |       |       |" << endl;
    cout<< "|   "<< ar[1][0]<<"   |   "<< ar[1][1]<<"   |   "<< ar[1][2]<<"   |" << endl;
    cout<< "|_______|_______|_______|" << endl;
    cout<< "|       |       |       |" << endl;
    cout<< "|   "<< ar[2][0]<<"   |   "<< ar[2][1]<<"   |   "<< ar[2][2]<<"   |" << endl;
    cout<< "|_______|_______|_______|" << endl;
    

}

void functionTwo(){

if(q==1){
int digit;
if(token == 'X'){

    cout << p1 << ",please enter the position: " << endl;
    cin >> digit;
}

if(token == 'O'){

    cout << "The Opponent Value is: " << rn << endl;
    digit = rn;
} 

if (digit == 1){

    row = 0;
    column = 0;
} 
else if (digit == 2){

    row = 0;
    column = 1;
} 
else if (digit == 3){

    row = 0;
    column = 2;

}
else if (digit == 4){

    row = 1;
    column = 0;
}
else if (digit == 5){

    row = 1;
    column = 1;

}
else if (digit == 6){

    row = 1;
    column = 2;

}
else if (digit == 7){

    row = 2;
    column = 0;

}
else if (digit == 8){

    row = 2;
    column = 1;

}
else if (digit == 9){

    row = 2;
    column = 2;

}
else if(digit > 9 or digit < 0){

    cout << "Invalid Output." << endl;
    cout << "Please try again." << endl;

}


if(token == 'X' and ar[row][column] != 'X' and ar [row][column] != 'O'){

    ar[row][column] = 'X';
    token = 'O';
}
else if (token == 'O' and ar[row][column] != 'X' and ar [row][column] != 'O'){

    ar[row][column] = 'O';
    token = 'X';
}
else{
cout << "There is no empty space." << endl;
cout << "Please try again." << endl;
functionTwo();
}
}

else if(q == 2){
int digit;
if(token == 'X'){

    cout << p1 << ",please enter the position: " << endl;
    cin >> digit;
}

if(token == 'O'){

    cout << p2 << ",please enter the position: " << endl;
    cin >> digit;
} 

if (digit == 1){

    row = 0;
    column = 0;
} 
else if (digit == 2){

    row = 0;
    column = 1;
} 
else if (digit == 3){

    row = 0;
    column = 2;

}
else if (digit == 4){

    row = 1;
    column = 0;
}
else if (digit == 5){

    row = 1;
    column = 1;

}
else if (digit == 6){

    row = 1;
    column = 2;

}
else if (digit == 7){

    row = 2;
    column = 0;

}
else if (digit == 8){

    row = 2;
    column = 1;

}
else if (digit == 9){

    row = 2;
    column = 2;

}
else if(digit > 9 or digit < 0){

    cout << "Invalid Output." << endl;
    cout << "Please try again." << endl;

}


if(token == 'X' and ar[row][column] != 'X' and ar [row][column] != 'O'){

    ar[row][column] = 'X';
    token = 'O';
}
else if (token == 'O' and ar[row][column] != 'X' and ar [row][column] != 'O'){

    ar[row][column] = 'O';
    token = 'X';
}
else{
cout << "There is no empty space." << endl;
cout << "Please try again." << endl;
functionTwo();
}
}
}

bool functionThree(){
   if(q == 1 or q == 2){ 
    
    for (int i = 0; i < 3; i++){
        
        if(ar[i][0] == ar [i][1] and ar[i][0] == ar[i][2] or ar[0][i] == ar[1][i] and ar[0][i] == ar[2][i]){
            return true;
        }
    }
if (ar[0][0] == ar[1][1] and ar[1][1] == ar[2][2] || ar[0][2] == ar[1][1] and ar[1][1] == ar[2][0]){
    return true;
}

for (int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
        if(ar[i][j] != 'X' and ar[i][j] != 'O' ){
            return false;
        }
    }
}
tie = true;
return true;
}
}

int main(){

cout << "Enter the name of the player 1: "<<endl;
cin >> p1;
cout << "Press 1 if you want to play with AI or 2 if you want to play with a friend." << endl;
cin >> q;
if(q == 2){
cout << "Enter the name of the player 2: "<<endl;
cin >> p2;
cout << "Player 1 name is: " << p1 << endl;
cout << "Player 2 name is: " << p2 <<endl;
cout <<p1 << " will move first." << endl;
cout <<p2 << " will move second." << endl;
}

if (q == 1){
while (!functionThree()){
srand(time(0));
int min = 1, max = 9;
rn = min + (rand() % (max - min + 1));
    functionOne();
    functionTwo();
    functionThree();
}    

if(token == 'X' and tie == false){
    functionOne();
    cout << rn << " wins this Tic-Tac-Toe" << endl;
}
}
if(token == 'O' and tie == false){
    functionOne();
    cout << p1 << " wins this Tic-Tac-Toe" << endl;
}
else if(tie == true){
    functionOne();
    cout << "Its a draw" << endl;
}




if (q == 2){
while (!functionThree()){
    functionOne();
    functionTwo();
    functionThree();

}



if(token == 'X' and tie == false){
    functionOne();
    cout << p2 << " wins this Tic-Tac-Toe" << endl;
}

if(token == 'O' and tie == false){
    functionOne();
    cout << p1 << " wins this Tic-Tac-Toe" << endl;
}
else if(tie == true){
    functionOne();
    cout << "Its a draw" << endl;
}
}
return 0;
}
