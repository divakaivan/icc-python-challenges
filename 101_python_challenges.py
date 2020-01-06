# 1) A Puzzling algorithm
#
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
#
# a = a + b
# b = a - b
# a = a - b
#
# print(f"a = {str(a)}")
# print(f"b = {str(b)}")
#

# 2) The box swap puzzle
#
# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter another number: "))
#
# if n1 < n2:
#     temp = n1
#     n1 = n2
#     n2 = temp
#
#
# print(f"n1 = {str(n1)}")
# print(f"n2 = {str(n2)}")

# 3) three numbers sort
# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter a number: "))
# n3 = int(input("Enter a number: "))
#
# if n1 > n2:
#     temp = n1
#     n1 = n2
#     n2 = temp # n2 is n1 and n1 is n2
#
# if n2 > n3:
#     temp = n2
#     n2 = n3
#     n3 = temp # n2 is n3 and n3 is n2
#
# if n1 > n2:
#     temp = n1
#     n1 = n2
#     n2 = temp # n1 is n2(which is n3) and n2 is n1
#
# print(f"n1 = {str(n1)}")
# print(f"n2 = {str(n2)}")
# print(f"n3 = {str(n3)}")

# 4) original price calculator

# def original_price(price, percent):
#     print(f"Your original price is {price / (1 - percent/100)}")
#
# original_price(10,10)

# 5) weight on the moon calculator

# def moon_weight(w_on_earth):
#     print(f"Your weight on the moon is {(w_on_earth/ 9.81)*1.622}")
#
# moon_weight(82)


# 6) complementary colours algorithm

# def complementary_rgb_color(r,b,g):
#     print(f"red: {r}")
#     print(f"blue: {b}")
#     print(f"green: {g}")
#
#     print(f"complementary red: {255 - r}")
#     print(f"complementary blue: {255 - b}")
#     print(f"complementary green: {255 - g}")
#

# 7) entry fees calculator
#
# adults = int(input("number of adults: "))
# children = int(input("number of children: "))
#
# cost = adults * 15 + children * 11
#
# if cost >= 50:
#     cost = cost * 95/100
# print(f"total cost is {str(cost)}")

# 8) stopping distance calculator
#
# speed = int(input("Enter your speed: "))
# mps = speed / 2.237
#
# stop_d = mps*1.5 + mps**2/2*0.7*9.81
# print(f"your stopping distance is: {str(int(stop_d))}")
#

# 9) mixed numbers challenge
# num = int(input("enter numerator: "))
# denom = int(input("enter denominator:"))
# if num >= denom:
#     print("this is an improper fraction")
#     quotent = num // denom
#     remainder = num/denom
#     if remainder > 0:
#         print(f"{str(quotent)} {str(remainder)} / {str(denom)}")
#     else:
#         print(f"{str(quotent)}")
# else:
#     print("this is a proper fraction")

# 10) area calculator
#
# shape = input("What is the shape: ").lower()
#
# if shape == "square":
#     width = float(input("width:"))
#     print(f"area is {str(width**2)}")
# elif shape == "circle":
#     radius = float(input("radius: "))
#     print(f"area is {str(radius*3.14)}")
# else:
#     print("no such figure")

# 11) type of angle
#
# angle = int(input("enter an angle between 0 and 360: "))
#
# if 0 < angle < 90:
#     print("this is an acute angle")
# elif angle == 90:
#     print("this is a right angle")
# elif 90 < angle < 180:
#     print("this is an obtuse angle")
# elif angle == 180:
#     print("this is a straight angle")
# elif 180 < angle < 360:
#     print("this is a reflex angle")
# else:
#     raise Exception("try entering an angle between 0 and 360")

# 12) atm algorithm
# money = int(input("enter amount to get from ATM: "))
# if (money % 10) != 0:
#     print("you can only get multiples of 10")
# else:
#     if not 10< money < 200:
#         print("you can only withdraw only between 10 and 200")
#     else:
#         notes20 = money // 20
#         notes10 = int((money % 20) / 10)
#         print(f"20 notes: {str(notes20)}")
#         print(f"10 notes: {str(notes10)}")

