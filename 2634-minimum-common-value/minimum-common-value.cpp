class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int i=0,j=0;
        int k=nums1.size(),l=nums2.size();
        while(i<k and j<l){
            if(nums1[i]==nums2[j]){
                return nums1[i];
            }
            else if(nums1[i]<nums2[j]){
                i=i+1;
            }
            else{
                j=j+1;
            }
        }
        return -1;
    }
};