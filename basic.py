# print('hello world')
# Everything in python is considered as object.Objects have attributes and functions.
# the size,color,speed of car are the attributes,car is object,function are drive,brake,accelerate.
# Functions wrt these objs are called methods.so every obj has attributes and methods.
# a = 6.7
# print(type(a))
# b = 5/5   ## in python3 division result is always float value.
# print(b)
# c = 3 // 3  ## print int division
# print(c)

# str.__dict__   #know the string methods
# help(str)
# b = b+3
# print(b)
# strings are list or sequence of chars.In python strings are an objs and they have methods.
# p = 'orange'
# print(p[0:2])
# print(p[-2])
# q = 'mango'
# print(p + ' ' + q)
# print(p*4)
# print(p.upper())
# p.swapcase()
# a.rjust(40,'-')   #a.center(40,'-')
# color = 'blue,black,white'
# print(color.split('a'))
# print(len(p))
# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8, 9]
# l = l1+l2
# l.append(34)
# l.pop()
#  fib.remove(1)
# del(l[5])
# print(l)
# char = ['aa', 'nn', 'kk', 6]
# # char.pop()
# char.append(90)
# print(char)
# newlist = [l, char, ['mango', 'lichi', 'lili', '103']]
# print(newlist[2][2])
# newlist1 = [newlist, char, l]
# print(newlist1[0][1][2])
# print(newlist1[1])
# print(newlist1[2])
# print(type(newlist))
# name = input('enter your name:')
# age = input('enter ur age:')
# print('hello', name, 'your age', age)
# area of circle
# radius = int(input('enter the radius:'))
# area = 3.142*(radius**2)
# print('area of the circle:', area)
####################################################
# FORMAT METHOD
# n1 = 3.14257890
# n2 = 10.2345678
# print('n1 is {0:.4} and n2 is {1:.3}'.format(n1, n2))
#####################################################
# # USING F-STRINGS
# print(f'num1 is {n1:.3} and num2 is {n2:.4}')
# age = int(input('enter ur age:'))
# if (age > 18 and age < 60):
#     print('you are eligible')
# elif (age > 60):
#     print('you are free')
# else:
#     print('you are not eligible')
######################################################
# veg = input('are you vegan?(y/n):')
# if veg == 'y':
#     print('vegeterian')
# else:
#     print('non-vegeterian')
# names = ['a', 'b', 'c', 'd']
# # for name in names[1:3]:
# #     print(name)
# for name in names:
#     if name == 'c':
#         print(f'{name} is cat')
#         break
#     else:
#         print(name)
###################################################################
# num = 0
# age = 20
# while num < age:
#     if num == 0:
#         num += 1
#         continue
#     if num % 2 == 0:
#         print(num)
#     if num > 10:
#         break
#     num += 1
##########################################################
# for n in range(5, 20, 3):
#     print(n)
# for n in range(5, 20, 3):
#     print(n)
# char = ['a', 'b', 'c', 'F', 'h']
# # for n in range(len(char)):
# #     print(n, char[n])
# for n in range(len(char)-1, -1, -1):
#     print(n, char[n])
###########################################################
# def greet():
#     print('hi')
# greet()
# def greet(name, age):
#     print(f'hi,my name is {name},age is {age}')
# name = input('enter your name:')
# age = int(input('enter your age:'))
# greet(name, age)
# def greet(name='atul', age='3'):
#     print(f'hi,my name is {name},age is {age}')
# greet()
###########################################################
# def area(radius):
#     return 3.142*radius*radius
# def vol(area, length):
#     print(f'the vol of the circle is {area*length}')
#     print(f'the area of the circle is {3.142*radius*radius}')
# radius = int(input('enter the radius:'))
# length = int(input('enter the length:'))
# vol(area(radius), length)
#######################################################################################################

# variable scope:scopes define the area of the zone that a variable can be accessed in.
# my_name = 'sia'  # GLOBAL SCOPE
# def print_name():
#     print('inside function name is', my_name)
# print_name()
# print('outside function name is', my_name)

# my_name = 'sia'  # GLOBAL SCOPE
# def print_name():
#     my_name = 'dia'  # LOCAL SCOPE
#     print('inside function name is', my_name)
# print_name()
# print('outside function name is', my_name)

# my_name = 'sia'  # GLOBAL SCOPE
# def print_name():
#     global my_name #override global scope
#     my_name = 'dia'  # LOCAL SCOPE
#     print('inside function name is', my_name)
# print_name()
# print('outside function name is', my_name)
#############################################################################
# Dictionary:mapping type,set of key-value pair - like JS obj notation
# fruit_color = {'mango': 'yellow', 'apple': 'red',
#                'guava': 'green', 'dates': 'brawn'}
# print(fruit_color['apple'])
# print('guava' in fruit_color)     # 'key' in dict
# key = list(fruit_color.keys())
# print(key)
# print(fruit_color.values())
# fruit_color['stawberry'] = 'red'
# print(fruit_color)
####################################################################
# person = dict(name="mou", age=24, color='black')
# print(person)

