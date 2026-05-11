class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            prod = 1

            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]

            result.append(prod)

        return result

  ## This problem makes it so that you can not have the current ith element in the product, it always excludes i. 
  ## So for example if we have {1.2.4.6} as input, let i = 0. We would have result[i] = 2 * 4 * 6 = 48, and we do that for each element in the array 
