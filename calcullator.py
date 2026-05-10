# making calculator
print(1., "additon")
print(2., "subtraction")
print(3., "multiplication")
print(4., "division")
print(5., "modulo")
print(6., "power")

choice = input("enter your choice (1/2/3/4/5/6) :")

num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))

if(choice == "1"):
    result = num1 + num2
    print("result :", result)

elif(choice == "2"):
    result = num1 - num2
    print("result :", result)

elif(choice == "3"):
    result = num1 * num2
    print("result :", result)

elif(choice == "4"):
    if(num2 != 0):
        result = num1/num2
        print("result :", result)

elif(choice == "5"):
    result = num1 % num2
    print("result :", result)

elif(choice == "6"):
    result = num1 ** num2
    print("result :", result)

else:
    print("error: devide num 0 is not allowed")


