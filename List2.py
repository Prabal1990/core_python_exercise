
# |||||||||||Passing a list to a Function|||||||||||

def greet_users(names):
 """Print a simple greeting to each user in the list."""
 for name in names:
    msg = f"Hello, {name.title()}!"
    print(msg)

    
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
print("\n")
# ---------------------------------------

# |||||||||||Modifying a List in a Function|||||||||||
# Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# # while unprinted_designs:
# #  current_design = unprinted_designs.pop()
# #  print(f"Printing model: {current_design}")
# #  completed_models.append(current_design)
# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#  print(completed_model)


def print_models(unprinted_designs, completed_models):
#  Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
 
 while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
 
def show_completed_models(completed_models):
 "Show all the models that were printed."
 print("\nThe following models have been printed:")
 for completed_model in completed_models:
    print(completed_model)
 
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


def make_pizza(*toppings):
 print("\nMaking the pizza with below toppings:")
 for topping in toppings:
    
    print(topping)


list1 = make_pizza('sugar')
list2 = make_pizza('salt', 'pepper', 'cabage')

# |||||||||||||||||||||||||||||||||||

def person(ist_name, last_name, **info):
  info["name 1st"] = ist_name
  info["name 2st"] = last_name
  print(info)

person('Naveen', 'Singh', Company = 'TCS', Hometown = 'Bangalore')

def person( names, classs, *info):
#   info["name 1st"] = ist_name
#   info["name 2st"] = last_name
    names

# print(info)

person('Naveen', 'Singh', 'TCS', 'Bangalore')