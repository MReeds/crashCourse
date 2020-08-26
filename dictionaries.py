# Practice with dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New position: {alien_0['x_position']}")

del alien_0['points']
print(alien_0)
