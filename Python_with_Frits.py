# str_num_a = input('Enter Your First :  ')
# str_num_b = input('Enter Your Second :  ')
# str_num_a = int(str_num_a)
# str_num_b = int(str_num_b)
# overal_result = str_num_a + str_num_b
# print(overal_result)
# plus_number1 = input('Enter case:  ')
# plus_number2 = input('Enter case:  ')

# result_num1 = float(plus_number1)
# result_num2 = float(plus_number2)

# Overal_ban = result_num1 / result_num2
# print(Overal_ban)
# sell_number1 = input('Enter case: ')
# sell_number2 = input('Enter case: ')

# number1 = float(sell_number1)
# number2 = float(sell_number2)
# last_result = number1 * number2

# Collection Data-Type in Python (List && Tuple && Set && Dictionary)
# --------------------------------------------------------

# List  &&             &&  Mutable   && Ordered && Collection
# Tuple &&             &&  Immutable && Ordered && Collection
# Set   &&   Unique    &&  Mutable   && Ordered && Collection
# Dict  &&   Mapped    &&  Mutable   && Ordered && Collection
# List = ['Xiao Yan', 'Chhanun', 'Lin Tong', 'Tang Sang']
# print(List[:2])
# print(List[2:])
# print(List[1:2])
# print(List[2:2])
# print(List[:1])
# print(List[:3])
# print(List[2:3])
# Number = [10, 20, 30, 40, 50]
# print(Number)
# print(len(Number))
# print(10 in Number)
# print(10 not in Number)
# print(sum(Number))
# print(sorted(Number))
# print(min(Number))
# print(max(Number))
# List = ['Xiao Yan', 'Chhanun', 'Lin Tong', 'Tang Sang']
# List[1] = 'Navizcy'
# print(List)
# update-value

# List.insert(2, 'Hello')
# print(List)
# extra-value(start on the number that user put and also deleted the main value)

# List.append('Sorona')
# print(List)
# add-more(start from the end line)

# List.remove('Lin Tong')
# (romove use with latter of the string)
# print(List)
# List.pop(1)
# print(List); (Always use with the number of the main_list)


# List_number = [
#     [0, 0, 0],
#     [1, 1, 1],
#     [2, 2, 2],
#     [3, 3, 3]
# ]
# number_1 = List_number[1]
# print(List_number)
# print(number_1)


# List_number.pop(2)
# print(List_number)


# count && index; (using in different ways be aware!)
#


# data_type = {
#     "int": "A count from , like 1,2,3,or 0.1",
#     "Sting": "Dog,like, Googe,fish,1,2,3,or 0.1",
#     "Subject": "Math,English,F7,Biology,Pysice, Khmer",
#     "Class": "H34,J89,F,K4,M1,P2,B3,G7",
#     "Scor": "80,59,70,78,100,95,97,91,89,67",
#     "Book": "1,2,3,4,5,6,7,8,9,10,11",
# }
# print(data_type['int']),
# print(data_type['Scor']),
# print(data_type.get('Book')),
# print(data_type.setdefault('Book')),
# print('Sting' in data_type)
# print('Sting' not in data_type)


# Membership Operator in / not in

# messenger = 'How are you boy and girl that stay in this place'
# print('boy' in messenger)
# print('girl'.upper() in messenger)
# print('girl'.lower() not in messenger)

# a = 10
# b = 3


# print('Value a :  ' + str(a))
# print('Value b :  ' + str(b))


# print("a + b = ", a + b)
# print("a - b = ", a - b)
# print("a * b = ", a * b)
# print("a / b = ", a / b)
# print("a // b = ", a // b)
# print("a % b= ", a % b)
# print("a ** b= ", a ** b)


# List Operator

# Example_1 = ["Chan", "Vana", "Dosok", "brighter"]
# Example_2 = ["Sovanna", "Kolana", "Jammei", "Yusu"]

# Example_3 = Example_1 + Example_2
# print(Example_3)

# Multuple lists
# print(Example_1*10)


# 🪄 It´s time to add logic to python

# Logic - Syntax Basics
# color1 = input('Enter Your Fullname :  ')
# color2 = input('Enter Your Schoolname :  ')

# colors = [color1, color2]


# if color1 == 'Red' and color2 == 'Blue':
#     {
#         print(f' {color1} + {color2} = Dark')
#     }
# elif color1 == 'Green' and color2 == 'Yellow':
#     {
#         print(f" {color1} + {color2} = Red ")
#     }
# elif color1 == 'Dodgerblue' and color2 == 'Sky_blue':
#     {
#         print(f" {color1} + {color2} = Darkgrage")
#     }
# else:
#     {
#         print(
#             "white"
#         )
#     }


# Let play game with me 🪄

# behind_number = 5
# max = 10
# min = 4

# for k in range(3):
#     print("="*50, f'Your priority has {k + 1} / 3')

