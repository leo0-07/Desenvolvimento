#include <iostream>
#include <string>
using namespace std;

class caractere{
// Definição - Declaração - Dimensionamento da classe.
private:
// Declaração dos membros de dados privados...
string mysemivogais[2] = {"i", "u"};
string myvogais[3] = {"a", "e", "o"};
string consoantes[19] = {"b", "c", "d","f","g","j","k","l", "m","n","p", "q", "r", "s", "t","v", "w", "x", "z"};
string outros = "h";
public:
// Declaração dos membros de dados públicos
int get_vogais() {cout << "as vogais são:"<< myvogais[0] << " - " <<myvogais[1] << " - " << myvogais[2] << endl;return 0;}
int get_semivogais(){cout << "as semivogais são:"  << mysemivogais[0] << " - " << mysemivogais[1] << endl;return 0;}
int get_consoantes() {int i=0;cout << "as consoantes são:";for(i=0;i<19;i++){cout << " - " << consoantes[i];}cout << endl;return 0;}
int  get_silabas_vogais()  {int i=0;for (i=0;i<19;i++){cout<<"consoante + vogal:"<< consoantes[i]<< endl;cout << "consoante + vogal:"<< consoantes[i] << myvogais[0] << " - " << consoantes[i] << myvogais[1] << " - "<< consoantes[i] << myvogais[2] << endl;}return 0;}
int get_silabas_semivogais() {int i=0;for (i=0;i<19;i++){cout << "consoantes + semivogais:" << consoantes[i] << endl;cout << consoantes[i] << mysemivogais[0] << " - " << consoantes[i] << mysemivogais[1] << endl;}return 0;}
int get_outros() {cout << "\n outras letras são:" << outros << endl;return 0;}
int show_menu(){ cout << "mostrar vogais - 0" << endl;cout <<  "mostrar consoantes - 1" << endl;cout << "mostrar semivogais - 2" << endl;cout << "mostrar sílabas com vogais - 3" << endl;cout << "motrar sílabas  om semivogais - 4" << endl;cout << "motrar outros caracteres - 5" << endl;return 0;}
};

int main() {
cout << "inicializando..." << endl;
caractere leo;
leo.show_menu();
int op;
cin >> op;
if (op==0){
leo.get_vogais();
};
if (op==1){
leo.get_consoantes();
};
if (op==2){
leo.get_semivogais();
};
if (op==3){
//leo.get_outros();
leo.get_silabas_vogais();
};
if (op==4) {
leo.get_silabas_semivogais();
};
if (op==5) {
leo.get_outros();
};
return 0;
}

