//Leer l�neas
#include<iostream>
#include<fstream>

using namespace std;

int main(){
    ifstream fichero("mifichero.txt");
    string mensaje;
    int salir;
    getline(fichero,mensaje);
    cout<<"La primera linea diche: ";
    cout<<mensaje;
    cin>>salir;
    }
