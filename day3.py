# type programme to check student grade through stydents mark

marks = int(input("type marks :"))

if(marks>= 90):
    grade = "A"
elif(marks >= 80 and marks<90):
    grade = "B"
elif(marks >= 70 and marks>80):
    grade = "c"
else:
    grade = "D"

print("grade of the student :", grade) 
