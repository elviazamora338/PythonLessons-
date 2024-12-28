lara = "He don't know"

# int variable
num = 1

# double or float variable
num2 = 1.3

# declaring a function 
def firstFunction(test):
    print(test + " doesn't know")

# call the function

firstFunction("Lara")
# work bitch
print(num)

#  1st approach
def addition():
    return num + num2

print(addition())

#  second approach
myResult = 0.0

def addition2(result):
    result = num + num2
    return result

print(addition2(myResult))

# 1st way
def subtraction():
    if num > num2:
        return num - num2
    elif num < num2:
        return num2 - num
   

print(subtraction())

# second way
myResult = 0.0
def subtraction(result):
    if num > num2:
        result = num - num2
    elif num < num2:
        result = num2 - num
    # will return whatever result becomes
    return result

print(subtraction(myResult))


#  arrays 
grades = [100, 60, 80, 100, 20, 10, 90]

#  by default 0
for x in grades:
    print(x)


max = grades[0]
# 60
for x in range(7):  
    # the current index in grades is greater than current max
    if grades[x] > max:
        # max = 70
        max = grades[x]
        print("max grade = ", max)

min = grades[0]
for x in range(7):
    if grades[x] < min:
        min = grades[x]

        print("min grade = ", min)
