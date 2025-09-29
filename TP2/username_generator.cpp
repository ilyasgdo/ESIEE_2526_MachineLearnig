#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>
using namespace std;

string toLowerCase(string str){
    string res = str;
    transform(res.begin(), res.end(), res.begin(), ::tolower);
    return res;  // Ajout du return manquant
}

bool notcontainanumber(string s){
    for(char c : s){
        if(!isalpha(c)){
            return false;
        }
    }
    return true;
}

int main(){
    string prenom, nom;
    
    // Lire prénom puis nom (selon l'énoncé)
    cin >> prenom;
    cin >> nom;
    
    // Vérifier le prénom
    if(!notcontainanumber(prenom)){
        cout << "\"" << prenom << "\" is not a valid firstname" << endl;
        return 0;
    }
    
    // Vérifier le nom
    if(!notcontainanumber(nom)){
        cout << "\"" << nom << "\" is not a valid lastname" << endl;
        return 0;
    }
    
    // Générer le nom d'utilisateur : 7 premières lettres du nom + initiale du prénom
    string usr = "";
    int len = min(7, (int)nom.length());
    usr += nom.substr(0, len);
    usr += prenom[0];
    
    string res = toLowerCase(usr);
    cout << res << endl;  // Ajout du retour à la ligne
    
    return 0;   
}
