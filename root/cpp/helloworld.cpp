#include <iostream>
#include <vector>
#include <string>
#include "TH1F.h"
#include "TTree.h"

using namespace std;

int main()
{
    TTree *T = new TTree("test", "test");
    T->Print();
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}
