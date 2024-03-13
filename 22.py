# Project Euler problem 22: sort the list of names in 22.txt in alphabetical order,
# then find the total of all the name scores in the file, where a name score is given
# by the name's order in the sorted list times its value (sum of the letters in the name,
# where A = 1, B= 2, etc.)

namesFile = open('./22.txt')
names = namesFile.read()
names = names.split(',')
names = [name.strip('"') for name in names]
names.sort()

alphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
for name in names:
    nameValue = 0
    for letter in name:
        nameValue += alphabetString.index(letter) + 1
    total += (names.index(name) + 1) * nameValue

print(total)







namesFile.close()