class Solution {
public:
    int countPairs(vector<int>& n, int t) {
        sort(n.begin(),n.end());
        int i=0,j=n.size()-1;
        int c=0;
        while(i<j){
            if(n[i]+n[j]<t){
                c+=j-i;
                i++;
            }
            else if(n[i]+n[j]>=t){
                j--;
            }
            else{
                i++;
            }
        }
        return c;
    }
};