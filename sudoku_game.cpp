#include <iostream>
#include <math.h>
using namespace std;

void Print(int board[][9], int n){
//     for (int i = 0; i < n; i++)
// {
//     for (int j = 0; j < n; j++){
//         cout << board [i][j] << " ";
//     }
//     cout << endl;
// }
// cout << endl;

cout <<"_____________________________________"<<endl;
cout <<"|_" << board[0][0] << "_|_" <<board[0][1] << "_|_" << board[0][2] << "_|_" << board[0][3] << "_|_" << board[0][4] << "_|_" << board[0][5] << "_|_" << board[0][6] <<"_|_" << board[0][7] << "_|_" << board[0][8] <<"_|"<<endl;
cout <<"|_" << board[1][0] << "_|_" <<board[1][1] << "_|_" << board[1][2] << "_|_" << board[1][3] << "_|_" << board[1][4] << "_|_" << board[1][5] << "_|_" << board[1][6] <<"_|_" << board[1][7] << "_|_" << board[1][8] <<"_|"<<endl;
cout <<"|_" << board[2][0] << "_|_" <<board[2][1] << "_|_" << board[2][2] << "_|_" << board[2][3] << "_|_" << board[2][4] << "_|_" << board[2][5] << "_|_" << board[2][6] <<"_|_" << board[2][7] << "_|_" << board[2][8] <<"_|"<<endl;
cout <<"|_" << board[3][0] << "_|_" <<board[3][1] << "_|_" << board[3][2] << "_|_" << board[3][3] << "_|_" << board[3][4] << "_|_" << board[3][5] << "_|_" << board[3][6] <<"_|_" << board[3][7] << "_|_" << board[3][8] <<"_|"<<endl;
cout <<"|_" << board[4][0] << "_|_" <<board[4][1] << "_|_" << board[4][2] << "_|_" << board[4][3] << "_|_" << board[4][4] << "_|_" << board[4][5] << "_|_" << board[4][6] <<"_|_" << board[4][7] << "_|_" << board[4][8] <<"_|"<<endl;
cout <<"|_" << board[5][0] << "_|_" <<board[5][1] << "_|_" << board[5][2] << "_|_" << board[5][3] << "_|_" << board[5][4] << "_|_" << board[5][5] << "_|_" << board[5][6] <<"_|_" << board[5][7] << "_|_" << board[5][8] <<"_|"<<endl;
cout <<"|_" << board[6][0] << "_|_" <<board[6][1] << "_|_" << board[6][2] << "_|_" << board[6][3] << "_|_" << board[6][4] << "_|_" << board[6][5] << "_|_" << board[6][6] <<"_|_" << board[6][7] << "_|_" << board[6][8] <<"_|"<<endl;
cout <<"|_" << board[7][0] << "_|_" <<board[7][1] << "_|_" << board[7][2] << "_|_" << board[7][3] << "_|_" << board[7][4] << "_|_" << board[7][5] << "_|_" << board[7][6] <<"_|_" << board[7][7] << "_|_" << board[7][8] <<"_|"<<endl;
cout <<"|_" << board[8][0] << "_|_" <<board[8][1] << "_|_" << board[8][2] << "_|_" << board[8][3] << "_|_" << board[8][4] << "_|_" << board[8][5] << "_|_" << board[8][6] <<"_|_" << board[8][7] << "_|_" << board[8][8] <<"_|"<<endl;
}







bool isValid(int board[][9], int i, int j, int num, int n){

    // Row check

    for(int x = 0; x < n; x++){
        if(board[i][x] == num){
            return false;
        }
    }

    // Column check

    for(int x = 0; x < n; x++){
        if(board[x][j] == num){
            return false;
        }
    }

    // Submatrix check
    
    int rn = sqrt(n);
    int si = i - i % rn;
    int sj = j - j % rn; 

    for(int x = si; x < si + rn; x++){
        for (int y = sj; y < sj + rn; y++){
            if(board[x][y] == num){
                return false;
            }
        }
    }

    return true;
}