#     check_result = input(f' Guess from number {min} to {max} :  ')
#     check_result = int(check_result)
#     if check_result < min or check_result > max:
#         print(f' The answer is between {min} and  {max} only')
#     if check_result == behind_number:
#         print('Fantastic! You are difinately got it👍')
#         break
#     elif check_result < behind_number:
#         print('Pleas try again! 😊')
#     elif check_result > behind_number:
#         print('Your guess is so far from the answer!😒')


# Loop come over the list!!

# Container = ['coffee', 'tea', 'green-tea', 'wildbery']
# for k in Container:
#     print(k)
#     print(k.lower(), k.upper())


# Button = 'Main charater in the movie of the years!'
# for okey in Button:
#     lower_okey = okey.lower()
#     upper_okey = okey.upper()
#     print(lower_okey, '-'*10, upper_okey, '*'*5)


#
# course = [
#     ['Lesson 1:01', 'Lesson 1:02', 'Lesson 1:03', 'Lesson 1:04', 'Lesson 2:00'],
#     ['Lesson 2:01', 'Lesson 2:02', 'Lesson 2:03', 'Lesson 2:04', 'Lesson 3:00'],
#     ['Lesson 3:01', 'Lesson 3:02', 'Lesson 3:03', 'Lesson 3:04', 'Lesson 4:00'],
# ]
# for container in course:
#     print(container)
#     for Lesson in container:
#         print(f'Noted: {Lesson}')

#     print('conpleted this line !')
#     print("*"*20)


# for x in range(11):
#     for y in range(11):
#         print(x, y)
# tickets = 100
# min = 1
# max = 100
# while True:
#     Number = input("Buy some tickets :  ")
#     Number = int(Number)

#     if tickets - Number < 0:
#         print('NOt enough tickets. Please try again.')
#         continue
#     tickets -= Number
#     print(f'tickets have left: {tickets}')

#     if tickets == 0:
#         print('Sold out!')
#         break


# while True:
#     student_1 = input('Enter Number:  ')
#     student_2 = input('Enter Number:  ')

#     teacher_1 = int(student_1)
#     teacher_2 = int(student_2)

#     Overal = teacher_1 + teacher_2

#     print(Overal)


# a = 0
# b = 1

# for i in range(10):
#     print(b)
#     c = a + b
#     a = b
#     b = c

# 🥇function in python

# def speak_something():
#     print('Hellow world of coding')

# speak_something()

# 🥈function with Argument/Parameters

# def fullName():
#     name = 'Chhanun'
#     print('hello{}'.format(name))


# fullName()

# 1️⃣this is call parameters in function!
# def fullName(name):
#     print('hello {}'.format(name))


# fullName("Chhanun")
# fullName("Somnang")


# def fullName(name, wellocome=''):
#     print('hello {}{}'.format(wellocome, name))


# fullName("Chhanun", "Mr.")
# fullName("Somnang", "Ms.")


# 2️⃣ this is call return value!

# a = 5
# b = 10

# c = a + b
# print(c)

# a = 5
# b = 10

# c = a + b
# print(a, b, c)

# a = 5
# b = 10

# c = a + b
# print('{} + {} = {}'.format(a,b,c))


# def sumNamber(a, b):
#     total = a + b
#     print('{} + {} = {}'.format(a, b, total))
#     return total

# x = sumNamber(5, 5)
# print(x)


# def sumNamber():
#     a = 1
#     b = 3
#     total = a + b
#     print(total)


# sumNamber()


# 🪄print(dir(str)) ['capitalize', 'casefold','center', 'count']


# x = 45
# y = 'Chhanun'
# z = ['some', 'one', 'body']

# if isinstance(x, (int, float)):
#     print(x**2)

# for k in range(10):
#     print(k, "You are so good!")


# x = 1.97878
# y = 9.12344
# z = 7.46579
# print(x, y, z)

# x = round(x)
# y = round(y)
# z = round(z)
# print(x, y, z)


# number = [5, 2, 8, 3, 1, 7, 4]
# print(sorted(number))
# print(sorted(number, reverse=True))

# materials = {
#     'Steel : 150',
#     'Concrate : 70',
#     'Wood : 60',
#     'Brick : 30',
# }


# def getting_value(items):
#     return items[1]


# sorted_value = sorted(getting_value.items(), key=getting_value)

# 🪄 How to use zip()

# container = ['Food', 'drink', 'vagetable']
# amounts = ['20', '60', '90']
# Zip_fullitems = zip(container, amounts)
# new_items = list(Zip_fullitems)
# print(new_items)

# container = ['Food', 'drink', 'vagetable']
# amounts = ['20', '60', '90']
# Zip_fullitems = (container, amounts)
# new_items = list(Zip_fullitems)
# print(new_items)

# container = ['Food', 'drink', 'vagetable']
# amounts = ['20', '60', '90']
# Zip_fullitems = zip(container, amounts)
# new_items = (Zip_fullitems)
# print(new_items)


# for container, amounts in zip(container, amounts):
#     print(container, amounts)

#  🪄This is how filter() effected in pythob! and list property
# def call_list(number):
#     return number % 2 == 0


# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_number = filter(call_list, number)
# print(list(even_number))

