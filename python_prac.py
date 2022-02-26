#print('hello')
# def myfunc():
#     global x
#     x = 'fantastic'
# myfunc()
# print('python is' + x) 
#x=1j
#print(type(x))
#z = -67
#print(type(z))
#import random 
#print(random.randrange(1,10))
#for x in 'banana':
    #print(len(x))
#b='hello'
#print(b[-2:5])
#a='hello'
#print(a.replace('e','K'))
#age = 23
#txt = 'my age is {}'
#print(txt.format(age)
#------------------------------if else-----------------------------------------#
'''a=67
b=4
if a>b:
    print('a is greater than b')
else:
    print('a is not  greater than b')    
x='hello'
print((bool(x)))
l1 = ['a',34,8.9,1+6j]
print(l1[3])
print(type(l1))
list = ['apple','banana','mango','lichi','pipeapple']
print(list[-1])
print(list[0:3]) 
list = ['apple','banana','mango','lichi','pipeapple']
list.remove('apple')
print(list) 
mytuple = ('apple','banana','mango','lichi','pipeapple')
print(len(mytuple))
print(type(mytuple))
print(mytuple[2:4])  
a = 5
b = 2
print('the reminder is ', a%b) '''
#-------------------------Even/Odd-------------------------------#
'''

num = int(input('enter a no \n'))
if(num %2) == 0:
    print(str(num),'is a Even number')
else:
    print(str(num),'is a odd  number')
 #----------------------------------square root------------------------------#   
num = int(input('enter a no \n'))
squ = num*num
root = squ ** (1/2)
print(squ)
print('the final result is' , root) 
#-----------------------------------prime no------------------------------------#
num =  int(input('enter the number \n'))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, 'is not a prime no')
            break
    else:   
      print(num, 'is a prime no')       
else:
    print(num, 'is not a prime no') 
#-----------------------------Armstrong---------------------------#
num = int(input('enter a no \n'))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
    print(num,'is armstrong no') 
else:
    print(num,'is not a armstrong no')  '''  
#--------------------------letter-------------------#
# letter = '''Dear <|NAME|>,
#  you are selected!
 
# Date: <|DATE|>
# '''

# name = input('enter your name \n')
# date = input('enter Date\n')
# letter = letter.replace("<|NAME|>",name)
# letter = letter.replace("<|DATE|>",date)
# print(letter) 
#--------------tuple--------------#
# t = ('babar','humayun','akbar','jahangir','shah','akbar')
# print(t[1:4])
# print(len(t))
# print(t)
# set = {'cpu','monitor','mouse','speaker','RAM','mouse'}
# print(set)

# f = ('apple','mango','dates')
# (green,yellow,brown) = f
# print(green)
# print(yellow)

# def my_fun():
#     print('hello ')
# my_fun()   

n = int(input())
arr = map(int,input().split())
arr = sorted(arr,reverse = True)
for i in range(len(arr)):
    if arr[i] == arr[0]:
        continue
    else:
        print(arr[i])
        break





















