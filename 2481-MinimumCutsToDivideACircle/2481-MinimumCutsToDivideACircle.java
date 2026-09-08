// Last updated: 9/8/2026, 1:40:07 PM
class Solution {
    public int numberOfCuts(int n) {
        if(n==1) return 0;
        if(n%2==0) return n/2;
        else return n;
    }
}