# 🪄 simple for return value with parameters() and list() property
# def call_list(number):
#     return number % 2 != 0
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_number = (number)
# print(list(even_number))


# 🪄 This is format() effected!
# text = 'Hellow {} Hackers.'.format('python')
# print(text)

# text2 = "{a},{b},{c}".format(
#     a="This is a coding",
#     b='Not too bad!',
#     c='Even easy!'
# )
# print(text2)


# 🪄 this is how index() using!
# text = " She is so beautiful!"
# print(text.index('o'))
# print(text.index('b'))


# 🪄 isUpper and islower (use to found out if the value is True or False only!)
# print("you are the best one in this generation boy!".islower())
# print(" This is the end of coding hah?".islower())
# print(" MY CAR IS GOING TO CRASH".isupper())
# print(" Try your best in order to fix the problem".isupper())


# 🪄 this is the property of using " Join()"

# Items = ['A', 'B', 'C', 'D', 'E', 'F']
# print(''.join(Items))
# print("".join(Items))
# print(" - ".join(Items))
# print(' ,'.join(Items))

# 🪄 Lower and upper is make user string looks better than before!
# print(" my god is going to death lately".upper())
# print(" MY DOG IS GOING TO DEATH LATELY".lower())


# 🪄  this is how to use replace()!
# print("Hellow".replace("l", 'L'))
# print("Wonderful job in this company".replace(
#     'job', "employement").replace("company", "institution"))


# 🪄 this is split() property
# print('Hello all python coder')
# print('Hello all python coder'.split(" "))
# print('Hello all python coder'.split("python"))
# print('Hello all python coder'.split())


# 🪄 this is how strip() using
# print('     hello world of coding') normol value
# print('     hello world of coding'.strip()) strip value!


# 🪄 this is how extend() effected
# list_1 = [1, 2]
# list_2 = [3, 4]
# list_1.extend(list_2)
# print(list_1)

# list_3 = list_1 + list_2
# print(list_3)

# 🪄 this is how insert() use
# list = [1, 3, 5]
# list.insert(1, 2)
# list.insert(3, 4)
# print(list)


# 🪄 this is how copy() in use
# list = [1, 2, 3, 4]
# new_list = list.copy()
# print(list)
# print(new_list)


# 🪄 this is how count() in use
# list = [1, 2, 3, 4]
# list.reverse()
# print(list)

# 🪄 this is how get() in use
# my_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3 }
# my_dect = my_dict.get('c')
# print(my_dect)


# 🪄 this is how items or keys() in use
# my_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3}
# my_dect = my_dict.items()

# 🪄 this is how keys() in use
# my_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3}
# my_dect = my_dict.keys()
# print(my_dect)

# 🪄 this is how value() in use
# my_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3}
# my_dect = my_dict.value()
# print(my_dect)


# 🪄 this is how seftdefault() in use
# my_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3}
# value_c = my_dict.setdefault('c', 3)
# value_d = my_dict.setdefault('e', 'Do not exists')
# print(value_c)
# print(value_d)


# print("="*50)


# def account():
#     Username = input(" Tap Your Name:  ")
#     UserS_id = input(" Tap Your ID:  ")
#     User_address = input(" Tap Your Address:  ")
#     User_gmail = input(" Tap Your Email:  ")
#     print(" This is your information check it again!")
#     print("="*50)

# while True:
#     account()
#     container = input(" Add more informatin Add/Stop ")
#     if container == "Add":
#         print("Let´s fill here")
#         continue
#     elif container == "Stop":
#         print(" Your information is completed!")
#         break
#     else:
#         print(" Text is not found! Please try again.")
#         break


# print("✅ Creat a new account. ")
# userName = input("Username :  ")
# userpassword = input("Userpassword :  ")
# print('='*50)
# symbol = "!@#$%^&*()_{|}?><"
# check_length = False
# check_digit = False
# check_lower = False
# check_upper = False
# check_symbol = False
# check_space = False


# if len(userpassword) >= 8:
#     check_length = True

# if " " not in userpassword:
#     check_space = True

# for char in userpassword:
#     if char.isdigit():
#         check_digit = True

#     elif char.islower():
#         check_lower = True

#     elif char.isupper():
#         check_upper = True

#     elif char in symbol:
#         check_symbol = True

# Check = [check_length,
#          check_digit,
#          check_lower,
#          check_upper,
#          check_symbol,
#          check_space
#          ]


# if all(Check):
#     print("✅ Account created successfully.")
# else:
#     print("❌ Password is not strong enough. ")

#     if not check_length:
#         print(f'  check on text again! {check_length}')

#     if not check_space:
#         print(f'  check on the space again! {check_space}')

#     if not check_digit:
#         print(f'  check digit doesn´t rigth ! {check_digit}')

#     if not check_lower:
#         print(f'  check on lower again! {check_lower}')

#     if not check_upper:
#         print(f'  check in upper again! {check_upper}')

#     if not check_symbol:
#         print(f'  check again! {check_symbol}')
# from openpyxl import *


