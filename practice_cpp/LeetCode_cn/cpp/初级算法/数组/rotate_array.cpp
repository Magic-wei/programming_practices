/* 'Questions: 
	将包含 n 个元素的数组向右旋转 k 步。
	例如，如果  n = 7 ,  k = 3，给定数组  [1,2,3,4,5,6,7]  ，向右旋转后的结果为 [5,6,7,1,2,3,4]。

	注意:
	尽可能找到更多的解决方案，这里最少有三种不同的方法解决这个问题。

	提示:
	要求空间复杂度为 O(1)
*/

// my solution one: time cost is 376 ms
class Solution_Mine_One {
public:
    void rotate(vector<int>& nums, int k) {
        assert(nums.size()>0);
        k = k%nums.size();
        int tmp;
        for(int j=0;j<k;j++) {
            tmp = nums[nums.size()-1];
            for(int i=nums.size()-1;i>0;i--) {
                nums[i] = nums[i-1];
            }
        }
    }
};

// The best solution: time cost is 16 ms
class Solution_Best_1 {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.empty() || (k %= nums.size()) == 0) return;
        int n = nums.size();
        reverse(nums.begin(), nums.begin() + n - k);
        reverse(nums.begin() + n - k, nums.end());
        reverse(nums.begin(), nums.end());
    }
};

class Solution_Best_2 {
public:
    void inverse(vector<int>& nums, int i, int j)
    {
        int temp;
        while(i<j)
        {
            temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
            i++;
            j--;
        }
    }
    void rotate(vector<int>& nums, int k) {
        int the_size = nums.size();
        k=k%the_size;
        inverse(nums,0,the_size-k-1);
        inverse(nums,the_size-k,the_size-1);
        inverse(nums,0,the_size-1);
    }
};

// 空间换时间的方法： time cost is 20 ms
class Solution_MoreSpace {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> t = nums;
        for (int i = 0; i < nums.size(); ++i) {
            nums[(i + k) % nums.size()] = t[i];
        }
    }
};
