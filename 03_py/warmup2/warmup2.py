def string_times(str, n):
  return str*n

def front_times(str, n):
  if len(str) < 3:
    word = str
  else:
    word = str[0:3]
  return word*n

def string_bits(str):
  x = 0
  s = ""
  for e in str:
    if x%2 == 0:
      s += e
    x +=1
  return s

def string_splosion(str):
  word = ""
  for e in range(len(str)+1):
    word += str[0:e]
  return word

def last2(str):
  word = str[len(str) - 2:]
  counter = 0
  for a in range(len(str) - 2):
    if word == str[a:a+2]:
      counter += 1
  return counter
  
def array_count9(nums):
  counter = 0
  for e in nums:
    if e == 9:
      counter = counter+1
  return counter
  
def array_front9(nums):
  counter = 0
  for e in nums:
    if counter == 3:
      break
    else:
      if e == 9:
        return True
      counter += 1
  return False
  
def array123(nums):
  for e in range(len(nums) - 2):
    if nums[e] == 1 and nums[e+1] == 2 and nums[e+2] == 3:
      return True
  return False
  
def string_match(a, b):
  counter = 0
  if len(a) > len(b):
    rangez = len(b)
  else:
    rangez = len(a)
  for e in range(rangez-1):
    if a[e:e+2] == b[e:e+2]:
      counter +=1
  return counter