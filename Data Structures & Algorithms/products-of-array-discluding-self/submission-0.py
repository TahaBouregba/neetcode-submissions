class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prd = 1
        for i in range (len(nums)):
            prefix[i]=prd
            prd *= nums[i]
        

        postfix= [1] * len(nums)
        prod = 1
        for i in range (len(nums)-1,-1,-1):
            postfix[i]=prod
            prod *= nums[i]
        result = [1] * len(nums)
        prodi = 1
        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]

        return result

        