# 13) auto petrol pump algorithm
#
# import random
# current_fuel = random.randint(0,55)
# print(f"your current fuel is {current_fuel}")
#
# tank_capacity = 55
# fuel_choice = input("what fuel do you need? : ")
# price = 0
# if fuel_choice == "A":
#     price = 1.17
# elif fuel_choice == "B":
#     price = 1.27
# elif fuel_choice == "C":
#     price = 1.21
# elif fuel_choice == "D":
#     price = 1.34
# else:
#     raise Exception("invalid input")
# full_tank = input("do you want to fill full tank ? (yes or no)")
#
# if full_tank.lower() == "yes":
#     quantity_needed = tank_capacity - current_fuel
# else:
#     quantity_needed = int(input("how many litres do you want: "))
#     if (current_fuel + quantity_needed) > tank_capacity:
#         quantity_needed = tank_capacity - current_fuel
# cost = quantity_needed * price
#
# print(f"please pay: {cost}")

# 14,15,16) padlock code challenge
# code = 0
# for i in range(1, 41):
#     code += 1
#
# code2 = 0
# for n1 in range(0, 10):
#     for n2 in range(0, 10):
#         for n3 in range(0, 10):
#             if n1 < n2 < n3:
#                 code2 += 1
#
# code3 = 0
# for n1 in range(0, 10):
#     for n2 in range(0, 10):
#         for n3 in range(0, 10):
#             if (n1 %2==0) and (n2 %2==0) and (n3 %2==0):
#                 code3 += 1
#
# code4 = 0
# for n1 in range(0, 10):
#     for n2 in range(0, 10):
#         for n3 in range(0, 10):
#             if (n1+n2+n2) % 2 == 1:
#                 code4 += 1
#
# code5 = 0
# for n1 in range(0, 10):
#     for n2 in range(0, 10):
#         for n3 in range(0, 10):
#             if (n1 == n2) or (n1 == n3) or (n2 == n3):
#                 code5 += 1
#
# code6 = 0
# for n1 in range(0, 10):
#     for n2 in range(0, 10):
#         for n3 in range(0, 10):
#             if n1==(n2+n3) or n2==(n1+n3) or n3==(n1+n2):
#                 code6 += 1
#
# code7 = 0
# n = 0
# while code < 100:
#     n += 1
#     code7 = n**2

# 17) finding factors of...
# n = int(input("enter a number: "))
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

# 18) star rating validation
# def input_number(message):
#     while True:
#         try:
#             user_input = int(input(message))
#         except ValueError:
#             print("not an integer. try again")
#             continue
#         else:
#             return user_input
#
#
# star_rating = input_number("enter a rating between 0 and 5: ")
# while 0 > star_rating > 5:
#     print("invalid star rating. try again")
#     star_rating = input_number("enter a rating between 0 and 5: ")
#
# print("Thanks")

# 19) pomodoro timer
# from time import sleep
# interval = 25*60 # 25mins
# short_break = 5*60 #5mins
# long_break = 30*60 #30mins
#
# task = input("What is your task: ")
# print(f"Your task is {task}")
# checkmarks = 0
# carry_on = "yes"
#
# while carry_on == "yes":
#     print("Starting pomodoro timer(25 min)")
#     sleep(interval)
#     print("End of pomodoro interval")
#     checkmarks += 1
#     print(f"Checkmarks are {str(checkmarks)}")
#
#     if checkmarks == 4:
#         print("Take a long break")
#         sleep(long_break)
#         checkmarks = 0
#     else:
#         print("Take a short break")
#         sleep(short_break)
#     carry_on = input("Do u want to carry on ? (yes or no) \n")
#
# print("bye bye")

# 20) bidding process

# current_bid = 0
# bidding = True
#
# while bidding:
#     user_input = input("Would you like to place a bid? (yes or no) ")
#     if user_input.lower() == "yes":
#         new_bid = int(input("How much would you like to bid? "))
#         if new_bid > current_bid:
#             current_bid = new_bid
#         else:
#             print(f"invalid bid. Bid must be higher than current one. Current one is {current_bid}")
#         print(f"Current bid is {current_bid}")
#     else:
#         bidding = False
# print(f"Final bid is {current_bid} \nThanks for playing")

