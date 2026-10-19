class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #boyer moore extended to 2 candidates
        if len(nums)==1:
            return nums.copy()
        cnt1 = 0
        cnt2 = 0
        num1 = -1
        num2 = -1
        res = []
        
        for i in range(len(nums)):
            if nums[i]==num1:
                cnt1+=1
            elif nums[i]==num2:
                cnt2+=1
            elif cnt1==0:
                num1 = nums[i]
                cnt1 = 1
            elif cnt2==0:
                num2 = nums[i]
                cnt2 = 1
            else:
                cnt1-=1
                cnt2-=1
        cnt1 = cnt2 = 0
        for num in nums:
            if num==num1:
                cnt1+=1
            elif num==num2:
                cnt2+=1
        if cnt1>len(nums)//3:
            res.append(num1)
        if cnt2>len(nums)//3:
            res.append(num2)
        return res