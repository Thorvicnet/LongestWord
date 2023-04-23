#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <fstream>

using namespace std;

string findIndices(string word) {
    sort(word.begin(), word.end());
    return word;
}

bool anagramCheck(string word1, string word2) {
    return findIndices(word1) == findIndices(word2);
}

vector<string> allPossibleSubset(string arr[], int n) {
    vector<string> subsets;
    int count = pow(2, n);
    for (int i = 0; i < count; i++) {
        string subset = "";
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                subset += arr[j];
            }
        }
        sort(subset.begin(), subset.end());
        do {
            subsets.push_back(subset);
        } while (next_permutation(subset.begin(), subset.end()));
    }
    return subsets;
}

int main()
{
    string letters;
    cout << "Entrez les lettres: ";
    cin >> letters;
    int n = letters.length();
    if (n > 7) {
        cout << "Etes vous sur que vous voulez testez avec " << n << " lettres? (O/N). Vous risquez crasher" << endl;
        char c;
        cin >> c;
        if (c == 'N' || c == 'n') {
            return 1;
        }
        else if (c == 'O' || c == 'o') {
            cout << "Ok, on continue." << endl;
        }
        else {
            cout << "Réponse non valide" << endl;
            return 1;
        }
    }
    string arr[n];
    for (int i = 0; i < n; i++) {
        arr[i] = letters[i];
    }
    vector<string> test = allPossibleSubset(arr, n);
    vector<string> words;
    ifstream file("repertoire_francais_tout.txt");
    string line;
    while (getline(file, line)) {
        words.push_back(line);
    }
    file.close();
    string ans;
    for (const auto & i : test) {
        for (const auto & word : words) {
            if (i == word) {
                if (i.length() > ans.length()) {
                    ans = i;
                }
            }
        }
    }
    cout << "Le mot le plus long est: " << ans << endl;
    return 0;
}