class Solution {
    public void sortColors(int[] nums) {
        int [] arr = new int[3];
        for(int num : nums){
            arr[num]++;
        }  

        int ind = 0;
        for(int i = 0; i<3 ;i++){
            for(int j = 0;j<arr[i];j++){
                nums[ind++] = i; 
            }
        }
    }
}
