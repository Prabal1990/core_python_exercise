
# .title() cannot be use in list
# List:|||||||||||||||||
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1].title())
# format-strings
# Exercise:
# output -"My first bicycle was a Trek. 
my_cycle = f"My first bicycle was a {bicycles[3].title()}."

# Exercise:
motorcycles = ['honda', 'yamaha', 'suzuki']
# output: ['ducati', 'yamaha', 'suzuki']
# sol:
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# LOOPING
magicians = ['alice', 'david', 'carolina'] 
# output- Alice, that was a great trick! 
# output- I can't wait to see your next trick, Alice. 
for i in magicians:
    # print(i, "that was a great trick!")
    print(f"{i.title()},that was a great trick! ")
    print(f"I can't wait to see your next trick, {i.title()}.\n")

# print(f"Hello, {fullname.title()}!")

# |||||||||||||range()  ||||||||||||||
number= list(range(1,5))
# output: [1, 2, 3, 4]
print(number)
num = list(range(1,10,4))
# it will give you a gap 0f 4
print(num)
# output:[1, 5, 9]
#printing even number
even_num = list(range(2,11,2))
print(even_num)

# |||||| Print Squares of even numbers ||||||||||||
# print this- list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# []
# [i]
# [i**2]
# [i**2.append]
list1 = []
for i in range (1,11):
    square  = i**2
    list1.append(square)
print(list1)
# or
list1 = []
for i in range(1,11):
    square = list1.append(i**2)
print(list1)
# to print in 1 line
list1 = [i**2 for i in range(1,11) ]
print(list1)

# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
# output is below:
# here are the first three players on my team: 
# Charles 
# Martina 
# Michael
print("Here are the first three players on my team:")
for i in players[0:3]:
    print(i.title())


cars = ['audi', 'bmw', 'subaru', 'toyota']
# print: Audi
# BMW
# Subaru
# Toyota
for i in cars:
    if i == "bmw":
        print("BMW")
    else:
        print(i.title())

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
# output- "Marie, you can post a response if you wish"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

# Example
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for club")
else:
    print("Not eligible")

