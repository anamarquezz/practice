"""
Method 1:
Solution based on Narsimha karumanchi's 
Dynamic Programming 
-----------------------------
Time Complexity: O(n^2)
Space Complexity: O(n)
------------------------------
"""
from typing import List
class Solution:
    def lengthOfList(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = 1
        dp=[1]*len(nums)
        print("dp:",dp)
        for i in range (len(nums)):
            for j in range (0,i):
               # print("-----------------")
               # print("------- %s:- %s:------",(i, j))
               # print("-----------------")
               # print("nums[i]: ", nums[i])
               # print("nums[j]: ", nums[j] )
               # print("dp[i]: ", dp[j])
               # print("dp[j] + 1: ", dp[j] + 1)
                if nums[i]>nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                #    print(" dp[i]: ",  dp[i])
                max_len = max(max_len, dp[i])
               # print("max_len ",max_len)
        return max_len

'''
        dp = []
        if not A:
            return 0
        if len(A) in range(1,2501):
            if len(A) == 1:
                    return 1
            max_len = 1
            print("dp", dp)
            dp[1] * len(A)
            for i in range (len(A)):              
                for j in range (0, i):
                    if A[i]>A[j] and dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                    max_len = max(max_len, dp[i])
            return max_len
'''

if __name__ == "__main__":
    s = Solution()
    s.lengthOfList([ 84, 80, 27 ])