# def intro(dictionary):
#     for key, val in dictionary.items():
#         print(f'I am {key},I am {val} years old.')
# person = {}
# while True:
#     name = input('enter your name:')
#     age = input('enter ur age:')
#     person[name] = age
#     another = input('add another?(y/n)')
#     if another == 'y':
#         continue
#     else:
#         break
# intro(person)
########################################################################
# nums = [1, 1, 8, 90, 56, 78, 34, 9, 5, 3, 66, 4, 15, 34]
# print(sorted(nums))     #In order
# print(set(nums))   #remove duplicates bt not in order
# names = ['apple', 'May', 'Aviya', 'bat', 'wannuy','zeya', 'Zia']   # sorted by capitalize
# print(set(names))
# print(sorted(names))

# def name_count(dictionary):
#     names = list(dictionary.keys())
#     for n in set(names):
#         num = names.count(n)
#         print(f'there are {num} {n} present')
# person = {}
# while True:
#     name = input('enter your name:')
#     age = input('enter ur age:')
#     person[name] = age
#     another = input('add another?(y/n)')
#     if another == 'y':
#         continue
#     else:
#         break
# name_count(person)

#####################################################################################
# Class is the blueprint of creating objs or instances.
# name = 'gaurv'
# age = 34
# num = {1, 2, 3, 4, 5}
# print(type(num))
# print(name.upper())
#######################################################

# class Personality:  # starts capital
#     def __init__(self):  # define init function,new obj of this class
#         self.name = 'Mou'
#         self.age = 24
#         self.work = 'IT'
#         self.tech = 'automation'
#     def own(self):
#         return f'{self.name} is in {self.tech} team'

# person = Personality()
# print(f'Name is:{person.name}')
# print(f'age is:{person.age}')
# print(person.own())

# personX = Personality()
##################################################
# class Personality:  # starts capital
#   shape = "round"   #class attribute can call any where
#     def __init__(self, name, age, work, tech):  # define init function,new obj of this class
#         self.name = name  #instance attribute
#         self.age = age
#         self.work = work
#         self.tech = tech
#     def own(self):
#         return f'{self.name} is in {self.tech} team'
# person = Personality('Mou', 24, 'IT', 'automation')
# print(f'Name is:{person.name}')
# print(f'age is:{person.age}')
# print(person.own())
# Sky = Personality('Sky', 26, 'Art', 'Artist')
# print(f'Name :{Sky.name}')
# print(f'Age:{Sky.age}')
# print(f'Work:{Sky.work}')
# print(f'Tech:{Sky.tech}')
# print(Sky.own())
# print(Personality.shape)

#######################################################################
# class Personality:  # starts capital
#     shape = "round"  # class level attribute can call any where :INSTANCE + CLASS

#     def __init__(self, name, age, work, tech):  # define init function,new obj of this class
#         self.name = name  # instance attribute because diff from each instance
#         self.age = age
#         self.work = work
#         self.tech = tech

#     def own(self):
#         return f'{self.name} is in {self.tech} team'

#     @classmethod  # decorator -commmon for all
#     def commons(cls):  # access to class level attribute
#         return f'all shapes are {cls.shape}'

#     # static method is kind of decorators which doesn't have access to self or class level attribute.Only access to the parameter which are passing through it individually.
#     @staticmethod
#     def spin(speed='2000 miles per hr'):
#         return f'spins speed is {speed}'


# person = Personality('Mou', 24, 'IT', 'automation')
# # print(f'Name is:{person.name}')
# # print(f'age is:{person.age}')
# # print(person.own())
# Sky = Personality('Sky', 26, 'Art', 'Artist')
# # print(f'Name :{Sky.name}')
# # print(f'Age:{Sky.age}')
# # print(f'Work:{Sky.work}')
# # print(f'Tech:{Sky.tech}')
# # print(Sky.own())
# # print(Personality.shape)
# # print(Personality.commons())
# # print(Sky.commons())
# # print(Personality.spin())
# # print(Sky.spin('a very high speed'))

########################################################
# packages:collection of Modules
# from <filename> import <classname>
# from basic import Personality  # from <filename> import <classname>
# from space.planet import Personality  # folder.file
# from space.calc import planet_mass, planet_vol
# Sky = Personality('Sky', 26, 'Art', 'Artist', 10, 2)
# # print(f'Name:{Sky.name}')
# # print(Sky.spin('a very high speed'))


