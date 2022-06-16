# def print2(str1):
#     print2(str1)
#     print("this is" + str1)

# print2(" harry")





# def factorial(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac

# number = int(input("enter the number"))
# print(factorial(number))





# def factorial(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#         return fac

# number = int(input("enter a number: "))
# print(factorial(number))




# a = [1,2,4,5,3,6,7,4,5]
# sum = 0
# for i in range(0,len(a)):
#     sum = sum + i
# print("sum of elements is : ", sum)





# a = [1,2,4,5,3,6,7,4,5]
# sum = 0
# i = 0
# while(i < len(a)):
#     sum = sum + a[i]

# print("sum of elements is : ", sum)

# a = [1,2,4,5,3,6,7,4,5]
# total = sum(a)
# print("total = ",total)





departmental = ["2 detol", "3 soap", "2 tide", "1 colgate", "2 detol", "2 tide"]
unique_items = []
for item in departmental:
    if item not in unique_items:
        unique_items.append(item)
print(unique_items)

