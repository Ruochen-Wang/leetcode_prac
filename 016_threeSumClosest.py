from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    closest = nums[0]+nums[1]+nums[2]
    for first in range(len(nums)-2):
        second = first+1
        third = len(nums)-1
        while second < third:
            curr_comb = nums[first] + nums[second] + nums[third]
            closest = curr_comb if (abs(curr_comb-target)) < (abs(closest-target)) else closest
            if curr_comb > target:
                third -= 1
            elif curr_comb < target:
                second += 1
            else:
                return curr_comb
    return closest


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 19
    print(threeSumClosest(nums, target))