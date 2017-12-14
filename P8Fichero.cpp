//FICHEROS
#include<iostream>
#include<fstream>

using namespace std;

int main(){
    //abrimos el fichero
    ofstream fichero ("mifichero.txt");
    fichero<<"En un lugar de La Mancha"<<endl;
    fichero<<"de cuyo nombre no quiero...";
    fichero.close();
    cout<<"Ya esta. Fichero cerrado";
    return 0;
}
