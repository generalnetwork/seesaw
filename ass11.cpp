/*
ASSIGNMENT 11 - sequential file organization
Department maintains student information. The file contains roll number, name,
division and address. Allow users to add, delete information about students.
Display information of a particular employee. If the record of the student does
not exist an appropriate message is displayed. If it is, then the system displays
the student details. Use a sequential file to maintain the data.
*/

#include <iostream>
#include <fstream>
using namespace std;
class student
{
public:
    int rollno;
    char div;
    bool flag;
    char name[20];
    char addr[20];
    void getdata();
    void display_data();
    int return_rno();
};
void student::getdata()
{
    cout << "Enter roll number: ";
    cin >> rollno;
    cout << "Enter name: ";
    cin >> name;
    cout << "Enter division: ";
    cin >> div;
    cout << "Enter address: ";
    cin >> addr;
}
void student::display_data()
{
    cout << "\nRoll Number: " << rollno << endl;
    cout << "Name: " << name << endl;
    cout << "Division: " << div << endl;
    cout << "Address: " << addr << endl;
}
int student::return_rno()
{
    return rollno;
}
void write_rec()
{
    ofstream fobj;
    fobj.open("Info.txt", ios::app);
    student s1;
    s1.getdata();
    fobj.write((char *)&s1, sizeof(s1));
    fobj.close();
    cout << "Record written successfully." << endl;
}
void display_rec()
{
    ifstream f1;
    f1.open("Info.txt");
    student s1;
    while (f1.read((char *)&s1, sizeof(s1)))
        s1.display_data();
    f1.close();
}
void search_rec()
{
    int rno;
    cout << "\nEnter rollno to be searched: ";
    cin >> rno;
    ifstream f1;
    f1.open("Info.txt", ios::in);
    student s1;
    while (f1.read((char *)&s1, sizeof(s1)))
    {
        if (s1.return_rno() == rno)
        {
            s1.flag = true;
            s1.display_data();
            f1.close();
            return;
        }
    }
    f1.close();
    if (s1.flag == false)
        cout << "Data not found" << endl;
}
void delete_rec()
{
    student s1;
    int r1no;
    cout << "\nEnter rollno to be deleted: ";
    cin >> r1no;
    ifstream f1;
    ofstream f2;
    f1.open("Info.txt", ios::in);
    f2.open("temp.txt", ios::out);
    f1.read((char *)&s1, sizeof(s1));
    while (!f1.eof())
    {
        if (s1.return_rno() != r1no)
            f2.write((char *)&s1, sizeof(s1));
        f1.read((char *)&s1, sizeof(s1));
    }
    cout << "Record with rollno " << r1no << " has been deleted" << endl;
    f1.close();
    f2.close();
    remove("Info.txt");
    rename("temp.txt", "Info.txt");
}
int main()
{
    int choice = 0;
    while (choice != 5)
    {
        cout << "-------------------------------------" << endl;
        cout << "Direct Access File Menu:" << endl;
        cout << "1. Write Record" << endl;
        cout << "2. Display Records" << endl;
        cout << "3. Search Record" << endl;
        cout << "4. Delete Record" << endl;
        cout << "5. Quit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            write_rec();
            break;
        case 2:
            display_rec();
            break;
        case 3:
            search_rec();
            break;
        case 4:
            delete_rec();
            break;
        case 5:
            cout << "Quitting..." << endl;
            break;
        default:
            cout << "Invalid choice. Please try again." << endl;
            break;
        }
    }
    return 0;
}
