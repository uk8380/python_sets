#sets used to store multible items in single variable
#this are unordered


uk={"uday",7,8}
for x in uk:#in set we can't access by index
    print(x)
    
print(type(uk))
#alternate to setup sets
uko=set(("uday",99,00))
print(type(uko))
#relational operator
print("banana" in uk)
uk.update(uko)
print(uk)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.union(y)
print(x)
