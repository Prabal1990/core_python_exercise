# Dictionary allow indexing through key only
alien_0 = {'color': 'green'}
print(alien_0['color'])

Alien_0 = {'color': 'green', 'points': 5}
# OUTPUT:     You just earned 5 points|
print(f"You just earned {Alien_0['points']} points.")

# ||||||||||Adding Input|||||||||||
Alien_0['x_axis'] = 2
Alien_0['y axis'] = 3
print(Alien_0)

alien_0['color'] = 'green'
# output : The alien is green.
print(f"The alient is {alien_0['color']}")
alien_0['color'] = 'red'
print(f"The alien is now {alien_0['color']}")
# The alien is now yellow.

# ||||||||||Alien game exercise|||||||
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Exercise:
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")






# if alien_0['speed'] == 'slow':
#  x_increment = 1
# elif alien_0['speed'] == 'medium':
#  x_increment = 2
# else:
#  # This must be a fast alien.
#  x_increment = 3
# # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")
# alien_0['speed'] = 'fast'