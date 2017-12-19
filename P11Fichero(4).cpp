//Leer líneas
#include<iostream>
#include<fstream>

using namespace std;

int main(){
    ifstream fichero("mifichero.txt");
    string mensaje;
    int salir;
    for(int nlinea=1;nlinea<=4;nlinea++){
            getline(fichero,mensaje);
            cout<<mensaje;
            cout<<endl;
            }
    cin>>salir;
}
