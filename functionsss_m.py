'''a = 5
b = 8
c = sum((a,b)) #built in function
print(c)'''

'''
def function1():
    print("hello you are in function 1")

(function1())
(function1())
(function1())
(function1())
(function1())
(function1())
'''


def function1(a,b):
    print("the sum of a and b", a+b)


def function2(a,b):
    '''this is a function which will calculate average of two numbers'''
    average = (a+b)/2
    print(average)
    # return average

v = function2(4,6)
w = function1(5,5)


print(function2.__doc__)
print(v,w)

















