
# # strings types
# str = "this is a strings.\nwe learn string today"
# str1 = 'python is the most using language in ai'
# str2 = '''this is also a string with 3 coumas'''
# print(str)

# # concat strings
# bbb = "atif"
# ccc = "king"
# print(bbb + ccc)

# # lenth function
# lenth = "i am the best. iam the only one of in this universe"
# print(len(lenth))

# # indexing
# strings = "king of the years atif"
# cha = strings[3]
# print(cha)

# # slicing
# boobs = "atifpapahai"
# print(boobs[4 : 8])

# # slicing -index
# boobs2 = "ashique"
# print(boobs2[-6 : -1])

# # func endswith 
# end = "i am a coder"
# print(end.endswith("er"))

# # func capitalize 
# cap = "atif salim"
# print(cap.capitalize())

# # func replace 
# rep = "i am studying python from apna coollege"
# print(rep.replace("o", "a"))

# # func find
# find = "i am studying python from apna coollege"
# print(find.find("o"))

# # func count 
# cou = "i am studying python from apna coollege"
# print(cou.count("o"))

# # letspractice
# # wap to inputs find name and print its length
# aa = input("first name : ")
# print("lenth", len(aa))

# # wap to find the occurrence of '$' in s string 
# bb = "atif kdsf$jetj$ dfjr$ this$is $ the$according$and$and$"
# print(bb.count("$"))

# #conditional statement 
# #if() elif() condition
# num = 5 
# if(num>8):
#     print("greater then")
# elif(num>3):
#     print("big")   

# light = "green"

# if(light == "red"):
#     print("stop")

# elif(light == "yellow"):
#     print("loook")

# elif(light == "green"):
#     print("go")

# # else statment

# empsalary = 4000

# if(empsalary>6000):
#     print("better")

# elif(empsalary<2000):
#     print("bad")

# elif(empsalary == 5000):
#     print("good")

# else:
#     print("koi baat nahi")

# age = 14

# if(age >= 20):
#     print("can vote")

# else:
#     print("cannot vote")

# # grade students based on marks

# marks = int(input("type marks :"))

# if(marks>= 90):
#     grade = "A"
# elif(marks >= 80 and marks<90):
#     grade = "B"
# elif(marks >= 70 and marks>80):
#     grade = "c"
# else:
#     grade = "D"

# print("grade of the student :", grade) 

# # nesting
# age = 20
# if(age >= 18):
#     if(age <= 50):
#        print("can drive")
# else:
#     print("cannot drive")

num = int(input("type number"))

rem = num % 2

if(rem == 0)
    number = "even"
else:
    number = "odd"

print("number is :", number)