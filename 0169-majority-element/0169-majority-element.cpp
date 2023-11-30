class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        set<int> checked;
        int n = nums.size();
        bool checking = true;
        while (checking) {
            int check = nums[rand() % n];
            while (checked.contains(check)){
                check = nums[rand() % n];
            }

            int count = 0;
            for (int i = 0; i < n; i++){
                if (check == nums[i]){
                    count += 1;
                }
            }

            if (count > n / 2){
                checking = false;
                return check;
            } else {
                checked.insert(check);
            }

        }
        return -1;
    }
};