// Last updated: 7/14/2026, 1:54:27 PM
// LeetCode 292 - Nim Game
class Solution {
    public boolean canWinNim(int n) {
        // If n is a multiple of 4, first player loses.
        return n % 4 != 0;
    }
}