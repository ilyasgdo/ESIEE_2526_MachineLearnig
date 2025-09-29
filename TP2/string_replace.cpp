#include <iostream>
#include <string>
using namespace std;

// Fonction pour remplacer la première occurrence de 'oldWord' par 'newWord' dans 'text'
string replace(const string& text, const string& oldWord, const string& newWord) {
    // Trouver la position de la première occurrence de oldWord
    size_t pos = text.find(oldWord);
    
    // Si oldWord n'est pas trouvé, retourner le texte original
    if (pos == string::npos) {
        return text;
    }
    
    // Créer une nouvelle chaîne avec le remplacement
    string result = text;
    result.replace(pos, oldWord.length(), newWord);
    
    return result;
}

int main() {
    // Tests avec les exemples fournis
    cout << "Test 1: replace(\"Bonjour Monsieur\", \"Monsieur\", \"Madame\")" << endl;
    cout << "Résultat: \"" << replace("Bonjour Monsieur", "Monsieur", "Madame") << "\"" << endl;
    cout << "Attendu: \"Bonjour Madame\"" << endl << endl;
    
    cout << "Test 2: replace(\"Bonjour Monsieur\", \"Patron\", \"Madame\")" << endl;
    cout << "Résultat: \"" << replace("Bonjour Monsieur", "Patron", "Madame") << "\"" << endl;
    cout << "Attendu: \"Bonjour Monsieur\"" << endl << endl;
    
    cout << "Test 3: replace(\"Bonjour Mr X et Mr Y\", \"Mr\", \"Mme\")" << endl;
    cout << "Résultat: \"" << replace("Bonjour Mr X et Mr Y", "Mr", "Mme") << "\"" << endl;
    cout << "Attendu: \"Bonjour Mme X et Mr Y\"" << endl << endl;
    
    // Test interactif
    string text, oldWord, newWord;
    cout << "=== Test interactif ===" << endl;
    cout << "Entrez le texte: ";
    getline(cin, text);
    cout << "Entrez le mot à remplacer: ";
    getline(cin, oldWord);
    cout << "Entrez le nouveau mot: ";
    getline(cin, newWord);
    
    string result = replace(text, oldWord, newWord);
    cout << "Résultat: \"" << result << "\"" << endl;
    
    return 0;
}