class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        nums.sort()
        mini = float(inf)
        for i in range(1,5):   
            mini = min(mini,(nums[n-i]-nums[4-i]))
            
        return mini

    """ Overall, the code is well-written and easy to understand. 
    One suggestion for improvement would be to add comments to explain what each part of the code does.
    This would make it easier for others to understand the code and its purpose.
    
    Overall, good job! Keep up the good work! """