# def countdown(n):
#     while n > 0:
#         if n < 0:
#             break
#         print(n)
#         n -= 1


# print("Interative")
# countdown(5)

# try:
#     print(1/0)
#     print('hello')

# except ZeroDivisionError:
#     print(' Divind By 0 is not Allowed')
# print("The end!")


# toggle = True
# if toggle:
#     word = "Enable"
# else:
#     word = "disable"

# word = "Enable" if toggle else "Disable"
# print(word)


# toggle = False
# if toggle:
#     word = "Enable"
# else:
#     word = "disable"

# word = "Enable" if toggle else "Disable"
# print(word)


# items = ["a_items", "b_items", "c_items", "d_items"]
# # items_upper = []
# # for item in items:
# #     items_upper.append(item.upper())
# items_upper = [item.upper() for item in items]
# print(items_upper)

# 📝 Note we can use loop in list with this method !!


# items = ["item_a", "item_b", "item_c", "item_d", "wrong_data"]
# items_upper = []
# for item in items:
#     if 'item_' in item:
#         items_upper.append(item.upper())
# print(items_upper)


# items = ["item_a", "item_b", "item_c", "item_d", "wrong_data"]
# items_upper = []
# for item in items:
#     if 'item_' in item:
#         items_upper.append(item.upper())
# items_upper = [item.upper() for item in items if 'item_' in item]
# print(items_upper)


# Subject = ['item_Math', 'item_Biology',
#            'item_Engling', 'item_khmer', 'item_History']
# saball = []
# for item in Subject:
#     if 'item_' in item:
#         saball.append(item.upper())
# print(saball)


# Subject = ['item_Math', 'item_Biology',
#            'item_Engling', 'item_khmer', 'item_History']
# saball = [item.upper() for item in Subject if 'item_' in item]
# print(saball)

# 📝 loop in list with numbers!!
# Numbers = [1, 2, 3, 4, 5]
# num_sq = [num**2 for num in Numbers]
# num_cube = [num**3 for num in Numbers]
# num_cube_even = [num**3 for num in Numbers if num % 2 == 0]
# print(Numbers)
# print(num_sq)
# print(num_cube)
# print(num_cube_even)


# 📝 How to work with text, CSV and JSON file.

# filename = "C:\\Users\\ASUS\\Desktop\\HTML VS CSS\\File-for.Python\\__pycache__\\iterable.py"
# file = open()
# content = file.read()
# print(content)
# file.close()
# with open(filename, 'r') as file:
#     content = file.read()

# print(content)

# for line in enumerate(content. splitlines()):
#     print(line)

# C:\Users\ASUS\Desktop\HTML VS CSS\File-for.Python\__pycache__\iterable.py
# with open(file, 'w') as f:
#     f.write('Hellow world! \n')
#     f.write('Hellow world! \n')
#     f.write('Hellow world! \n')
#     f.write('Hellow world! \n')

# 📝 this is how os work with open file!
# import os
# filename = 'C:\\Users\\ASUS\\Desktop\\HTML VS CSS\\File-for.Python\\__pycache__\\iterable.py'
# if not os.path.exists(filename):
#     print(f'Creating a new file: {filename}')
#     with open(filename, 'w') as f:
#         f.write('hello world \n')
#         f.write('hello world \n')
#         f.write('hello world \n')
#         f.write('hello world \n')
#         f.write('hello world \n')

# else:
#     print("File Exist")
#     print('Content : ')
#     with open(filename, 'r') as f:
#         print(f.read())


# 📝 this is how CSV file work with open file!


# import csv
# filename = 'C:\\Users\\ASUS\\Desktop\\\For Exel'
# with open(filename, 'r') as f:
#     # contents = f.read()
#     # print(contents)

#     for row in filename:
#         print(row)


# 📝this the JSON without

# import json
# with open('C:\\Users\\ASUS\\Desktop\\HTML VS CSS\\File-for.Python\\__pycache__\\iterable.py', 'r') as f:
#     data = json.load(f)
#     print(data)
#     print(type(data))


# 📝 this is how ( wb openpyxl work )


#  this is (how Before())
# with time_it() :
#     result = [ i*2 for i in range(100)]


# with time_it():
#     result = []
#     for i in range(100):
#         result.append(i*2)


# 📝 1️⃣  Learn how to use Logging like a pro.

# import logging
# logging.basicConfig(level=logging.WARNING)
# logging.debug("this is a debug msg")
# logging.info("This is an info msg.")
# logging.warning("this is a warning msg")
# logging.error("this is a error msg.")
# logging.exception("this is an exception msg.")
# logging.critical("this is an critical msg")


# a, b = 10, 20

# logging.debug(f'Executing: {a}/{b}')
# try:
#     c = a/b
#     logging.info(f'Result:{c}')

# except:
#     logging.errroe('Something went wrong!')


# 2️⃣ log to a file.

