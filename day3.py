# list in python 
marks = [11, 22, 33, 44, 55]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(marks[3])
print(marks[4])

# list is mutable 

student = ["atif", 99.9, 17, "bihar"]
print(student[0])
student[0] = "mehar"
print(student)

# list slicing similar to strings slicing 
marks = [23, 55, 66, 87, 90]
print(marks[0:4])
print(marks[-5:-1])

# list methods
#list.append(add one element at the end )
list = [2, 4, 55, 789, 123]
list.append(100)
print(list)

# list.sort(short is asce oeder)

apple = [5, 4, 3, 2, 1]
apple.sort()
print(apple)
apple.sort(reverse=True) # sort in desc order
print(apple)

# list.rverse
okk = ["my", "name", "is", "atif"]
okk.reverse()
print(okk)

# list.insert
byy = ["my", "name", "is", "atif"]
byy.insert(3, "love")
print(byy)

# remeove methods
remo = [22, 34, 56, 78, 90]
remo.remove(78)
print(remo)

# list.pop
pop = [12, 45, 56, 78, 12, 11, 90]
pop.pop(5)
print(pop)


# tuples in python it is immutable

tup = (3, 3, 6, 7, 8, 9)
print(type(tup))
print(tup)

aa = (1) # python understand this is a int value
aa = (1,) # then python undersatand this is a tuple (,) is madetory in tuple value
aa = (1, 2, 3, 4)#but (,) is madatory in starting value ending value is not madatory in tupls value

# methods of tuple
# tup.index(), tup.count()

mango = (1, 4, 6, 8, 9, 4, 7, 4, 2, 4)
print(mango.index(8))
print(mango.count(4))

# lets practice 

# wap to ask the user to enter name oof their 3 favorite movies and store them in a list
movies = []
a = input("first movie")
b = input("second movie")
c = input("third movie")
movies.append(a)
movies.append(b)
movies.append(c)

print(movies)

# wap to check if a contains a palindrome of elements.(hint.use copy()method)
list = [1,2,1]
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrom")
else:
    ("not palindrom")

# wap to count the number of students with the gradde "A" in the following tuple
# ["C", "D", "A", "A", "B", "B", "A"]

Grade = ("C", "D", "A", "A", "B", "B", "A")
print(Grade.count("A"))
 
# store the above value in a list & sort them "A" to "D".

alph = ["C", "D", "A", "A", "B", "B", "A"]
alph.sort()
print(alph)

