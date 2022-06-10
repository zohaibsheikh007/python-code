from operator import imatmul

#unpacking a list
#list1 = [["zohaib" , 1 ], ["sohail", 3] , ["zunaid", 6 ], ["zaid" , 99]]
#dict1 = dict(list1)



#print(list1[0] ,list1[1])
#for item,tofee in dict1.items():
 #   print(item,"and tofee is",tofee)

#for item in dict1:
    #print(item)


itemsoflist = [int, float , "zohaib", 22 , 1 , 22 , 4 , 55 , 8 , 88 , 99]
for item in itemsoflist:
    if str(item).isnumeric() and item>6:

        print(item)


















