class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        vector<int>v;
        int s=0;
        double ans,l;
        for(int i=0;i<k;i++){
            s+=nums[i];
        }
        v.push_back(s);
        for(int i=k;i<nums.size();i++){
            s+=(nums[i]-nums[i-k]);
            v.push_back(s);
        }
        l=*max_element(v.begin(),v.end());
        ans=l/k;
        return ans;
    }
};