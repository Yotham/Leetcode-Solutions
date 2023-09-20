class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string str="";
        string initial = strs[0];
        for(int j=0;j<initial.size();j++)
        {
            int i=1;
            for(i;i<strs.size();i++)
            {
                if(initial[j]!=strs[i][j])
                    break;
            }
            if(i==strs.size()){
                str+=initial[j];
            }
            else
                break;
        }
        return str;
    }
};