# import logging
# log_format = '  %(asctime)s - %(levelname)s - %(message)s  '
# logging.basicConfig(level=logging.DEBUG,
#                     format=log_format,
#                     filename="C:\\Users\\ASUS\\Desktop\\HTML VS CSS\\Example.txt")
# logging.debug('This is a debug msg')
# logging.info('This is an info msg.')
# logging.warning('This is a warning msg.')
# print('where are our logging messages')


# 👿 Ready to Excel in your Python skill?
# # https://openpyxl. rpeadthedocs. io/en/stable/
#  openpyxl #Note this line !!
# from openpyxl import*
# -------------------------------------------------------------------------
# filename = 'C:\\Users\\ASUS\\Desktop\\For Exel\\Book1.xlsx'
# wb = load_workbook(filename)
# wb = openpyxl.Workbook()  #Creat new Workbook
# wb.save('text.xlsx')
# -------------------------------------------------------------------------


# 🗒️ get worksheets from Workbook
# -------------------------------------------------------------------------
# ws = wb.active     # get active worksheet
# ws = wb['Sheet2']   # get sheet by name


# all_ws = wb.worksheets # List of Worksheet
# all_ws_names = wb.sheetnames # List of Worksheet
# new_ws = wb.create_chartsheet('NewSheet4')   # Creat a new Worksheet
# So in this way you are only for one times!  if you close the file and start to run it once again it erorr
# ws_to_remove = wb['NewSheet4']
# wb.remove(ws_to_remove)  # for remove worksheet!
# new_ws = wb.copy_worksheet(ws)   # this is how to copy
# new_ws.title = 'New_Sheet'  # Change Worksheet Name

# wb.save(filename)   # Override the file


# ✅  Read data
# -----------------------------------------------------------------------------------
# from openpyxl import load_workbook
# filename = 'C:\\Users\\ASUS\\Desktop\\For Exel\\Book1.xlsx'
# wb = load_workbook(filename)  # Open Existing Workbook
# ws = wb.active   # get active Worksheets

# print(f'Worksheet: {ws.title}')
# print('-'*50)

# Read Specific Cell
# ------------------------------------------
# cell_a1 = ws['A1']
# cell_a2 = ws.cell(row=4, column=4)
# print(cell_a1.value)
# print(cell_a2.value)


# for row in range(10):
#     row_data = []

#     for col in range(10):
#         cell = ws.cell(row=row + 1, column=col + 1)  # tab to complete
#         row_data.append(cell.value)
#     print(row_data)
# for row in range(10):
#     row_data = []

#     for col in range(10):
#         cell = ws.cell(row=row + 1, column=col + 1)  # tab to complete
#         if cell.value:
#             row_data.append(cell.value)
#     print(row_data)

#   loop in row! (rows)
# --------------------------------------------------------------
# for row in ws.iter_rows():
#     print(row)


# for row in ws.iter_rows():
#     row_data = [r.value for r in row]
#     print(row_data)


# How to write Data 📝
# --------------------------------------------------------------
# from openpyxl.comments import *
# from openpyxl.styles import *
# from openpyxl import load_workbook
# wb = load_workbook('C:\\Users\\ASUS\\Desktop\\For Exel\\Book1.xlsx')
# ws = wb.active
# ws["B2"] = "New B2 value"
# ws["B3"].value = "New B3 value"
# ws.cell(row=4, column=2, value='New B4 Value')
# wb.save('C:\\Users\\ASUS\\Desktop\\For Exel\\Book1.xlsx')


# Append Data Row
# n = ws.max_row+1
# ws.append([f'Chhanun', 'Price', 'Linux', 5, 200, '= D{n}*E{n}'])

# wb.save('C:\\Users\\ASUS\\Desktop\\For Exel\\Book1.xlsx')

# Insert / Date Rows or COlumns
# ws.insert_rows(3)
# ws.insert_cols(3)

# ws.delete_rows(3)
# ws.delete_cols(3)


# Move Data
# ws.move_range("A1:B10", rows=5, cols=10)


# Cell Ranges
# -------------------------------------------------------------------
# cell_range = ws['A1':'C2']
# col_C = ws['C']
# col_range = ws['C:D']
# row10 = ws[10]
# row_range = ws[5:10]
# print(cell_range)
# print(col_C)
# print(col_range)
# print(row10)
# print(row_range)

# print('-'*50)

# for items in col_C:
#     print(items)
# for cell in ws['C1:C2']:
#     for c in cell:
#         print(c.value)
# for cell in ws['C']:
#     if cell.value is not None:
#         print(cell.value)
# for row in range(1, 3):
#     print(ws.cell(row=row, column=3).value)
# Styling
# ---------------------------------------------------------------------
# ws['A6'].font = Font(bold=True, color='FF0000', size=24)
# ws['A6'].fill = PatternFill(
#     start_color='FFFF00', end_color='FFFF00', fill_type='solid')
# ws['A6'].alignment = Alignment(horizontal='center')
# ws.merge_cells('B1:D5')  # Merge Cells

# Resize row / column
# ---------------------------------------------------------
# ws.row_dimensions[5].height = 50
# ws.column_dimensions['A'].width = 50


# Add comment

# ws['A5'].comment = Comment('Auto Comment', 'EF')

