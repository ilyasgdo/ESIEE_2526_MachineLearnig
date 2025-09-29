#include <iostream>
#include <string>
using namespace std;

// Fonction pour compter les occurrences de 'word' dans 'text'
int count(const string& word, const string& text) {
    int occurrences = 0;
    size_t pos = 0;
    
    // Utiliser find pour chercher toutes les occurrences
    while ((pos = text.find(word, pos)) != string::npos) {
        occurrences++;
        pos += word.length(); // Avancer la position pour éviter les chevauchements
    }
    
    return occurrences;
}

int main() {
    // Tests avec les exemples fournis
    cout << "Test 1: count(\"Hello\", \"Hello world\") = " << count("Hello", "Hello world") << endl;
    cout << "Test 2: count(\"hello\", \"Hello world\") = " << count("hello", "Hello world") << endl;
    cout << "Test 3: count(\"o\", \"Hello world\") = " << count("o", "Hello world") << endl;
    
    // Test interactif
    string word, text;
    cout << "\nEntrez le mot à chercher: ";
    cin >> word;
    cin.ignore(); // Ignorer le retour à la ligne après cin
    cout << "Entrez le texte: ";
    getline(cin, text);
    
    int result = count(word, text);
    cout << "Nombre d'occurrences de \"" << word << "\" dans \"" << text << "\": " << result << endl;
    
    return 0;
}