def productExceptSelf(nums):
        forward = [0]*len(nums)
        backward = [0]*len(nums)
        
        forward[0] = nums[0]
        backward[len(nums)-1] = nums[len(nums)-1]
        
        # an array of accmulating mult from the beginning
        i = 1
        while i < len(nums):
            forward[i] = nums[i]*forward[i-1]
            i += 1
            
        # an array of accmulating mult from the end
        i = len(nums)-2
        while i >= 0:
            backward[i] = nums[i]*backward[i+1]
            i -= 1
        
        res = [0]*len(nums)
        # first handle the start and end
        
        res[0] = backward[1]
        res[len(nums)-1] = forward[len(nums)-2]
        # handle the middle
        i = 1
        while i < len(nums)-1:
            res[i] = forward[i-1]*backward[i+1]
            i += 1
            
        return res

if __name__ == "__main__":
    print(productExceptSelf([1, 2, 3, 4]))