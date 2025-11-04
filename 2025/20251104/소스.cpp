//https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/?envType=daily-question&envId=2025-11-04
//3318. Find X-Sum of All K-Long Subarrays I

#include<unordered_map>

class Solution {
public:
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        int n = nums.size();
        //k는 window size
        //window size에 대해 xsum을 찾기
        if (n == 1) { 
            return nums;
        }

        unordered_map<int, int> myMap;
        int left = 0;
        int right = 0;

        while (right < k-1) { 
            if (myMap.contains(nums[right])) { 
                myMap[nums[right]] += 1;
            } else { 
                myMap[nums[right]] = 1;
            }
            right += 1;
        }

        vector<int> answer = {};
        while (right < n) {
            if (myMap.contains(nums[right])) { 
                myMap[nums[right]] += 1;
            } else { 
                myMap[nums[right]] = 1;
            }

            vector<pair<int, int>> vec(myMap.begin(), myMap.end());
            sort(vec.begin(), vec.end(), [](const auto& a, const auto& b) {
                if (a.second != b.second) { 
                    return a.second > b.second;
                } else { 
                    return a.first > b.first;
                }
            });

            vector<pair<int, int>> topElements(vec.begin(), min(vec.end(), vec.begin()+x));
            int sum = 0;
            for (const auto& [key, value]: topElements) { 
                sum += key*value;
            }
            answer.push_back(sum);
            myMap[nums[left]] -= 1;
            left += 1;
            right += 1;
        }
        return answer;
    }
};