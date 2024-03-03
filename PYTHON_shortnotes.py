
# SHORT NOTES
# print("hello world")
# # another way of print function --->when comma separated ,it prints in the same line
# print("My name is adi . ","I am 20 years old")
# # we can print numbers
# print(34)
# # we can perform arthematic operations
# print(43*44)
# print("hello\
# world")
# if u want to write the statement in multiple lines then use \
# print(''' A
# A
# A ''')
# use ''' """ at both ends to print the lines as it as u want

# # VARIABLES

# name="adithya"
# age=20
# price=34.45
# # = is called assignment operator
# a,b = 10,20  ----> is valid
# print(name,age,price)
# # or
# print("My name is :",name,"I am ",age,"old","my price is ",price)

# # IDENTIFIERS -->names of variables
# # not start with numbers(but can be at end)
# # only underscoe is allowed in special characters
# # case sensitive
# # size of variable name can be any thing(but make it simple,meaningful)
# # dont use the keywors names as identifiers

# #WE CAN GET THE TYPE(data type) OF THE VARIABLE BY USING type
# print(type(name))
# print(type(age))
# print(type(price))
# # 5 data types
# # 1.int  2.float  3.string   4.boolean  5.none
# #we can assign the string value to A VARIABLE IN " " ,' '  ,'''  '''.
# print('test')
# print("test")
# print('''test''')

# # true and false are the 2 values in boolean --they start with capital T and F   and none type also starts with capital N
# va1=True
# va2=False
# print(va1)
# print(va2)

# # none

# a=None
# print(type(a))

# KEYWORDS=reserved words
# PUNCTUATORS ---{}.[],#,*=,@,()
# python is a implicit typed lang.
# string can be multiplied with numebr 
# if u wanna add 2 str's then use +(it is called concatination)

# print(1/1)---->division always gives float value    
# (verify it once)even it is a integer divison(//) it gives float only but integer part is the value and decimal value is 0
# print(7//7)

# modulo(%)value is -ve only when numerator is +ve , and denominator is -ve---->this is the only 1 case

# COMMENTS
# -->single line -- #
# -->multi line --- """    """
# print("heeee")
# press ctrl+/ ---to comment the line
# """ print("hello")"""

# INPUT--->is always in string datatype 
# print() 
# name = input("Enter name : ")
# so,we use type casting
# name=str(input("Enter name"))
# print(name)

#  this task can be done by :
# print(input("name:"))

# OPERATOR PRECEDENCE
# not>and>or

# CONDITIONAL STATEMENTS

# if(condition1) :
#     statement1
# elif(condition2):
#     sttaemnet2
# else:
#     statement3

# INDENTATION IS IMPORTANT 

# TRAFIC LIGHT EXAMPLE  

# light = input(" enter light color : ")
# if(light=="red"):
#     print("STOP")
# elif(light=="yellow"):
#     print("LOOK UP")
# elif(light=="green"):
#     print("GO")
# else:
#     print("LIGHT IS INVALID")

# LOGICAL OPERATORS
# and or not

# TERNANRY OPERATOR
#   <str1> if <condition> else <str2>
# ex: print("yes") if (a>=18) else print("no")

# CLEVER IF OPeRTAOR
# <var> = (false_value,true_value) [<condition>]
# ex: a = ("yes","no") [a>=18]

# OPERATORS AND ITS TYPES
# 1.ARTHEMATIC  -----   + - * / % **(power) //    every time we divide we get float value as result
# 2.RELATIONAL ------   > < >= <= == !=
# 3.ASSIGNMENT ------   = += -= *= /= %= **=
# 4.LOGICAL -----------  and or not

#TYPE CONVERSION
# 1.AUTOMATIC CONVERSION (IMPLICIT)
# 2.MANUAL CONVERISION (TYPE CASTING----mentioned in a brackets (int))(EXPLICIT)

# strings are sequence of characters
# " " / ' '  / """  """
# when ever u use """ """ ===> it prints as it is ,even  the tabs,next lines 
# # ESCAPE SEQUENCE CHARACTERS
# "\n" ==> next line

# STRING CONCATINATION
# use this +
# use len() to find length of the string
# it has indexing--startts from 0---and used for accesing
# string cannot be changesd(immutable) by indexing--- index assignment is not possible   --- ex: marks[2]='r'
# slicing --acceseing parts of a string
#  [0:5]--- returns from 0 to 4---(5-1)--->last parameter is exculded
# negative indexing----from -1,-2,-3,......
# [-3,-1] -- returns from -3 to -2--->last parameter is exculded

