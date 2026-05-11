#loops
# while loops

count = 1
while count <= 5:
    print("hello")
    count += 1

print(count)

i  = 1
while i <= 5:
    print(i)
    i += 1

a = 5
while a >=  1:
    print(a)
    a -= 1

# lets practice 
# print 1 to 100

starting_num = 1
while starting_num <= 100:
    print(starting_num)
    starting_num += 1
    

# print 100 to 1

start = 100
while start >=1:
    print(start)
    start -= 1

# print multiplication table 5
n = int(input("enter number :"))
i = 1
while i <= 10:
    print(n*i)
    i += 1

# print elements of the following list using a loop:
nums = [ 1, 4, 16, 25, 36, 49, 64, 81, 100]

indx = 0
while indx < len(nums):
    print(nums[indx])
    indx += 1

heroes = ["thor", "captain", "spider", "ant", "thanos", "iron"]
i = 0
while i < len(heroes):
    print(heroes[i])
    i += 1

# search for a num x in this tuple using loop:
nums = ( 1, 4, 16, 25, 36, 49, 64, 81, 100)

x = 64
indx = 0
while indx < len(nums):
    if(nums[indx] == x):
        print("found index", indx)
    indx += 1

# break and continue
# break:

i = 1
while i <= 5:
    print (i)
    if(i == 3):
        break
    i += 1

nums = ( 1, 4, 16, 25, 36, 49, 64, 81, 100)

x = 64
indx = 0
while indx < len(nums):
    if(nums[indx] == x):
        print("found index", indx)
        break
    else:
        print("finding..")
    indx += 1

# continue 

i = 0
while i <= 10:
    if(i == 8):
        i +=1
        continue
        print(i)
        i += 1

aa = 1
while aa <= 10:
    if(aa%2 != 0):
        aa += 1
        continue
    print(aa)
    aa += 1

# for loop

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["akaash", "faizan", "sufiyaan", "rahman", "yaseen", "afzal"]

for val in nums:
    print(val)

for val2 in names:
    print(val2)

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

for num in tup:
    print(num)

str = "i am the devil of my world"

for num in str:
    print(num)

for val in str:
    if(val == "o"):
        print("o found")
        break
    print(val)
    
else:
      print("lost of love")

# lets practice 

# print the ele of the following list using loop:

list = [1, 4, 9, 12, 45, 67, 23, 45, 78, 90]

for val in list:
    print(val)

# search for a num x in this tuple using loop:

tup = (1, 4, 9, 12, 45, 67, 23, 45, 78, 67, 90)
x = 67
indx = 0
for val2 in tup:
    if(val2 == x):
        print("found tup", indx)
    indx += 1


# range function 

for i in range(10):
    print(i)

# i have write range func in 3 different seq:

for num in range(10): # range(stop)
    print(num)

for num in range(2, 10): # range(start, stop)
    print(num)

for num in range(2, 10, 2): # range(start, stop, step)
    print(num)

for multi in range(5, 55, 5):
    print(multi)

# lests practice using for and range():

# print 1 to 100
for num1 in range(1, 101, 1):
    print(num1)

# print 100 to 1
for num in range(100, 0, -1): 
    print(num)

# print multiplication 1 to 10 num of n
n = int(input("enter num :"))

for i in range(1, 11):
    print(i * n)

# pass statment 

for i in range (5):
    pass

if i > 6:
    pass

print("end")

#lets practice 

# wap to find the sum of first n numbers using while or for
n = 10 
sum = 0
for i in range(1, n+1):
    sum += i
    
print("total sum =", sum )

n = 10
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum :", sum)

# wap to find the factorial of first n numbers using for

n1 = 10
fact = 1
for val in range(1, n1+1):
    fact *= val

# print("factorial =", fact)

n2 = 5
facto = 1
while i <= n2:
    i *= facto
    i +=1

print("factorial =", facto)