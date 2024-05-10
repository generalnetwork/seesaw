/*
ASSIGNMENT NO. 5
A book consists of chapters, chapters consist of sections and sections consist of
subsections. Construct a tree and print the nodes. Find the time and space requirements
of your method.
*/

#include <iostream>
using namespace std;
struct Node
{
    string label;
    int count = 0;
    struct Node *child[100];
};
struct Node *root;
class Tree
{
public:
    Tree()
    {
        root = new Node;
        root->label = "";
    }
    void create() // working
    {
        cout << "Enter the name of the Book" << endl;
        cin >> root->label;
        cout << "Enter number of chapters" << endl;
        cin >> root->count;
        for (int i = 0; i < root->count; i++)
        {
            root->child[i] = new Node;
            cout << "enter name of chapter " << i + 1 << endl;
            cin >> root->child[i]->label;
            cout << "enter number of section in chapter " << i + 1 << endl;
            cin >> root->child[i]->count;
            for (int j = 0; j < root->child[i]->count; j++)
            {
                root->child[i]->child[j] = new Node;
                cout << "enter name of section number " << j + 1 << endl;
                cin >> root->child[i]->child[j]->label;
            }
        }
        cout << "tree created" << endl;
    }
    void display()
    {
        cout << "BOOK NAME: " << root->label << endl;
        for (int i = 0; i < root->count; i++)
        {
            cout << " -CHAPTER NAME : " << root->child[i]->label << endl;
            for (int j = 0; j < root->child[i]->count; j++)
            {
                cout << "  -SECTION NAME : " << root->child[i]->child[j]->label << endl;
            }
        }
        cout << "END" << endl;
    }
};

int main()
{
    Tree obj;
    obj.create();
    obj.display();
    return 0;
}