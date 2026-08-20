class Solution {
public:
    int maxArea(vector<int>& height) {
        int left=0;
        int right=height.size()-1;
        int Max_area=0;
        while(left<right){
            int area=min(height[left], height[right])*(right-left);
            Max_area=max(Max_area,area);
            if(height[right]>height[left]){
                left++;
            }
            else{
                right--;
            }
        }
        return Max_area;
    }
};