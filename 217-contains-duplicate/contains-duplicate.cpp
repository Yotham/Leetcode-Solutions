class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::set <int> check;
        for(int i = 0; i < nums.size(); i++){
            auto s = check.insert(nums[i]);
            if(s.second == false){
                return true;
            }
        }
        return false;
    }
};