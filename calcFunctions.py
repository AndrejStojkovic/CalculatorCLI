import math

def add(nums):
    r = 0
    for num in nums:
        r = r + num
    print(r)

def sub(nums):
    r = nums[0]
    nums.pop(0)
    for num in nums:
        r = r - num
    print(r)

def mul(nums):
    r = 1
    for num in nums:
        r = r * num  
    print(r)

def div(nums):
    r = nums[0]
    nums.pop(0)
    for num in nums:
        r = r / num
    print(r)

def sqrt(num):
    print(num**(1./2))

def cbrt(num):
    print(num**(1./3))

def pow(nums):
    print(nums[0] ** nums[1])

def avg(nums):
    r = add(nums)
    r = r / len(nums)
    print(r)

def abs(nums):
    i = 0
    for i in range(0, len(nums)):
        if nums[i] < 0:
            nums[i] = -nums[i]
    print(nums)

def sin(num):
    print(math.sin(float(num)))

def asin(num):
    print(math.asin(float(num)))

def cos(num):
    print(math.cos(float(num)))

def acos(num):
    print(math.acos(float(num)))

def tan(num):
    print(math.tan(float(num)))

def atan(num):
    print(math.atan(float(num)))

def log(nums):
    print(math.log(nums[0], nums[1]))

def loge(nums):
    print(math.log(float(nums)))

def log10(nums):
    print(math.log(nums, 10))
