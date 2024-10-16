# LISTS IN PYTHON
# A built-in data type that stores set of values.
# It can store elements of different types(integers,floats,strings,etc)
# Lists are always written in square barces like []
# lists are mutuable means we can make changes into the list like add,sub,etc

# ex:
# marks = [87,45,68,90,100]
# fruits = ["mango","guava","apple","jackfruit","banana"]
# print(marks) this will print the entire list named marks
# print(len(marks)) this is return the length of the list marks
# print(fruits)
# print(len(fruits))
# print(fruits[0]) thus will print mango 

# LIST SLICING
#  this is simliar to string slicing
# syntax:   list_name[starting_index:ending_index] endong index is not considered

# ex:
# marks = [23,45,89,27,100]
# print(marks[1:3]) this will return [45,89] last index will not be included
# this also supports negative indexing

# ex:
# list = ["payal","prajyot",58,10]
# print(list[1:-1]) this will print ["prajyot",58]

'''LIST METHODS 
1. list.append() : adds new element at the end of the list 
ex:
age = [23,47,29,60,50]
age.append(66)
print(age)

2. list.sort() : sorts in assending order even we can append into it
ex: 
name = ["payal","apple","oxygen","zebra"]
name.append("cow")
print(name)
name.sort()
print(name)

3. list.sort(reverse=True) : sorts in desending order 
ex:
numbers = [1,2,3,4,5,6]
numbers.sort(reverse=True) this will return the list in desending order
print(numbers)

4. list.reverse() : this reverses the original list as it is
ex:
city = ["jaysingpur","mumbai","banglore","belgavi"]
city.reverse()
print(city) list  is printed in reverse order

5. list.insert(idx,ele) : this method inserts the elemnt at specific index
ex:
soap = ["lux","dove","lifeboy"]
print(soap)
soap.insert(0,"cinthoal")
print(soap) #cinthoal is inserted at the first place int the list
soap.sort()
print(soap)

6. list.remove() : removes first occurence of the element
ex:
table = [2,4,6,8,10]
table.remove(4) #removes 4 from the list
print(table)

7. list.pop(idx) : removes element at the specific index given
ex:
things = ["box",45,"pencile",30,100]
things.pop(0)
print(things) #box will be removed from the list
'''

# TUPLES IN PYTHON
# A built-in data type that let us create an immutable sequence of values
# Tuple is always written in simple braces()
# We can also create an empty tuple like tup = ()
# We can also print only one element into the tuple like tup = (1,)
# Comma is compulsory in the tuple because that comma treats it as tuple or else it wil
# treat it as integer  

# ex:
# tup = ()
# print(tup) #empty tuple is created this will return ()

# ex:
# one = (1,)
# print(type(one))
# print(one) #this will print one element of the tuple one

# TUPLE SLICING
# this is also possile here
# ex:
# tup = ("payal",45,"prajyot",20)
# print(tup(0:2)) #last index is not included like lists and strings

'''TUPLE METHODS

# 1. tup.index(el) : returns index of the first occurence
# ex: tup = ("orange",68,"apple",3.6)
print(type(tup))
print(tup.index(3.6)) 
this returns the index of the element

 2. tup.count(el) : counts the total number of occurences
ex:
tup = ("payal",2,"payal","2")
print(tup.count("payal")) this will return number od times the elemnet is present
'''

############################   END   ##########################################
