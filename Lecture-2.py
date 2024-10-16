# STRINGS AND CONDITIONAL STATEMENTS

#string is a data type that stores a sequence of characters.
'''There are some basic operations in the strings
1. Concatenation:  means adding to strings together 
ex:"hello+world = helloworld"
a = "hello"
b = "world"
print(a+b) # this will return helloworld

2. Length of the string: this will return the lenght of the string
ex: 
a = "Hello"
A = " I am learning python"
print(a+A)
print(len(a+A))

3. Indexing of the strings : if we pass any index then it will return the value at that index 
ex:
str = "payal khot"
p = str[2]
print(p) # this will return y because 'y' is present at index 2 
#note that indexing always starts from 0.

4. Slicing of the strings : Accessing the parts of the string
this will return the substring or letter between the indices passed in the code
this will not consider the ending index
SYNTAX: str[starting_index : ending_index]
ex:   
str = "prajyotkhot"
print(str[0:5]) #this will return prajy 

5. Negative slicing of the strings: this is same as slicing, only the difference 
is we can give the negative index 
ex:
str = "payal"
print(str[-3:-1])#this will return ya in this code index will start from the right side from 0the-1
'''
#STRING FUNCTIONS

'''
1. str.endswith("") : returns true if string ends with substr
ex:
str = "i am payal"
print(str.endswith("al")) #al is the ending of the string therefore output is true.
 
2. str.capitalize() : capitalizes first char
ex: 
str = "i am payal"
print(str.capitalize()) 

3. str.replace(old,new) : replaces all and occrrences of old
ex: 
str = "I am studying python from apna college"
print(str.replace("o","a")) #this will replace o with using this command.

4. str.find(word) : this function return the word in the program and if 
the word is found then it returns first index of the word means where is he word ppresent.
ex :
str = "My self payal and i am leaning python"
print(str.find("self")) #this returns '3' that means self is present at index 3 

5. str.count(word) : this function counts the occurence of substring
ex :
str = "hello there is a cute dog behind you so please look at that dog"
print(str.count("dog")) #this returns 2 that means the dog word has occured 2 times in the sentence

'''
#This is end of lecture 2