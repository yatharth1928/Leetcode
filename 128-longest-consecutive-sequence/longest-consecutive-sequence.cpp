class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n=nums.size();
        unordered_set<int>st;
        if(n==0)return 0;
        int maxi=0;
        int count=1;
        for(int i=0;i<n;i++){
            st.insert(nums[i]);
        }
    
        for(auto it:st){
            if(st.find(it-1)==st.end()){
                count=1;
                int x=it;

                while(st.find(x+1)!=st.end()){
                    x++;
                    count++;
                }
                maxi=max(count,maxi);
            }
        }
        return maxi;

    }
};