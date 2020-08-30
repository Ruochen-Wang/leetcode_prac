#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res{""};
        vector<string> one;
        vector<string> two;
        vector<string> three;
        vector<string> four;

        auto append_to_strings = 
            [](vector<string> vec, string c)->vector<string>{
            vector<string> new_vector{};
            for(string s : vec){
                new_vector.push_back(s.append(c));
            }
            return new_vector;
        };

        for(auto c: digits){
            switch (c){
            case '2':
                one = append_to_strings(res, "a");
                two = append_to_strings(res, "b");
                three = append_to_strings(res, "c");
                one.insert(one.end(), two.begin(), two.end());
                one.insert(one.end(), three.begin(), three.end());
                res = one;
                break;
            case '3':
                one = append_to_strings(res, "e");
                two = append_to_strings(res, "d");
                three = append_to_strings(res, "f");
                one.insert(one.end(), two.begin(), two.end());
                one.insert(one.end(), three.begin(), three.end());
                res = one;
                break;
            case '4':
                one = append_to_strings(res, "g");
                two = append_to_strings(res, "h");
                three = append_to_strings(res, "i");
                one.insert(one.end(), two.begin(), two.end());
                one.insert(one.end(), three.begin(), three.end());
                res = one;
                break;
            case '5':
                one = append_to_strings(res, "j");
                two = append_to_strings(res, "k");
                three = append_to_strings(res, "l");
                one.insert(one.end(), two.begin(), two.end());
                one.insert(one.end(), three.begin(), three.end());
                res = one;
                break;
            case '6':
                one = append_to_strings(res, "m");
                two = append_to_strings(res, "n");
                three = append_to_strings(res, "o");
                one.insert(one.end(), two.begin(), two.end());
                one.insert(one.end(), three.begin(), three.end());
                res = one;
                break;
            case '7':
                one = append_to_strings(res, "p");
                two = append_to_strings(res, "q");
                three = append_to_strings(res, "r");
                four = append_to_strings(res, "s");
                one.insert(one.end(), two.begin(), two.end());
                one.insert(one.end(), three.begin(), three.end());
                one.insert(one.end(), four.begin(), four.end());
                res = one;
                break;
            case '8':
                one = append_to_strings(res, "t");
                two = append_to_strings(res, "u");
                three = append_to_strings(res, "v");
                one.insert(one.end(), two.begin(), two.end());
                one.insert(one.end(), three.begin(), three.end());
                res = one;
                break;
            case '9':
                one = append_to_strings(res, "w");
                two = append_to_strings(res, "x");
                three = append_to_strings(res, "y");
                four = append_to_strings(res, "z");
                one.insert(one.end(), two.begin(), two.end());
                one.insert(one.end(), three.begin(), three.end());
                one.insert(one.end(), four.begin(), four.end());
                res = one;
                break;
            //default:
            //    break;
            }
        }
        if(res.size()==1)
            res.clear();
        return res;
    }

};

int main(){
    Solution s;
    string d = "234";
    for(auto res : s.letterCombinations(d)){
        cout << res << " ";
    }
    
    s.letterCombinations(d);
    return 0;
}