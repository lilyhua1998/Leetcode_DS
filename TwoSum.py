class Solution1:
  #O(n^2)
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

print(Solution1.twoSum(nums=[3,3], target=6))

    class Solution2:
      #O(n), using hash table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable={}
        for i in range(len(nums)):
            hashtable[nums[i]]=i

        for j in range(len(nums)):
            complement=target-nums[j]
            if complement in hashtable and hashtable[complement] != j:
              return [j, hashtable[complement]]

        return None

