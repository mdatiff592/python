# # dictionary and sets
# # dictionary
# info = {"name" : "atif",
#         "CGPA" : 9.3,
#         "marks" : [98, 45, 67],
#         "is_adult" : True,
#         "gender" : "male",
#         "class" : "10th"} 
# print(info)
# print(info["name"])
# print(info["marks"])

# # change dict value
# info["name"] = "alvi mehar"
# print(info["name"])

# # add value in dict 
# info["gender"] = "female"
# print(info)

# # nested in dict 
# student = {"name" : "atif",
#            "subject" : {
#                "physics" : 98,
#                "maths" : 60,
#                "chemistry" : 68
#         }
#  }
# print(student)
# print(student["subject"])
# print(student["subject"]["physics"])

# # empty dict 
# aa = {}
# print(type(aa))
# # dictionary methods
# # dict.keys()
# print(info.keys())

# # dict.value
# print(info.values())

# # dict.items
# print(info.items())
# pairs = list(info.items())
# print(pairs[4])

# # dict.get("key")
# print(info["nam2"]) #error
# print(info.get("name2")) # no error -> none

# # dict.update()
# info.update({"city" : "bihar", "age" : "20"})
# print(info)

# new_dict = {"city" : "bihar", "age" : "20"}
# info.update(new_dict)
# print(info)

# # sets in python 
# collection = {1, 2, 3, 4, "hello", "hello", "world", 4, 2, 2, 2}
# print(collection)
# print(type(collection))

# # create empty set
# sets = set()
# print(type(sets))

# set methods
# set.add()

num = set()
num.add(1234)
num.add(23455)
num.add(3456)
num.add("atifkingkhan")

num.remove("atifkingkhan")
print(num)
