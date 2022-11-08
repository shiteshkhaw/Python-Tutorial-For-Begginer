# Sets are the collection of non repeatable data
a={4,5,9,6,8}
print(a)
print(type(a))
b={}
print(type(b))#It will return the class as Dictionary
#To create an empty set
c=set()
print(type(c))#It is an empty set
#Methods In Sets
c.add(69)#Add the values given in the paranthesis
print(c)
c.add(70)
c.add(81)
c.add(69)
c.add(85)
c.add((4,5,6))#Tuples can be added as it is an hashable datastructure
print(c)
c.pop()#It will remove random values on its own
print(c)
c.remove(81)#It will remove the given value
print(c)
c.add([4,5,8,9])#It will not add List as it is an unhashable data structure
print(c)
c.add({45:69})#Dictionary is also an unhashable data structure

