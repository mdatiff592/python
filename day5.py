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

        