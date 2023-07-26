# importing the regular expression module
import re

# regex pattern
pattern = re.compile(r'^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$')

# for loop to get input from user 
for _ in range(int(input().strip())):
    
    #using pattern to search if the number is valid
    print('Valid' if pattern.search(input().strip()) else 'Invalid')
