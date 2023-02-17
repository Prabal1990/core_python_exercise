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

def pet_available(pet_type, pet_name):
    print(f"I have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")

pet_available("dog", "tipu")