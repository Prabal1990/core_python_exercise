message = "hello python world!"
print(message.title())

#it will caps the 1st letter of every word
#apply the title method on name variable
#title doesn't need any other info thats why  parentheses are empty
name = "ada lovelace"
print(name.title())
# to using every thing in upper/lower letter
print(name.upper())
# output - ADA LOVELACE
print(name.lower())
# output - ada lovelace
# The lower() method is particularly useful for storing data

# ||||||String CONCATINATION - f-strings|||||||||||||||
# { = curly braces, format-strings
# format the string by replacing the  variable  with its values 
first_name = "ada"
last_name = "lovelace"
fullname = f"{first_name} {last_name}"
print(fullname)
# output -ada lovelace
fullname = f"{first_name}{last_name}"
print(fullname)
# output -adalovelace

#try to print below- 
# Hello, Ada Lovelace!
print("Hello", fullname.title(),"!")
print('Hello,', f"{fullname.title()}!")
print(f"Hello, {fullname.title()}!")


# Adding Whitespace to Strings with Tabs "\t" or Newline "\n"
print("Python")
print("\tPrabal \n\t\tsingh")
# To add a newline in a string
print("Languages:\nPython\nC\nJavaScript") 

# for removing extra space
# we use Stripping Whitespace .rstrip()
favorite_language = 'python  '
favorite_language.rstrip()
