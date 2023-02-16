
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

