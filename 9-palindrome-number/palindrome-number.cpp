class Solution {
public:
    bool isPalindrome(int x) {
        int r;
        long sum = 0;
        int check = x;
        if(x < 0){
            return false;
        }
        while(x > 0){
            r = x%10;
            sum = (sum*10)+r;
            x = x/10;
        }   
        if(check == sum){
            return true;
        }
        return false;
    }
};