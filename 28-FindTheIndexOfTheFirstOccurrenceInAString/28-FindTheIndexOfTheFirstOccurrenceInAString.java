// Last updated: 7/14/2026, 1:54:51 PM
class Solution {
    public int strStr(String h, String needle) {
        for(int i=0;i<h.length()-needle.length()+1;i++){
            if(h.charAt(i)==needle.charAt(0)){
                if(h.substring(i,needle.length()+i).equals(needle)){
                    return i;
                }
            }
                
        }
        return -1;
    }
}