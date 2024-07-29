class Solution:
  def twoSum(nums, target):
      for index1,value1 in enumerate(nums):
          #print(f'value1Index={index1}')
          for index2, value2 in enumerate(nums):
              if index2 == index1:
                continue #pass this same value1
              elif value1+value2==target:
                return [index1, index2]
                break
              else:
                continue

print(Solution.twoSum(nums=[3,3], target=6))