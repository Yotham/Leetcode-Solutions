class Solution {
public:
    bool isValid(string s) {
        stack<int> stack;
        for(int i = 0; i < s.size(); i++){
            char ch = s[i];
            if(ch == '(' || ch == '{' or ch == '['){stack.push(ch);}
            else{
                if(stack.empty() || (stack.top() == '(' && ch != ')') || (stack.top() == '{' && ch != '}') || (stack.top() == '[' && ch != ']')){return false;}
                stack.pop();
            }
        }
        return stack.empty();
    }
};