# Sky_mass = planet_mass(Sky.gravity, Sky.radius)
# Sky_vol = planet_vol(Sky.radius)
# print(f'{Sky.name} has a mass of {Sky_mass} and vol of {Sky_vol}')


###################################################################
# List comprehension: alternative ways to constract list and dictonary based on collection
# prizes = [5, 10, 100, 500, 1000]
# dbl_prizes = []
# for prize in prizes:
#     dbl_prizes.append(prize*2)
# print(dbl_prizes)

# # comprehension method
# dbl_prizes = [prize*2 for prize in prizes]
# print(dbl_prizes)

# # squaring numbers
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# squared_even_nums = []
# for num in nums:
#     if(num ** 2) % 2 == 0:
#         squared_even_nums.append(num ** 2)
# print(squared_even_nums)

# # comprehension method
# squared_even_nums = [num ** 2 for num in nums if(num ** 2) % 2 == 0]
# print(squared_even_nums)

############################################################################
# Map: way to take a list apply some kind of function to each item within that list to change the items and spit out a new list with those updated items within it.
# map(function,data)

# from random import shuffle
# from pyparsing import Word
# def jumble(word):
#     anagram = list(word)
#     shuffle(anagram)
#     return''.join(anagram)
# words = ['beetroot', 'carrots', 'potatoes']
# anagrams = []

# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

#print(list(map(jumble, words)))

#print([jumble(word) for word in words])
#####################################################################

# grades = ['R','A','B','F','S','M','A','F']
# def remove_fails(grade):
#     return grade!= 'F'

# print(list(filter(remove_fails,grades)))

# filtered_grades = []
# for grade in grades:
#     if grade != 'F':
#         filtered_grades.append(grade)
# print(filtered_grades)

#print([grade for grade in grades if grade!='F'])


##############################################################################################
# LAMDAS:like inline anonymous function,don't need name or identifier.
# nums = [1, 2, 3, 4, 5, 6]
# def square(n):
#     return n*n
# print(list(map(square, nums)))

# nums = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda n: n*n, nums)))

###########################################################
# Decorators: extend the behaviour of function without modifying the function itself.
# def cough_dec(func):
#     def func_wrapper():
#         # code before function
#         print('*cough*')
#         func()
#         # code after function
#         print('*cough*')
#     return func_wrapper
# @cough_dec
# def question():
#     print('whats ur name?')
# @cough_dec
# def answer():
#     print('I m gimi')
# question()
# answer()

#############################################################
# Reading Files:
# ipsum_file = open(
#     'C:/Users/moumita.nemo/OneDrive - HCL Technologies Ltd/Documents/practice/python/loremsum.txt')
# # for line in ipsum_file:
# #     print(line.rstrip())
# # ipsum_file.seek(0)
# # lines = ipsum_file.readlines()
# # print(lines)

# ipsum_file.seek(50)
# file_text = ipsum_file.read(100)
# print(file_text)

# ipsum_file.close()

# def sequence_filter(line):
#     return 'Lorem' not in line
# with open('C:/Users/moumita.nemo/OneDrive - HCL Technologies Ltd/Documents/practice/python/loremsum.txt') as ipsum_file:
#     lines = ipsum_file.readlines()
#     print(list(filter(sequence_filter, lines)))
########################################################################
# Writing Files:
# with open('C:/Users/moumita.nemo/OneDrive - HCL Technologies Ltd/Documents/practice/python/write.txt', 'w') as write_file:
#     write_file.write('Python has many scope')

# with open('C:/Users/moumita.nemo/OneDrive - HCL Technologies Ltd/Documents/practice/python/write.txt', 'a') as write_file:
#     write_file.write('\n Everybody should learn python.')

# quotes = ['\n Python is a high-level general-purpose programming language.'
#           '\n Its design philosophy emphasizes code readability with the use of significant indentation.'
#           '\n Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.']
# with open('C:/Users/moumita.nemo/OneDrive - HCL Technologies Ltd/Documents/practice/python/write.txt', 'a') as write_file:
#     write_file.writelines(quotes)
#############################################################################


# import pandas as pd
# dataframe:rows and columns(like database)of data,backbone of pandas.
# series:column
# df = pd.read_csv('location')
# df.shape
# df = pd.DataFrame(df)
# df.loc[1]
# df.iloc['a']

# arr = [[1,2,3],[4,5,6]]
# arr1 = pd.DataFrame(arr)
# arr1
# arr1.index = ['a','b']
# arr1 = pd.DataFrame(arr,index = ['c','d'])
# arr1.columns = ['x','y','z']

import pandas as pd
df = pd.read_csv(
    'C:\\Users\\moumita.nemo\\OneDrive - HCL Technologies Ltd\\Documents\\practice\\python\\pandas\\Data\\survey_results_public.csv')
# print(df)
# print(df.shape)
print(df.info())