# 21) Euler's number
#1.
# n = 100000000
# e = (1+1/n)**n
# print(e)
#2.
# e = 1
# quotient = 1
# for i in range(1, 100):
#     quotient *= i
#     e += 1/quotient
# print(e)
# 22) blackbeard map
#
# for row in range(2440, 2770):
#     for col in range(750, 770):
#         if (row*col) == 1889121:
#             print("The location is")
#             print(f"Row: {str(row)}")
#             print(f"Col: {str(col)}")

# 23) min, max,range, mean, median
#
# import statistics as stat
# def get_stats(list_of_n):
#     print(f"Min is: {min(list_of_n)}")
#     print(f"Max is: {max(list_of_n)}")
#     print(f"Length is: {len(list_of_n)}")
#     print(f"Mean is: {stat.mean(list_of_n)}")
#     print(stat.mode(list_of_n))
# get_stats([1,2,5,3,5,12])

# 24) protractor challenge
# import turtle
# my_pen = turtle.Turtle()
# my_pen.shape("turtle")
# my_pen.speed(100000)
# my_pen.color("#333333")
# my_pen.penup()
# my_pen.goto(-10, 0)
# my_pen.pendown()
# my_pen.setheading(0)
# my_pen.forward(20)
# my_pen.penup()
# my_pen.goto(0, -10)
# my_pen.pendown()
# my_pen.setheading(90)
# my_pen.forward(20)
# my_pen.penup()
# my_pen.write("hi")
#
# my_pen.hideturtle()

# 25 26 27) moroccan mosaic
# insane
# import turtle
# my_pen = turtle.Turtle()
# my_pen.shape("arrow")
# my_pen.speed(1000)
# def draw_mosaic(color, n_of_sides, size, n_of_iters):
#     my_pen.color(color)
#     for i in range(0, n_of_iters):
#         for j in range(0, n_of_sides):
#             my_pen.forward(size)
#             my_pen.left(360/n_of_sides)
#         my_pen.left(360/n_of_iters)
#
# draw_mosaic("#333333", 5, 100, 250)


# 28) splash screen and progress bar
#
# import os
# import time
# def progress_bar(seconds):
#     for progress in range(0, seconds+1):
#         percent = (progress * 100) // seconds
#         print("\n")
#         print("Loading...")
#         print("<" + ("=" * progress) + (" " * (seconds - progress)) + "> " + str(percent) + "%")
#         print("\n")
#         time.sleep(1)
#         os.system('clear')
#
# def splash_screen(seconds):
#     print("\n")
#     print(" *******************")
#     print(" *                 *")
#     print(" *  SPLASH SCREEN  *")
#     print(" *       V1.0      *")
#     print(" *                 *")
#     print(" *******************")
#     time.sleep(seconds)
#     os.system('clear')
#
# splash_screen(3)
# progress_bar(3)
# username = input("Type your username: ")

# 29) how many bytes in...
#
# def kb_to_b(kb):
#     return 1024 * kb
# def mb_to_b(mb):
#     return 1024*1024*mb
# def gb_to_b(gb):
#     return mb_to_b(gb)*1024

# 30) binary shifts

# binary = int(input("Enter an 8-bit binary number: "))
# shift = input("What type of shift, left or right: ")
#
# def left_shift(binary, digits):
#     for i in range(0, digits):
#         binary = binary[1:8]
#         binary += "0"
#     return binary
# def right_shift(binary, digits):
#     for i in range(0, digits):
#         binary = binary[0:7]
#         binary = "0" + binary
#     return binary

# 31) binary permutations
#
# def binary_permutations(n_bits, binary=""):
#     if n_bits > 0:
#         binary_permutations(n_bits-1, binary+"0")
#         binary_permutations(n_bits-1, binary+"1")
#     else:
#         print(binary)
# binary_permutations(4)

# 32) factorial challenge

# def factorial(n):
#     if n == 0: return 1
#     total = 1
#     for i in range(1, n+1):
#         total *= i
#     return total
#
# def recurs(n):
#     if n == 0: return 1
#     if n > 1:
#         return n * recurs(n-1)
#     else:
#         return n
#
# print(recurs(5))

