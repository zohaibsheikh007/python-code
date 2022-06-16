
'''
0) double the element in list
ex = [5,10,15,6,3,7,9,11,5,16,7]


1) remove duplicate from the list
ex = input [1,1,2,2,3,4,3,4,2]
output = [1,2,3,4]

2) get sum of the array
ex = [2,3,44,2,4,6]
output = 61

3) perform arithmatic operations
ex = [1,"+",2,"+",4,"*",2,"*",-1,"*",100,"/",10]
output = -140
'''




'''def remove_duplicate(number):
    number = list(set(number))
    return number
    
    
    # unique_list = []
    # for elements in number:
    #     if elements not in unique_list:
    #         unique_list.append(elements)
    # return unique_list
    
number1 = [1,1,2,2,3,4,3,4,2]
print(remove_duplicate(number1))'''

'''def double_array(numbers):
    double = []
    for x in numbers:
        
        double.append( x * 2)
    return double

print(double_array([1,1,2,2,3,4,3,4,2]))'''




# def summation_numbers(numbers):
#     sum = 0
#     for x in numbers:
#         sum = sum + x
#     return sum

# numbers = [2,3,44,2,4,6]
# print(summation_numbers(numbers))

def arithmatic_operation(list):
    var = list[0]
    for i in range(1,len(list),2):
        print(i)
        if list[i] == "+":
            print(var,"+",list[i+1]," = ",var+list[i+1])
            var = var + list[i+1]
        elif list[i] == "-":
            print(var,"-",list[i+1]," = ",var-list[i+1])
            var = var - list[i+1]
        elif list[i] == "*":
            print(var,"*",list[i+1]," = ",var*list[i+1])
            var = var * list[i+1]
        elif list[i] == "/":
            print(var,"/",list[i+1]," = ",var/list[i+1])
            var = var / list[i+1]

    return var

# print(arithmatic_operation([1,"+",7,"-",4,"*",2,"*",-1,"*",100,"/",10]))




'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3],'''


#def nums(ar1,ar2)

'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
([)] = false'''








'''
168. Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"
'''




'''
171. Excel Sheet Column Number
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 
Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701
xit-apov-yxk'''


'''
136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''


'''217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''



'''169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
xit-apov-yxk
'''



'''Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''


def index_values(list1,target):
    a = []
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i] + list1[j] == target:
                a[0]=i
                a[1]=j
                
                return a
               

list1 = [2,11,7,15,3,6]
target = 9
#print(index_values(list1,target))




# n = int(input("enter number"))
# sum = 0
# i = 1
# while (i<=n):
#     sum = sum + i
#     i = i + 1

# # for i in range(n+1):
# #     sum = sum + i
# print(sum)




# Q 1)
# 1. You are given a string exp representing an expression.
# 2. Assume that the expression is balanced  i.e. the opening and closing brackets match with each other.
# 3. But, some of the pair of brackets maybe extra/needless. 
# 4. You are required to print true if you detect extra brackets and false otherwise.

# e.g.'
# ((a + b) + (c + d)) -> false
# (a + b) + ((c + d)) -> true


def duplicate_bracket(expression):
    stack = []
    for i in expression:
        if i != ")":
            stack.append(i)
        else:
            pop_count = 0
            while(True):
                last_var = stack[-1]
                if last_var == "(":
                    if pop_count == 0:
                        return True
                    stack.pop()
                    break
    
                else:
                    stack.pop()
                    pop_count += 1
    return False

print(duplicate_bracket('((a+b)+(c+d))'))
print(duplicate_bracket('(a+b)+((c+d))'))


'''
1.declare an empty stack
    1.1 loop the expression for i values

2. if current character in string is "("
    2.1 push characters to empty stack 
3. else character is ")"
    3.1 pop characters from empty stack'''
