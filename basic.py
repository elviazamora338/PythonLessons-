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


# while loop
index = 0
max = grades[index]
while index < 7:
    if grades[index] > max:
        max = grades[index]

    # index = index + 1
    index+=1
    
print("max grade for while loop = ", max)   
  
index2 = 0
while index2 < 7:
    if grades[index2] == 20:
        print("index for 20 =",index2)
    
    index2+=1

##########   QUESTION 1: ##########
# make a for loop that goes through the array grades and finds grade 10
# print the index that holds value 10 not the actual grade 10


# COMMENTS: This code is redundant. You are using two for loops instead of using just one 
# based on your code this is your logic that is having :: In the first loop, you are going through all the grades in the array, looking for the grade 10.
# If a grade 10 is found, you print "grade 10 found".
# Then, in the second loop once 10 is confirmed, you iterate over the grades array again using enumerate to find the index where the grade is 10.
# you are going through the array again in the for loop when you already found 10.
# the point of enumerate is that you don't need two for loop or need to do what we did prior. You are given the index and the value in the array at the same time
# also the index+=1 is primarily used in while loops or special conditions. right now it is doing this 0,2,4,etc  

for index, grade in enumerate(grades):
    if grade == 10:
        print("The index holding the value 10 is:",index)
        break



###########  QUESTION 2: ############
# give me the average of the total grades 
# either find a shortcut, create a function prior, or do avg = (addition of all grades)/(the total amount of grades)
# MUST USE a for or while loop
total = 0
for grade in grades: 
    total += grade
average = total / len(grades)
print ("average grade using for loop =", average)

###########  QUESTION 3: #############
# go through the array and print out a statment if at least one grade is repeated "there is one repeated grade"
# else print "No repeated grades"
# Use a while loop
index = 0
found_repeated = False 
while index < len(grades):
    if grades[index] in grades[index + 1:]:
        found_repeated = True
        print('There is one repeated grade.')
        break
    index += 1

if not found_repeated:
     print("no repeated grades.")



    # paper rock scissors game
    # random number generator is the computer only 0,1,2 the randoly generrateed will be computer
    # The user can input their decision but they will also be prompted the gane and if they want to play
    # if they enter 0 that paper, 1 is rock, 2 is scissors
    # if the user puts paper and the computer is rock then user wins, keep same logic throughtout other options
    # same logic applies to computer and they will be prompted who the winner is and if they want to play again
    


    # Prime Number Check
    # Write a function that checks whether a given number is prime.
    # Prime numbers are natural numbers that are divisible by only 1 and the number itself. 
    # In other words, prime numbers are positive integers greater than 1 with exactly two factors, 1 and the number itself. 
    # Some of the prime numbers include 2, 3, 5, 7, 11, 13, etc.

    # 


    # make me this tree

# *
#  * 
#   *
#    *

    # make this other tree
    #       *       # 0 starts at column 3
    #      * *      # 1 
    #     * * *     # 2
    #   * * * * *   # 3 


#     for(int row = 0; i < 4; ++i)
# {
#     for(int col = 0; j < i; ++j)
#     {
#         cout << "*"
#     }
# }


# int first = 0 # 1
# int second = 1 # 1
# int third = 2 # 2

# #  to get the length of the array 
# # 6
# array.len()

# while(third does not equal the length)
#     {
#         does the array[first] + array[second] = array[third] 
#             YES
#             # incrementing
#             ++first # 1 second variable in the array
#             ++second # 2 # third variable in the array
#             ++ third # 3 

#     }