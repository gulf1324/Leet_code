#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm> // For sort
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;

        for (string word : strs) {
            string sortedWord = word;
            sort(sortedWord.begin(), sortedWord.end());  // sort ==> makes different words(but anagrams) in the same key
            anagramMap[sortedWord].push_back(word);     //  ex) "eat" and "tea" will have the same sorted key "aet"
        }

        vector<vector<string>> result;
        for (auto& entry : anagramMap) {
            result.push_back(entry.second);  // append only the values (anagram groups) to the result vector
        }

        return result;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<string> strs = {"eat","tea","tan","ate","nat","bat"};
    vector<vector<string>> result = solution.groupAnagrams(strs);
    cout << "Anagram groups : {";

    //show result
    for (size_t i = 0; i < result.size(); ++i) {
        cout << "{";
        for (size_t j = 0; j < result[i].size(); ++j) {
            cout << "\"" << result[i][j] << "\"";
            if (j < result[i].size() - 1) {
                cout << ",";
            }
        }
        cout << "}";
        if (i < result.size() - 1) {
            cout << ",";
        }
    }

    cout << "}" <<endl;
    // >>> {{"bat"},{"tan","nat"},{"eat","tea","ate"}}
    return 0;
}