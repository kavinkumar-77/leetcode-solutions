// Last updated: 7/14/2026, 1:55:07 PM
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numMap = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int complement=target-nums[i];
            if(numMap.containsKey(complement)){
                return new int[]{numMap.get(complement),i};
            }
            numMap.put(nums[i],i);
        }
        return new int[]{};
    }
}