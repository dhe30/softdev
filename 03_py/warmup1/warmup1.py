def sleep_in(weekday, vacation):
  if not weekday:
    return True
  if vacation:
    return True
  return False

def diff21(n):
  if n > 21:
    return 2*(n-21)
  return 21-n

def near_hundred(n):
  if abs(100-n) <= 10 or abs(200-n) <= 10:
    return True
  return False
  
def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else:
    return a < 0 and b > 0 or b < 0 and a > 0

def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]

def front_back(str):
  if len(str) >= 2:
    return str[len(str)-1] + str[1:len(str)-1] + str[0]
  return str

def monkey_trouble(a_smile, b_smile):
  return a_smile and b_smile or not a_smile and not b_smile
  
 def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True;
  return False;

def makes10(a, b):
  return (a == 10) or (b == 10) or (a+b == 10)

def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  return a+b

def not_string(str):
  if str[0:3] == 'not':
    return str
  return 'not ' + str

def front3(str):
  if len(str) < 3:
    word = str
  else:
    word = str[0:3]
  return word + word + word