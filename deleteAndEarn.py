# You are given an integer array nums. You want to maximize the number of points you get by performing the 
# following operation any number of times:
#   Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete 
#   every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # For this problem, we want to do some preprocessing steps
        # First, we want to sum up the total points for each number
        sums = defaultdict(int)
        for i in range(len(nums)):
            sums[nums[i]] += nums[i]
        # Then, we want to loop through the sorted keys of sums
        sorted_nums = sorted(list(sums.keys()))
        if len(sorted_nums) == 1:
            return sums[sorted_nums[0]]
        # Now we need to define our dynamic programming definition of how to solve this problem
        # let sn represent sorted_nums
        # dp(i) = max points for the ith number
        # dp(sn) = sums[0]
        # For this problem, the solution would be equal to dp(n) where n is the largest number
        memo = [0] * len(sorted_nums)
        memo[0] = sums[sorted_nums[0]]
        memo[1] = max(memo[0], memo[0] - sums[sorted_nums[1] - 1] + sums[sorted_nums[1]])
        # Now that we have our base case, we can build up number by number
        # At each step, we need to see if this nuber is worth choosing.
        # We do this by comparing sums[i] with sums[i - 1].
        # if memo[i-1] - sums[i - 1] + sums[i] > memo[i-1] then we update, otherwise carry over
        # only compare if sn[i - 1] + 1 == sn[i]
        for i in range(2, len(sorted_nums)):
            cur = sorted_nums[i]
            prev = sorted_nums[i - 1]
            if prev + 1 == cur:
                memo[i] = max(memo[i - 2] + sums[cur], memo[i - 1])
            else:
                memo[i] = memo[i - 1] + sums[cur]
        return memo[len(memo) - 1]