# Add hyperlink
# ----------------------------------------------------------------------

# ws['A5'].hyperlink = "https://www.python.org"
# ws['A5'].style = 'Hyperlink'
# ws = wb.save('C:\\Users\\ASUS\\Desktop\\For Exel\\Book1.xlsx')


# Final Example
# -----------------------------------------------------------------------
# Data
# from openpyxl.styles import Font
# from openpyxl import load_workbook, Workbook
# import os
# data = [
#     ["Room Number", "Room Name", "Area(sqm)", "Occupancy", "Finishes"],
#     ["101", "Lobby", 35, 50, "Marble Floor"],
#     ['102', "Conference Room", 25, 20, 'Carpe'],
#     ['103', 'office', 15, 5, "Vinyl Flooring"],
# ]
# # Crear a Workbook + Worksheet
# filename = r"C:\Users\ASUS\Desktop\For Exel\For Pythob test.xlsx"
# wb = load_workbook(filename)
# # if os.path.exists(filename):
# #     wb = load_workbook(filename)
# # else:
# #     wb = Workbook()
# ws = wb.active
# ws.title = "EF - Rooms"
# # Separate data
# headings = data[0]
# data = data[1:]
# # from openpyxl import load_workbook
# # wb = load_workbook('C:\\Users\\ASUS\\Desktop\\For Exel\\Book1.xlsx')
# # ws = wb.active
# for col_n, heading in enumerate(headings, start=1):
#     cell = ws.cell(row=1, column=col_n, value=heading)
#     cell.font = Font(bold=True, size=12)
# # Write Data
# for row in data:
#     ws.append(row)

# # # Save workbook
# # filename = r'C:\Users\ASUS\Desktop\For Exel\For Pythob test.xlsx'
# wb.save(filename)
# print(filename)
# print(ws.max_row)


# from openpyxl import load_workbook
# from openpyxl.styles import Font
# Data_top = [
#     ['Name of staff', 'ID', 'Location', 'Room Number', 'Email', 'Phone Number'],
#     ['Chhanun', 'B202020', 'Therk Thaloe', 56,
#         'praveasna1234@gmail.com', '067722071'],
#     ['Rotha', 'B2489249', 'Takmaor', 34, 'rohtavana12342@gmail.com', '098764523'],
#     ['Sokheamg', 'B2439055', 'Prileap', 102,
#         'sokheang5873@gmail.com', '088345712'],
#     ['Darona', 'B2478987', 'Oirjom', 57, 'daronadavith33@gmail.com', '012774563'],
#     ['Vijea', 'B3948576', 'Prileap', 234, 'keyeoli6538@gamil.com', '08845627'],
# ]
# filename = r"C:\Users\ASUS\Documents\Student Room.xlsx"
# wb = load_workbook(filename)
# ws = wb.active
# ws.title = "Student Rent Room"
# # ws.delete_rows(1, ws.max_row)
# headings = Data_top[0]
# for col_n, heading in enumerate(headings, start=1):
#     cell = ws.cell(row=1, column=col_n, value=heading)
#     cell.font = Font(bold=True, size=12)
# for row in Data_top[1:]:
#     ws.append(row)
# wb.save(filename)
# import pandas as pd
# import csv
# df = pd.read_csv(r"C:\Users\ASUS\Desktop\For Exel\For Pythob test.xlsx", index= False)
# print(df)


# from openpyxl import Workbook
# from openpyxl.styles import Font
# Database = [
#     ['Name of staff', 'ID', 'Location', 'Room Number', 'Email', 'Phone Number'],
#     ['Chhanun', 'B202020', 'Therk Thaloe', 56,
#         'praveasna1234@gmail.com', '067722071'],
#     ['Rotha', 'B2489249', 'Takmaor', 34, 'rohtavana12342@gmail.com', '098764523'],
#     ['Sokheamg', 'B2439055', 'Prileap', 102,
#         'sokheang5873@gmail.com', '088345712'],
#     ['Darona', 'B2478987', 'Oirjom', 57, 'daronadavith33@gmail.com', '012774563'],
#     ['Vijea', 'B3948576', 'Prileap', 234, 'keyeoli6538@gamil.com', '08845627'],
# ]
# filename = r"C:\Users\ASUS\Documents\testing.python.xlsx"
# wb = Workbook()
# ws = wb.active
# ws.title = "Information"
# header = Database[0]
# for col, headers in enumerate(header, start=1):
#     cell = ws.cell(row=1, column=col, value=headers)
#     cell.font = Font(bold=True, size=12)
# for row in Database[1:]:
#     ws.append(row)
# wb.save(filename)


# import pandas as pd
# Data_pandas = {
#     "Project Name": [
#         "Burt Khalifa",
#         "Shanghai Towoer",
#         "Phnom Penh City",
#         "Berng Kok Center",
#         "Lotter World Tower"
#     ],
#     "Height(m)": [
#         234,
#         345,
#         546,
#         770,
#         456,
#     ],
#     "Country": [
#         "Cambodia",
#         "China",
#         "Canada",
#         "Australia",
#         "Turkey"
#     ],
#     "City": [
#         "Phnom Penh",
#         "Shanghai",
#         "Mecixco",
#         "Sonayu",
#         "Seoul"]

