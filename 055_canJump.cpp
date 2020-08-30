#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int i, required_jump_len = 0;
        bool can;
        /*loop through the array reversely and count the
          the required jump size*/
        for(i=nums.size()-2; i >= 0; i--){
            if(nums[i] > required_jump_len){
                required_jump_len=0;
            }
            else{
                required_jump_len += 1;
            }
        }
        if(required_jump_len==0){
            return true;
        }
        else{
            return false;
        }
    }
};

int main(){
    vector<int> arr{3,2,1,0,4};
    Solution s;
    cout << s.canJump(arr);
    return 0;
}