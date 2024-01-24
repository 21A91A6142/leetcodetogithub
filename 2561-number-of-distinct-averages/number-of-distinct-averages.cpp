class Solution {
public:
    int distinctAverages(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int i=0,j=nums.size()-1,c=0;
        vector<double>v;
        double ans;
        while(i<=j){
            double avg=(double(nums[i]+nums[j])/2);
            v.push_back(avg);
            i++;
            j--;

        }
        set<double> s(v.begin(),v.end());
        return s.size();
    }
};