# STRING FUNCTIONS---this doesnot change the value of the string,it just manuplates the present string snd prints it

# 1.str.endswith("xyz")---boolean
# 2.str.capitalize("str")---str--capitalizes first chcar
# 3.str.replace(old,new)---str---replaces the occurences
# 4.str.find(word/char)----returns index value of the first occurence--returs -1 if ,not exists,but it doesnt mean that it is giving the negative indexing value===>by the way negative indexing is  only for slicing concept
# 5.str.count("str/char")---returns no.of occurances

# LISTS IN PYTHON - similar to strings
# written in [] and the values are comma separeted
# has indexing-starts from 0
# length can be -returned by len()
# we can store any type of data unlike array
# can be changed(mutable)
# list slicing can be done
# index assignment is possible   --- ex: marks[2]=3454.56
# marks = [1,3,4,4,5,"adi",6.343]
# print(marks)
# print(type(marks))
# print(marks[2:5])
# duplicates allowed and it doesnt ignores while printing

# METHODS in lists:
# 1.list.append()---adds at the end
# 2.list.sort()-----sorts in ascending order
# 3.list.reverse()--reverses the list
# 4.list.insert(index,element)---inserts at specified index
# 5.list.remove(element)---removes first occurance
# 6.list.pop(index)---removes that element



# TUPLES IN PYTHON
# immutable--just like strings
# use () and separeted by comma
# acessed by indexing
#  index assignment is possible   --- ex: marks[2]=3454.56
# can crreate empty tuple , by 
# tu = (1)
# print(type(tu))
# but when we have single element tuple then make sure u have used , after that element---if not it will take it as int
# slicing can be done
# METHODS
# 1.tup.index(ele)---returns first occurance index
# 2.tup.count(ele)---returns no.of times it occoured
# tup = (1,2,45,2)
# print(tup)
# print(type(tup))
# duplicates allowed and it doesnt ignores while printing

# DICTIONARIES IN PYTHON
# works in pairs
# "key":value
# mutable
# not dupilcates
# use {pairs} and comma separated
# unordered i.e no index
# info = {
#     "name" : "adi",
#     "age" : 20,
#     "topics" : (1,3,4,45)
# }
# print(info)
# print(type(info))
# accessing:
# print(info["name"])
# new key can be inserted as :
# info["f'name"] = "ramesh"
# print(info)
# if the keyname is same ---then it overrides
# empty dic:
# d = {}
# print(d)
# DICT METHODS
# 1.dict.keys() --- returns collection of keys
# 2.dict.values()---returns values\
# 3.dict.items()---returns key value pairs--tuple
# 4.dict.get("key")---returns its value
# 5.dic.update(pair)---adds that pair


# SETS IN PYTHON
# unique values,unordered i.e no index,immutable
# use {} and comma sepatared but has no pairs
# setex = {1,3,4,5,5}
# if values are repeated,then it just ignores
# print(setex)
# print(type(setex))
# for empty set --- use
# coll=set()
# print(type(coll))
# 
# SET METHODS
# SETS ARE MUTABLE,BUT ELEMENTS IN IT ARE IMMUTABLE i.e we can add new elements to it
# 1.set.add(ele)--adds that element
# 2.set.remove(ele)---removes the elemenet
# 3.set.clear()---empties the set
# 4.set.pop()--removes a random value     
# 5.set.union(set2)
# 6.set.intersection(set2)  


# LOOPS
# 1.while
# 2. for

# WHILE
# count  = 1
# while count<=10:
#     print(count)
#     count+=1
# print("End of loop")


# FOR
# for variable in list :
    # code
# else is opitonal

# RANGE()---returns sequence of numbrs
# if--range(5)----it returns 0,1,2,3,4 
# range(stop)---starts from 0 to stop-1
# range(start,stop)
# step value is 1 by deafult
#range(1,20,2)
# --start,stop,step


# BREAK AND CONTINUE
# break ----stops immediatley
# continue---stops that particular iteration


# pass keyword---it is used to ,,keep the code,empty,and it can be filled later



# FUNCTIONS
# def fn_name(parameters):
#     # code
#     return a
# to print the statements in the same line then  use :
#   end = " "

# RECURSION
# def show(n):
#     # if(n==0):base condition
#         return
#     print(n)
#     show(n-1)
# show(6)



# FILE I/O 
# f=open("demo.txt", "r")
# f=open("demo.txt", "w")
# data = f.read()
# data = f.readline()//empty lines will be printed,if there is no data in the fole
# print(data)
# f.write("\nhello")
# data = f.read()
# print(data)
# f.close()