# }

# # Data_frame📝
# df = pd.DataFrame(Data_pandas)
# print(df)
# df.to_excel(r"C:\Users\ASUS\Documents\Pandas.xlsx", index=False)


# import pandas as pd
# Data_pandasone = [
#     ["Fullname", "Student_ID", "Address", "Major", "Session"],
#     ["Vannak Chhanun", "B2344555", "Terk Tlar", "Computer_Science", "Morning"],
#     ["Sok Heang", "B556664", "Preleap", "Soft_Engineering", "Evening"],
#     ["Ang Soriya", "B2345132", "Leapdue", "Doctor", "After_noon"],
#     ["Tung Sitina", "B4356365", "Sokpeak", "Nurse", "Morning"],
#     ["Hour Staya", "B4635343", "Hourkong", "Technology Information", "Morning"],
#     ["Boun Tearn", "B4456264", "Tourkong", "Software_Engineering", "Morning"],
#     ["Kong Davung", "B2456790", "Tong Kor", "Computer_Science", "Evening"]
# ]

# df = pd.DataFrame(Data_pandasone)
# print(df)
# df.to_excel(r"C:\Users\ASUS\Documents\PandasOne.xlsx", index=False)


# import contextlib


# @contextlib.contextmanager
# def ef_context_manager():
#     print("---Before---")
#     print("---Before---")

#     print("---After---")
#     print("---After---")
#     yield  # take the last result into this line !!
#     print("---After---")
#     print("---After---")


# with ef_context_manager():
#     print("test")

# import contextlib
# import time
# import traceback


# @contextlib.contextmanager
# def time_it():
#     start = time.time()
#     yield
#     end = time.time()
# # for i in range(1000):
# #     pass
#     end = time.time()
#     timer = end-start
#     print(f"Time Taken: {timer}s")


# @contextlib.contextmanager
# def _try_except(debug=False):
#     try:
#         yield
#     except:
#         print(traceback.format_exc())
# with time_it():
#     for i in range(10):
#         print("Hello World")

# # Loop
# with time_it() :

#     result = []
#     for i in range(100):
#         result.append(i * 2)
# # Comprehension
# with time-it():
#     result = [ i * 2 for i in range(100)]


# with _try_except():
#     print(1/0)
# with _try_except(debug=True):
#     print(1/0)
# with _try_except():
#     print(1/0)
# with _try_except():
#     print(1/0)
# with _try_except():
#     print(1/0)


# ✅ Take Noted ! This how to use Logging in Python
# ***************************************************

# DEBUG = 10
# INFO = 20
# WARNING = 30
# ERROR = 40
# CRITIAL = 50

# ***************************************************
# 🗒️ learn how to use logging !!
# ------------------------------------------------------
# import logging
# # Setup Logger
# log_format = '%(asctime)s - %(levelname)s - %(message)s'
# 📱 Log Messages
# logging.debug("This is what I want to learn! msg")
# logging.info(" This is an info msg.")
# logging.warning(" This is a warning msg.")
# logging.error(" This is an error msg.")
# logging.exception(" This is an exception msg")
# logging.critical("This is an critical msg")

# Example
# a, b = 30, 15
# logging.debug(f"Calculate: {a} + {b}")
# try:
#     c = a + b
#     logging.info(f"Calculate: {c}")
# except:
#     logging.exception("This is not available")
# print("Hello world")

#  📱 Log to a file
# -----------------------------------------------------------------
# import logging
# # Setup Logger
# log_format = """
# *** %(levelname)s ***
# Time: %(asctime)s
# Msg : %(message)s
# ----------------------------------------------------------"""
# logging.basicConfig(level=logging.DEBUG,
#                     format=log_format,
#                     filename=r"C:\Users\ASUS\Desktop\HTML VS CSS\File-for.Python\example.txt")
# # Log Messages
# logging.debug(" Section on one page one")
# logging.info("This is an info msg")
# logging.warning("This is a warning msg")
# print("How old are you bro!")


# 📱 Log to

# import logging
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# # formatting
# Log_format = """
# # *** %(levelname)s ***
# # Time: %(asctime)s
# # Msg : %(message)s
# # ----------------------------------------------------------"""
# formatter = logging.Formatter(Log_format)

# # Handler 1 - fileHandler
# file_handler = logging.FileHandler("example.xlsx")
# file_handler.setFormatter(formatter)
# # Handler 1 - StreamHandler
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)

# # Configure Logger

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logger.addHandler(file_handler)
# logger.addHandler(file_handler)

# logger.debug("This is a DEBUG msg")

# Custom logger (Discord)
# ----------------------------------------------------------------------
# import logging , requests
# Webhook - is a way apps to communicate using HTTZP Post requests
# In a nutshell, we can send json data to a URL, and the other app knows to do...


