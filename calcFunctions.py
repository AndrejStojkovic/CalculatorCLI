import math

def add(nums):
    r = 0
    for num in nums:
        r = r + num
    return r

def sub(nums):
    r = nums[0]
    nums.pop(0)
    for num in nums:
        r = r - num
    return r

def mul(nums):
    r = 1
    for num in nums:
        r = r * num  
    return r

def div(nums):
    r = nums[0]
    nums.pop(0)
    for num in nums:
        r = r / num
    return r

def sqrt(num):
    return num[0]**(1./2)

def cbrt(num):
    return num[0]**(1./3)

def pow(nums):
    return nums[0] ** nums[1]

def avg(nums):
    r = add(nums)
    r = r / len(nums)
    return r

def abs(nums):
    i = 0
    for i in range(0, len(nums)):
        if nums[i] < 0:
            nums[i] = -nums[i]
    return nums

def sin(nums):
    return math.sin(float(nums[0]))

def asin(nums):
    return math.asin(float(nums[0]))

def cos(nums):
    return math.cos(float(nums[0]))

def acos(nums):
    return math.acos(float(nums[0]))

def tan(nums):
    return math.tan(float(nums[0]))

def atan(nums):
    return math.atan(float(nums[0]))

def log(nums):
    return math.log(nums[0], nums[1])

def loge(nums):
    return math.log(nums[0])

def log10(nums):
    return math.log(nums[0], 10)
