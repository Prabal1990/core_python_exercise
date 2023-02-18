# def greet_user():
#     print("Hello!")

# greet_user()

# --------------
def greet_user(username):
    print(f"Hello! {username.title()}")

greet_user("surya")
# greet_user = function
# surya = argument

# -----------------------------------
# def describe_pet(animal_type, pet_name):
#  """Display information about a pet."""
#  print(f"\nI have a {animal_type}.")
#  print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('cat', 'kitty')


# Creating a function:

# def pet_available(pet_type, pet_name):
#     print(f"I have a {pet_type}.")
#     print(f"My {pet_type}'s name is {pet_name.title()}.")

# pet_available("dog", "tipu")
# pet_available(pet_name= 'kitty', pet_type= 'cat')
# pet_available(pet_name="Kitty")

def pet_available(pet_type, pet_name= 'dog'):
    print(f"I have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")

# def get_formatted_name(first_name, middle_name,  last_name):
#     fullname = f"{first_name} {middle_name} {last_name} "
#     return fullname.title()
# name = get_formatted_name('prabal', 'pratap', 'singh')
# print(name)


# ||||||Creating fuction for formatting name|||||||

def formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

name = formatted_name("prabal", "pratap", "singh")
print(name)
# |||||||||||||||Fuction 1||||||||||||||||
def build_person(first_name, last_name, age=None):
 """Return a dictionary of information about a person."""
 person = {'first': first_name, 'last': last_name}
 if age:
    person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age = 12 )
print(musician)
# -----------------------------

def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {last_name}"
 return full_name.title()
# This is an infinite loop!
while True:
 print("\nPlease tell me your name:")
 f_name = input("First name: ")
 l_name = input("Last name: ")
 
 formatted_name = get_formatted_name(f_name, l_name)
 print(f"\nHello, {formatted_name}!")


