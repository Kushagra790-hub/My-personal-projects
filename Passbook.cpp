#include <iostream>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <algorithm>
using namespace std;

class Bank {
private:
    string name;
    long long int ac;
    int g;
    int pn;
    string eid;
    string sc;
    string choice;

public:
    // Constructor
    Bank(string name, int ac) {
        this->name = name;
        this->ac = ac;
        this->pn = generatePhone();
        this->eid = generateEmail();
        this->sc = generateIFSC();
        this-> choice = getChoice();
    }

    int generatePhone() {
        srand(time(0));
        long long int min = 5678345467, max = 9999999999;
        pn = min + (rand() % (max - min + 1));
        return pn;
    }

    string generateEmail() {
        string email = name;
        transform(email.begin(), email.end(), email.begin(), ::tolower);
        email.erase(remove(email.begin(), email.end(), ' '), email.end());
        srand(time(0));
        int min = 100, max = 900;
        int rn = min + (rand() % (max - min + 1));
        return email + to_string(rn) + "@gmail.com";
    }

    string generateIFSC() {
        srand(time(0));
        int min = 1, max = 9;
        int sc = min + (rand() % (max - min + 1));
        return "KUSH000" +  to_string(sc);
    }

    string getChoice(){
        cout << "Do you want to check balance or withdraw?: " << endl;
        cin >> choice;
        return choice;
    }
    
        
    int BW(){        
        if (choice == "Balance" or choice == "balance" or choice == "BALANCE"){
            srand(time(0));
            int min = 1000, max = 10000;
            g = min + (rand() % (max - min + 1));
            cout << "The balance of your Account No. " << ac << " is: " << g << endl;
        }
        else if(choice == "Withdraw" or choice == "WITHDRAW" or choice == "withdraw"){
            int p;
            srand(time(0));
            int min = 100, max = 900;
            int g = min + (rand() % (max - min + 1));
            cout << "Your current balance is: " << g << endl;
            cout << "Enter the amount you want to withdraw: "<< endl;
            cin >> p;
            if (p > g){
                cout << "Your balance is lower than your withdrawal amount" << endl;
            }
            else{
                int j = g - p; 
                cout << "The remaining balance is: " << j << endl;
            }
        }    
    }
        
    

    void displayPassbook() {
        cout << "_____________________________________________________________" << endl;
        cout << "|                         PASSBOOK                          |" << endl;
        cout << "|       _______________________________________________     |" << endl;
        cout << "|      |                                              |     |" << endl;
        cout << "|      | Name: "<< name  << "                                           " << endl;
        cout << "|      |                                              |     |" << endl;
        cout << "|      | Bank Account Number: " << ac << "                             " << endl;
        cout << "|      |                                              |     |" << endl;
        cout << "|      | Phone Number: " << pn <<  "                     |     |" << endl;
        cout << "|      |                                              |     |" << endl;
        cout << "|      | IFSC CODE: " << sc << "                          |     |" << endl;
        cout << "|      |                                              |     |" << endl;
        cout << "|      | Email ID: " << eid << "                          " << endl;
        cout << "|      |______________________________________________|     |" << endl;
        cout << "|                                                           |" << endl;
        cout << "|___________________________________________________________|" << endl;
    }
    

};

int main() {
    cout << "Welcome to KUSHAGRA Bank" << endl;
    
    string name,name1,name2;
    int ac;
    
    cout << "Enter your first name: " << endl;
    cin >> name1;
    cout << "Enter your surname name: " << endl;
    cin >> name2;
    name = name1 + " " +name2;
    cout << "Enter your full Account number: " << endl;
    cin >> ac;

    Bank customer(name, ac);
    customer.displayPassbook();
    customer.BW();

    return 0;
}    
