def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6
 
def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[len(nums) -1]

def make_pi():
  pi = [3, 1, 4]
  return pi
 
def common_end(a, b):
  return a[0] == b[0] or a[len(a) -1] == b[len(b) - 1]

def sum3(nums):
  counter = 0
  for e in nums:
    counter += e
  return counter
 
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

def reverse3(nums):
  return [nums[2],nums[1],nums[0]]

def max_end3(nums):
  a = nums[0]
  if nums[0] < nums[2]:
    a = nums[2]
  return [a,a,a]

def sum2(nums):
  index = 0
  sum = 0
  for e in nums:
    if index < 2:
      sum = sum + e
    index = index + 1
  return sum

def middle_way(a, b):
  return [a[1],b[1]]

def make_ends(nums):
  return [nums[0],nums[len(nums) -1]]

def has23(nums):
  for e in nums:
    if e == 2 or e == 3:
      return True
  return False
  