#include <iostream>
using namespace std;

int main() {
    string input,old_password = "oldpass",new_password;
    int attempts=0;
    
    while (true) {
        cout << "Old password: ";
        cin >> input;
        
        if (input == old_password && attempts !=  3) {
            cout << "Password matched!\n";
            cout << "New password: ";
            cin >> new_password;
            
            if (new_password != old_password) {
               old_password = new_password;
               cout << "Password changed succesfully!\n";
               attempts = 0;
            }
            }
        else if (attempts == 2) {
            cout << "Attempts reached, Exiting....";
            break;
        }
        else {
            attempts += 1;
            cout << "Attempts: " + to_string(attempts)+ "\n";
            cout << "Invalid password, try again!\n";
        }
    }
}
