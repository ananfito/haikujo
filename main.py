# Haiku Journal 
# main.py 

# import libraries

# diplay options to user

# user input - 3 lines for haiku
haiku = []
line1 = input('Enter haiku line 1:\n')
line2 = input('Enter haiku line 2:\n')
line3 = input('Enter haiku line 3:\n')

# store input into dict? list? 
haiku.append(line1)
haiku.append(line2)
haiku.append(line3)

# write stored input into file; CSV? HTML?
# create file
with open('./haikujournal/haiku.txt', 'w') as haiku_file:
    haiku_file.write('')

# update file with haiku text from user
with open('./haikujournal/haiku.txt', 'a') as haiku_file:
    haiku_file.write(haiku[0] + '\n')
    haiku_file.write(haiku[1] + '\n')
    haiku_file.write(haiku[2] + '\n')
print('Haiku saved to file.')

# display haiku to user
print(haiku)

# re-display options to user
