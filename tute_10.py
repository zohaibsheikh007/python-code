# dictionary is nothing but key value pairs
d1 = {}
#print(type(d1))
d2 = {"Zohaib" : "burger" , "sohail" : "chicken" , "junaid" : "roti" ,
     "shubham" : {"B" : "bread" , "L" : "roti"}}
d2["Ankit"] = "junk food"
d2["420"] = "kababs"
#print(d2["junaid"])
#print(d2["shubham"] ["B"])
print(d2)
d3 = d2.copy() 
del d3["420"]
print(d2)
print(d2.get("Zohaib"))
d2.update({"Leena" : "Tofee"})
print(d2)
print(d2.keys())
print(d2.items())















