# dictionary and sets
# dictionary
info = {"name" : "atif",
        "CGPA" : 9.3,
        "marks" : [98, 45, 67],
        "is_adult" : True,
        "gender" : "male",
        "class" : "10th"} 
print(info)
print(info["name"])
print(info["marks"])

# change dict value
info["name"] = "alvi mehar"
print(info["name"])

# add value in dict 
info["gender"] = "female"
print(info)

# nested in dict 
student = {"name" : "atif",
           "subject" : {
               "physics" : 98,
               "maths" : 60,
               "chemistry" : 68
        }
 }
print(student)
print(student["subject"])
print(student["subject"]["physics"])

# empty dict 
aa = {}
print(type(aa))
# dictionary methods
# dict.keys()
print(info.keys())

# dict.value
print(info.values())

# dict.items
print(info.items())
pairs = list(info.items())
print(pairs[4])

# dict.get("key")
print(info["nam2"]) #error
print(info.get("name2")) # no error -> none

# dict.update()
info.update({"city" : "bihar", "age" : "20"})
print(info)

new_dict = {"city" : "bihar", "age" : "20"}
info.update(new_dict)
print(info)

# sets in python 
collection = {1, 2, 3, 4, "hello", "hello", "world", 4, 2, 2, 2}
print(collection)
print(type(collection))

# create empty set
sets = set()
print(type(sets))

# set methods
# set.add()

num = set()
num.add(1234)
num.add(23455)
num.add(3456)
num.add("atifkingkhan")

num.remove("atifkingkhan")
print(num)

# set.clear
num.clear()
print(num)

# set.pop() random element delete

collec = {"hello", "sir", "my", "name", "is", "atif"}
collec.pop()
print(collec)

# set.union
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))
print(set1)
print(set2)

# set.intersection
print(set1.intersection(set2))

# lets practice

# store following word meanings in a python dictonary
dict = {"table" : ["a piece of furniture", "list of facts and figures"],
        "cat" : "a small animal"
        }

print(dict)

# you are given a list of subject for students.
# assume one classeroom is required for 1 subject.
# how many classroom are needed by all students.

subject = {"python", "java", "c++",
            "python", "javascript", "java",
            "python", "java", "c++",
            "c"}
print(subject)
classrooms = subject
print(len(classrooms))

# wap to enter marks of 3 subject from the user and store them in 
# a dictionary.
# start with an empty dictionary and add one by one. use subject
# as key and marks as value 

marks = {}

vab1 = int( input("enter phy :"))
marks.update({"phy" : vab1})

vab2 = int( input("enter maths :"))
marks.update({"maths" : vab2})

vab3 = int(input("enter che :"))
marks.update({"che" : vab3})

print(marks)

# figure out a way to store 9.0 as seperate values in the set
# (you can take help of built in data type).

# 1 sollution
values = {9, "9.0"}
print(values)

# 2 use data type sollution 
val3 = {
    ("float", 9.0),
    ("int", 9)
}
print(val3)

# this is the end of a session 