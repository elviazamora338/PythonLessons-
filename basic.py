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
    return num - num2

print(subtraction())

# second way
myResult = 0.0
def subtraction(result):
    result = num - num2
    return result

print(subtraction(myResult))
