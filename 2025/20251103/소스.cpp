
//https://leetcode.com/problems/minimum-time-to-make-rope-colorful/?envType=daily-question&envId=2025-11-03
//1578. Minimum Time to Make Rope Colorful
#include<iostream>

class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        //최소 비용으로 제거하기
        //연속된 array를 찾기 => max value 남기고 나머지를 다 삭제
        //바로 직전 것과 비교만 하면 됨
        int right = 0;
        char prev = ' ';
        int currSum = 0;
        int maxVal = 0;
        int cost = 0;
        int n = colors.size();
        while (right < n) { 
            if (colors[right] == prev) { 
                currSum += neededTime[right];
                maxVal = max(maxVal, neededTime[right]);
            } else { 
                prev = colors[right];
                cost += currSum - maxVal;
                maxVal = neededTime[right];
                currSum = neededTime[right];
            }
            right += 1;
        }
        cost += currSum - maxVal;
        return cost;
    }
};