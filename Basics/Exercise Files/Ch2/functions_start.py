#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a func1")

# function that takes arguments
def func2(arg1,arg2):
    print(str(arg1) + " " + str(arg2))

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def func3(*arg):
    result = 0
    for i in arg:
        result = result + i
    return result


# func1()
# print(func1())
# print(func2(2,3))
# print(cube(3))
# print(func3(2,3,4,5))
print(power(2,3))

