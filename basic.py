#print('hello world')
# Everything in python is considered as object.Objects have attributes and functions.
# the size,color,speed of car are the attributes,car is object,function are drive,brake,accelerate.
# Functions wrt these objs are called methods.so every obj has attributes and methods.
# a = 6.7
# print(type(a))
# b = 5/5   ## in python3 division result is always float value.
# print(b)
# c = 3 // 3  ## print int division
# print(c)
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
# color = 'blue,black,white'
# print(color.split('a'))
# print(len(p))
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]
l = l1+l2
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
# FORMAT METHOD
# n1 = 3.14257890
# n2 = 10.2345678
# print('n1 is {0:.4} and n2 is {1:.3}'.format(n1, n2))
# # USING F-STRINGS
# print(f'num1 is {n1:.3} and num2 is {n2:.4}')
# age = int(input('enter ur age:'))
# if (age > 18 and age < 60):
#     print('you are eligible')
# elif (age > 60):
#     print('you are free')
# else:
#     print('you are not eligible')

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