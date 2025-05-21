# Haiku Journal 
# haikujo.py 

# import libraries
from datetime import datetime

# diplay options to user

# create list to store haiku
haiku_list = []

# function to ask for user input
def get_haiku_line(num):
    return input(f'Enter haiku line {num}:\n')

# user input - 3 lines for haiku
# loop to ask for 3 lines of haiku
for num in range(1, 4):
    haiku_list.append(get_haiku_line(num))

# write stored input into file; CSV? HTML?
# create timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# create file
# TO-DO: need to add logic in case file already exists
'''
with open('./haikujournal/haiku.txt', 'w') as haiku_file:
    haiku_file.write('')
'''


# update file with haiku text from user
with open('./haikujournal/haiku.txt', 'a') as haiku_file:
    haiku_file.write(timestamp + '\n')
    haiku_file.write(haiku[0] + '\n')
    haiku_file.write(haiku[1] + '\n')
    haiku_file.write(haiku[2] + '\n')
print('Haiku saved to file.')

# display haiku to user
print(haiku)

# re-display options to user