# We have been through OOP in python ✅
# class Element:
#     count_id = 1

#     def __init__(self, w, h, loc, mat):

#         self. width = 12
#         self. height = 20
#         self. location = loc
#         self. material = mat
#         self.id = self.new_gen()

#         print(f" Welcome to OOP in Python! <{self.id}> ")

#     def new_gen(self):
#         el_id = Element.count_id
#         Element.count_id += 1
#         return el_id

#     def print_data(self):
#         print(f" Welcome to OOP in Python! <{self.id}> ")
#         print(f'Material: {self.material}')
#         print(f'Location: {self.location}')
#         print(f'Width: {self.width}')
#         print(f'Height: {self.height}')
#         print("-------")

#     def move(self, x, y):
#         print(f" Moving an Element <{self.id}> X: {x}, Y: {y}")
#         Y_seen = self.location[0]
#         she_seen = self.location[1]

#         # 📝 take note no (self.location = wrong!!)
#         self.location = (Y_seen+x, she_seen+y)


# # 📦 Object Instances Based on Template
# elem_a = Element(12, 20, (9, 9), "wood")
# elem_b = Element(15, 34, (6, 6), "Concrete")

# # print Statements
# elem_a.print_data()
# elem_b.print_data()


# elem_a.move(10, 20)
# elem_a.print_data()


# class student_info:
#     numerber = 1

#     def __init__(self, table_num, room_num, time_sch, subject, session):
#         self.Table = table_num
#         self.Room = room_num
#         self.Schedule = list(time_sch)
#         self.Subject = subject
#         self.Session = session
#         self.New_one = self.student_num()

#     def student_num(self):
#         stu_num = student_info.numerber
#         student_info.numerber += 1
#         return stu_num

#     def show_room(self):

#         print(f" Room Number: < {self.New_one}  > ")
#         print(f" Your table: {self.Table}")
#         print(f" Room: {self.Room}")
#         print(f" Schedule: {self.Schedule}")
#         print(f" Subject: {self.Subject}")
#         print(f" Session : {self.Session}")
#         print("="*50)

#     def Add_data(self, old_one, old_two):
#         print(f" Extra hour:< Old = {old_one}, and Old = {old_two} >")
#         data_one = self.Schedule[0]
#         data_two = self.Schedule[1]
#         self.Schedule = (data_one + old_one, data_two + old_two)


# value_a = student_info(10, 205, [5, 8], "Computer Science", "Evening")
# value_b = student_info(15, 200, [5, 8], "Computer Science", "Morning")

# value_a.Add_data(10, 20)
# value_b .Add_data(30, 40)

# value_a.show_room()
# value_b.show_room()


# ✅🗒️ Let´s Sort Your Messy Downloads Folder!!

# from pathlib import Path
# import os
# # Global Variables
# # -------------------------------------------------------------------
# PATH_DOWNLOADS = r"C:\Users\ASUS\OneDrive\Desktop\HTML VS CSS\File-for.Python\__pycache__"
# PATH_DOWNLOADS = Path.home() / "Downloads"

# Get Downloade Path
# Define Sorting Rules

# CATEGORIES = {
#     "Images": ["jng", "Yao", "Sum"],
#     "Git": ["gifl"],
#     "Videos": ["mp4,", "mkd", "avia", "mov"],
#     "Docs": ["pdf", "docx", "txt"],
#     "zips": ["zip", "Rar", "7ghf"],
#     "Instollaers": ["exe", "msi"],
#     "Code": [".py", ".html", ".js", "CSS", ".md"],
#     "Data": [".csv", "xlsx"]
# }
# # Rread All Files
# for file in os.listdir(PATH_DOWNLOADS):
#     # print(file)
#     sorting_cat = None
#     file_extension = "." + file.split(".")[-1]

#     for cat, list_keywords in CATEGORIES.items():
#         if file_extension in list_keywords:
#             sorting_cat = cat
#             print(cat, file)
#             break
# Get file Catagory ( Basesd on rules)
# Creat Sorting Folder
# Move Files
# Report Results
# Bonus: Create CMD-COmmond


# Super Charge Your Python with AI 🤖🤖
# ⚠️ NEVER hardcode API keys in your code or comments — store them in a .env
#    file that is listed in .gitignore, and load them with dotenv instead.
# 1️⃣ Import what we need
from openai import OpenAI
import os
from dotenv import load_dotenv


# Get API key
# -----------------------------------------------------------------
# Create a .env file next to this script containing:
#   OPENAI_API_KEY=your_real_key_here
# and make sure .env is listed in your .gitignore so it never gets committed.
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Prepare message for AI
tone = "Speak like an old pirate who just woke up and hit his toe on the screen and check it carefully."
question = "List 10 tallest buildings in the world"
msg = f"Style: {tone} message: {question}"
print(f'Asking AI:\n{msg}')
print("*"*50)


client = OpenAI(api_key=OPENAI_API_KEY)
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": msg}
    ]
)
print(response.choices[0].message.content)
#----------------------------------------------------
# The end of the code.
#----------------------------------------------------