bool SudokuSolver(int board[][9], int i, int j, int n){ // A method for solving Sudoku
// Base Class
if(i == n){
    Print(board,n);
    return true;
}

// If we are not inside the board
if(j == n){
    return SudokuSolver(board, i+1, 0, n);
}

// If cell is already filled -> just move ahead
if(board[i][j] != 0){
    return SudokuSolver(board, i, j+1, n);
}

// We try to fill the cell with an appropiate number

for(int num=1; num <= 9; num++){
    //Check is sum can be filled?
    if(isValid(board, i, j, num, n)){
        board[i][j] = num;
        bool subAns = SudokuSolver(board, i, j+1, n);
            if(subAns){
                return true;
            }
        // Backtracking -> undo the change
            board[i][j] = 0;
        }
    }
    return false;
}

bool Boardfull(int board[][9]){ // This function helps to check if board is full or not
    for(int x = 0; x < 9; x++){
        for(int y = 0; y < 9; y++){
            if(board[x][y] == 0){
                return false;
            }
        }
    }
    return true;
}

bool Comparision(int userboard[][9], int solveBoard[][9]){
    bool is = true;
    cout << ".....Checking your Solution...." << endl;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (userboard[i][j] != solveBoard[i][j]) {
                cout << "Mistake at (" << i + 1 << ", " << j + 1 << "): Expected " << solveBoard[i][j] << " but found " << userboard[i][j] << "." << endl;
                is = false;
            }
        }
    }
    if (is) {
        cout << "Congratulations! You solved the Sudoku correctly! " << endl;
    } 
    else {
        cout << "Some mistakes were found. Try again!" << endl;
    }
    return is;
    
    }
    

void functionOne(int board[][9]){ // A function which helps user to write their digits
    
    int c,r,digit;
    int board1[9][9];
    
    for(int x = 0; x < 9; x++){
        for(int y = 0; y < 9; y++){
            board1[x][y] = board[x][y];
        }
    }
    
    while(Boardfull(board1) == false){
    cout << "Enter the row position(1-9): ";
    cin >> r;
    
    cout << "Enter the column position(1-9): ";
    cin >> c;

    cout << "Enter the digit(1-9): ";
    cin >> digit;
    
    if(digit > 9 or digit < 1){
        cout << "Invalid Digit" << endl;
        cout << "Please try again." << endl;
        continue;
    }

    else{
        if(board1[r-1][c-1] == 0){
        board1[r-1][c-1] = digit;
           Print(board1, 9); 
    }
    
    
    else if(board1[r-1][c-1] != 0){
        cout << "The number already present in sudoku cannot be changed." << endl;
        cout << "Please try again." << endl;
    }
    
}
}


int solveBoard[9][9];
        for(int x = 0; x < 9; x++){
            for(int y = 0; y < 9; y++){
                solveBoard[x][y] = board[x][y];
            }
        }
        SudokuSolver(solveBoard, 0, 0, 9);
        Comparision(board,solveBoard);
    }

int main (){
    int n = 9;
    int j;
    string ans;
    int board[9][9] = { // A board is creted for Sudoku
        {0,0,7,1,0,0,0,6,0},
        {1,0,5,2,0,8,0,0,0},
        {6,0,0,0,0,7,1,2,0},
        {3,1,2,4,0,5,0,0,8},
        {0,0,6,0,9,0,2,0,0},
        {0,0,0,0,0,3,0,0,1},
        {0,0,1,0,0,4,9,8,6},
        {8,0,3,9,0,6,0,0,0},
        {0,6,0,0,8,2,7,0,3},
    }; 
    cout << "The sudoku problem is: " << endl;
    Print(board,n);
    cout<< "Press 1 to play the sudoku game or 2 for sudoku solver: ";
    cin >> j;

    if (j == 1){
        functionOne(board);
        }    

    else if(j == 2){
    SudokuSolver(board, 0,0, n);
    
 return 0;
}
}