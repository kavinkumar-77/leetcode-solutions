// Last updated: 7/14/2026, 1:54:35 PM
class Solution {
    public int addDigits(int num) {
        if(num==0) return 0;
        if(num%9==0) return 9;
        else return num%9;
    }
}