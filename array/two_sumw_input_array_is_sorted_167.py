from typing import List

'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            tar = target - numbers[i]
            j = self.search(numbers, tar)
            if j and i != j:
                return [i + 1, j + 1]

    def search(self, numbers, tar):
        begin = 0
        end = len(numbers) - 1
        middle = int((begin + end) / 2)
        while begin != end:
            if tar == numbers[middle]:
                return middle
            if tar > numbers[middle]:
                begin = middle + 1
            else:
                end = middle - 1
        return None


if __name__ == '__main__':
    s = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(numbers, target))
