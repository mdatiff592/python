# functions and recursion in python 
# functions

def cal_sum(a, b):
    sum = a + b
    print(sum)
    return sum

cal_sum(20, 50) # call function

def print_hello():
    print("hello")

print_hello() 

# wap using function return avg of 3num

def avg_num(a, b, c):
    sum = a + b + c 
    avg = sum /3
    print(avg)
    return avg

# avg_num(98, 97, 95)

# default parameters
def func_name(a = 1, b = 2):
    multi = a * b
    print(multi)
    return multi

func_name()

# lets practice
# waf to print the lenth of a list.(list is the parameters)

cities = ["bihar", "pune", "rajisthan", "mumbai", "kolkata"]
names = ["atif", "alvimehar", "gilnaz", "tiasha ghosh", "naziya", "nagma"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(names)

# waf to print the elements of a list in a single line.(list is the paramenters)

def print_elements(list):
    for items in list:
        print(items, end = " ")

print_elements(names)
print_elements(cities)

# waf to find the fectorial of n.(n is the parameters)

n = 5

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)

# waf to convert USD to INR 

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =", inr_val,"INR")

converter(18)

def check(n):
    if(n%2 != 0):
        print("odd")
    else:
        print("even")

check(19)

# recursion

def show(n):
    if(n == 0):
        return
    print(n)
    show( n-1)

show(5)

# # find factorial using recursion

def fact(n):
    if(n == 0):
        return 1
    return fact(n -1) * n


print(fact(5))

# lets practice 
# write a recursive function to calculate the sun of first n natural num:
def sum(n):
    if(n == 0):
        return 0
    return sum(n -1) + n

print("sum =", sum(5))

# write a recursive function to print all elements in a list 
# [hint : use list and index as parameters]

nums = [1, 4, 56, 78, 234, 89, 213, 78, 213]
indx = 0
def ele(list, indx):
    if(indx == len(list)):
        return 
    print(list[indx])
    ele(list, indx+1)

ele(nums, indx)


