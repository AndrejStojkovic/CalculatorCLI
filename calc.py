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
    return num**(1./2)

def cbrt(num):
    return num**(1./3)

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

def sin(num):
    return math.sin(float(num))

def asin(num):
    return math.asin(float(num))

def cos(num):
    return math.cos(float(num))

def acos(num):
    return math.acos(float(num))

def tan(num):
    return math.tan(float(num))

def atan(num):
    return math.atan(float(num))

def log(nums):
    return math.log(nums[0], nums[1])

def loge(nums):
    return math.log(float(nums))

def log10(nums):
    return math.log(nums, 10)
