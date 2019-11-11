from typing import List

'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

'''


class Solution:

    def __init__(self, nums: List[int]):
        self.origin = list(nums)
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = list(self.origin)
        self.origin = list(self.nums)
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        random.shuffle(self.nums)
        # for i in range(len(self.nums)):
        #     j = random.randrange(i, len(self.nums))
        #     self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# 这题ac不是靠shuffle,是靠reset,保证深拷贝
nums = [1, 2, 3]
obj = Solution(nums)
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
