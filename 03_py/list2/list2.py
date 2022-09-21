def count_evens(nums):
  sum = 0
  for e in nums:
    if e % 2 == 0:
      sum += 1
  return sum

def big_diff(nums):
  mins = nums[0]
  maxs = nums[0]
  for e in nums:
    mins = min(mins,e)
    maxs = max(maxs,e)
  return maxs - mins

def centered_average(nums):
  mins = nums[0]
  maxs = nums[0]
  sum = 0
  for e in nums:
    mins = min(mins,e)
    maxs = max(maxs,e)
    sum += e
  sum = sum - mins - maxs
  return sum/(len(nums)-2)

def sum13(nums):
  sum = 0
  for e in range(len(nums)):
    if nums[e] != 13 and (e == 0 or nums[e-1] != 13):
      sum += nums[e]
  return sum

def sum67(nums):
  ignore = False
  sum = 0
  for e in nums:
    if e == 6:
      ignore = True
    if not ignore:
      sum += e
    if e == 7:
      ignore = False
  return sum

def has22(nums):
  for e in range(len(nums) - 1):
    if nums[e] == 2 and nums[e + 1] == 2:
      return True
  return False