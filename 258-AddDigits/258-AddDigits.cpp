// Last updated: 7/14/2026, 1:54:30 PM
class Solution {
public:
    int addDigits(int num) {
        if(num==0)
            return 0;
        else 
            return 1+(num-1)%9;
    }
};