# 33) my class register
#
# def register(pupils):
#     student_dict = {}
#     for i in pupils:
#         attending = input(f"Is {i} attending (y or n): ")
#         student_dict[i] = attending
#     print(f"Total number of students is {len(pupils)}")
#     print(f"The number of students attending is {sum(v == 'y' for v in student_dict.values())}")
#     print(f"The number of students absent is {sum(v == 'n' for v in student_dict.values())}")
# print(register(["ivan", "john", "shaun", "phil"]))

# 34) weather stats challenge
#
# quebec = [["January", -11.1, 83], ["February", -9.7, 71], ["March", -3.8, 71], ["April", 4.1, 71], ["May", 11.2, 80],
#           ["June", 16.6, 114], ["July", 19.9, 117], ["August", 8, 107], ["September", 13.3, 105], ["October", 7.3, 82],
#           ["November", 0.5, 93], ["December", -8.1, 107]]
# # month, avg. temperature, rainfall
# import statistics
#
# avg_year_temp = statistics.mean(i[1] for i in quebec)
#
# hottest_month = max(i[1] for i in quebec)
#
# total_rainfall = sum(i[2] for i in quebec)
#
# avg_rainfall = statistics.mean(i[2] for i in quebec)
#
# coldest_month = min(i[1] for i in quebec)
#
# dif_wet_and_dry = max(i[2] for i in quebec) - min(i[2] for i in quebec)
#
# max_rainfall = 0
# max_rainfall_month = ""
# wettest_avg_temp = 0
# for i in range(0, 12):
#     if quebec[i][2] > max_rainfall:
#         max_rainfall = quebec[i][2]
#         max_rainfall_month = quebec[i][0]
#         wettest_avg_temp = quebec[i][1]
#
# avg_winter_temp = statistics.mean(i[2] for i in quebec if i[0] in ["December", "January", "February"])
# print(avg_winter_temp)

# 35) colour difference formula
#
# r = int(input("enter red code"))
# g = int(input("enter green code"))
# b = int(input("enter blue code"))
#
# shortest_dist = 3*255**2+1
# closest_color = ""

# 36) top 3 countries
#
# largest = ["Russia", "Canada", "USA"]
# guesses = []
#
# carry_on = True
# while carry_on:
#     user_input = input("Enter a guess: ")
#     if user_input == "x":
#         print("You ended the game.")
#         carry_on = False
#     elif user_input in largest and user_input not in guesses:
#         print(f"Yes, {user_input} is one of the top 3")
#         guesses.append(user_input)
#         print(f"Your guesses so far are: {guesses}")
#     elif user_input in guesses and user_input in largest:
#         print(f"Sorry, you have already put in {user_input}")
#     else:
#         print(f"{user_input} is not in the top 3")

#new one
#
# decrypt_me = "TIIAERTESGHSSSCEMSAE"
# first = decrypt_me[:len(decrypt_me)//2]
# last = decrypt_me[len(decrypt_me)//2:]
#
# decrypted = ""
# for x,y in zip(first, last):
#     decrypted += f"{x}{y}"
# print(decrypted)
#

# 62) credit card validity

# number = "4921817171391514"
#
# number = [int(i)*2 if number.index(i) % 2 == 0 else int(i) for i in number]
# print(number)
# number = [1+(i-10) if i > 10 else i for i in number]
# print(sum(number))
# if sum(number) % 10 == 0:
#     print("correct")

from random import randint

def random_n(n):
    range_start = 10 ** (n-1)
    range_end = (10**n) - 1
    return str(randint(range_start, range_end))

def get_luhn_number():
    while True:
        eight_digit = random_n(16)
        # *2 of even positioned numbers
        eight_digit = [int(i)*2 if eight_digit.index(i) % 2 == 0 else int(i) for i in eight_digit]
        # turning 2 digit numbers to one digit
        eight_digit = [1+(i-10) if i >= 10 else i for i in eight_digit]
        if sum(eight_digit) % 10 == 0:
            yield eight_digit

f = get_luhn_number()
x = False
while not x:
    x = next(f)

import itertools

def get_n_luhn_numbers(n):
    luhn_numbers = list(itertools.islice(get_luhn_number(), n))
    return luhn_numbers






















































