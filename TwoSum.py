# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order. DONE
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
# 2 <= nums.length <= 103
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def twoSum(nums, target):
    answer = nums
    # for x in reversed(answer):
    #     if x > target:
    #         answer.remove(x)
    for i in nums:
        remainder = target - i
        for y in nums:
            if y > i and y == remainder:
                print('[', i, ', ', y, ']', sep='')
                break

# Figure out how to break after getting first working pair. DONE

nums_in = [2, 7, 11, 15]
target_in = 18

twoSum(nums_in, target_in)