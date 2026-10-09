class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums: set = set(nums)
        if len(set_nums) != len(nums):
            return True
        return False


instance = Solution()
my_numbers_1 = [1, 2, 3, 3]
my_numbers_2 = [1, 2, 3, 4]

answer1 = instance.hasDuplicate(my_numbers_1)
answer2 = instance.hasDuplicate(my_numbers_2)
        
print(answer1, answer2)