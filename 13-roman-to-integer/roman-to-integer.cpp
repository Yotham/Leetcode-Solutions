class Solution {
public:
    int romanToInt(string s) {
        int sum = 0;
        int i = 0;
        while(i<s.size()){
            if(s[i] == 'I' && s[i+1] != 'V' && s[i+1] != 'X'){
                sum+=1;
                i++;
            };
            if(s[i] == 'I' && s[i+1] == 'V'){
                sum+=4;
                i+=2;
            };
            if(s[i] == 'I' && s[i+1] == 'X'){
                sum+=9;
                i+=2;
            };
            if(s[i] == 'V'){
                sum+=5;
                i++;
            };
            if(s[i] == 'X' && s[i+1] != 'L' && s[i+1] != 'C'){
                sum+=10;
                i++;
            };
            if(s[i] == 'X' && s[i+1] == 'L'){
                sum+=40;
                i+=2;
            };
            if(s[i] == 'X' && s[i+1] == 'C'){
                sum+=90;
                i+=2;
            };
            if(s[i] == 'C' && s[i+1] != 'D' && s[i+1] != 'M'){
                sum+=100;
                i++;
            };
            if(s[i] == 'C' && s[i+1] == 'D'){
                sum+=400;
                i+=2;
            };
            if(s[i] == 'C' && s[i+1] == 'M'){
                sum+=900;
                i+=2;
            };
            if(s[i] == 'L'){
                sum+=50;
                i++;
            };
            if(s[i] == 'D'){
                sum+=500;
                i++;
            };
            if(s[i] == 'M'){
                sum+=1000;
                i++;
            };
        };
        return sum;
    };
};