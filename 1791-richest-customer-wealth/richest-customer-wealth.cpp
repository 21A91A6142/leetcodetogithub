class Solution {
public:
    int maximumWealth(vector<vector<int>>& a) {
        vector<int>v;
        for(int i=0;i<a.size();i++){
            int c=0;
            for(int j=0;j<a[i].size();j++){
                c+=a[i][j];
            }
            v.push_back(c);
        }
        int k=*max_element(v.begin(),v.end());
        return k;
    }
};