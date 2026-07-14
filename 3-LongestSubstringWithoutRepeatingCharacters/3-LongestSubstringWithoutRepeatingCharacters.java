// Last updated: 7/14/2026, 1:55:03 PM
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left=0;
        int max_len=0;
        Set<Character> set=new HashSet<>();
        for(int right=0;right<s.length();right++){
            char c=s.charAt(right);
            while(set.contains(c)){
                set.remove(s.charAt(left));
                left++;
            }
            set.add(c);
            int current_len=right-left+1;
            max_len=Math.max(max_len,current_len);
        }
        return max_len;
    }
}