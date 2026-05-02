print("atif is my name")
print("my age is 20")

print("atif is my name", "my age is 20")
print (23 + 23)
print(23 * 23)
print(23 / 23)
print(23 - 23)

# question 1
name = "aTIF"
age = 23
price = 25.99

print(name, age, price)
print("my name is :", name)
print("my age is :", age)

age2 = age
print (age2)

# how to find datatypes wse stored in variables
print(type(name))
print(type(age))
print(type(price))

name1 = "sk"
name2 = 'sk'
name3 = '''sk'''
print(name1)
print(name2)
print(name3)

# boolean variable
a = 23
old = False
b = None
print(type(a))
print(type(old))
print(type(b))

# calculate revenue
quantity = 100
price = 18 
revenue = quantity * price

print("revenue is:", revenue)

# arithmetic oprators

a = 100
b = 200

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# relational comparision oprators
n = 50
m = 20

print(n == m)
print(n != m)
print(n < m)
print(n <= m)
print(n >= m)
print(n > m)

# assignment oprators

num  = 10
num = num + 10
print(num)

num = 10 
num += 10
print(num)

num = 10
num -= 10
print(num)

num = 10 
num *= 10
print(num)

num = 10
num /= 10
print(num)

num = 10
num %= 10
print(num)

num = 10
num **= 10
print(num)

# logical oprators

alvi = 50
atif = 56

print(alvi > atif)
print(not (alvi > atif))

val1 = True
val2 = False
print( val1 and val2)
print(val1 or val2)
print(alvi != atif and alvi < atif)
print(alvi == atif or alvi < atif)

# type conversion automatic conversion
a = 2
b = 4.25
sum = a + b 
print( sum )

a = int("2")
b = 4.25
print(a + b)

a = 3.14
a = str(a)
print(type(a))

# input in python

name = input("enter your name :")
print("welcome", name)

love = input("name :")
print ("i love you", love)

name = input("enter name :")
age  = int(input("enter age :"))
marks = int(input("enter marks :"))

print("welcome", name)
print("age =", age)
print("marks =", marks)

# lets practiece
a = int(input("first number"))
b =int(input("secound number"))
print("sum =", a + b)

# wap to input side of a squar and print its area.
side = float(input("enter sides :"))
print("area =", side * side)

# wap to input 2 floating point numbers and print their average.

a = float(input("first number :"))
b = float(input("second number :"))
print("avg =", (a + b) /2)

# wap to input 2 int num a and b 
# print true iF a is greter then = b if not print false

a = int(input("first no :"))
b = int(input("second no :"))
print(a >= b)

# strings types
str = "this is a strings.\nwe learn string today"
str1 = 'python is the most using language in ai'
str2 = '''this is also a string with 3 coumas'''
print(str)

# concat strings
bbb = "atif"
ccc = "king"
print(bbb + ccc)

# lenth function
lenth = "i am the best. iam the only one of in this universe"
print(len(lenth))

# indexing
strings = "king of the years atif"
cha = strings[3]
print(cha)

# slicing
boobs = "atifpapahai"
print(boobs[4 : 8])

# slicing -index
boobs2 = "ashique"
print(boobs2[-6 : -1])

# func endswith 
end = "i am a coder"
print(end.endswith("er"))

# func capitalize 
cap = "atif salim"
print(cap.capitalize())

# func replace 
rep = "i am studying python from apna coollege"
print(rep.replace("o", "a"))

# func find
find = "i am studying python from apna coollege"
print(find.find("o"))

# func count 
cou = "i am studying python from apna coollege"
print(cou.count("o"))

# letspractice
# wap to inputs find name and print its length
aa = input("first name : ")
print("lenth", len(aa))

# wap to find the occurrence of '$' in s string 
bb = "atif kdsf$jetj$ dfjr$ this$is $ the$according$and$and$"
print(bb.count("$"))

#conditional statement 
#if() condition
