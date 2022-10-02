number = [1, 2, 3]
new_list = []
for n in number:
    num_1 = n + 1
    new_list.append(num_1)
############################################## Or ###########
### new_list = [new_item for item in list] ######### this is example of how it should be arrange###
number = [1, 2, 3]
new_list = [n + 1 for n in number]

################################## console code###############
number = [1, 2, 3]
new_number = [w + 1 for w in number]
name = "Abdulroqeeb"
new_list = [letter for letter in name]
range_list = [num * 2 for num in range(1, 5)]
names = ["Abdul", "malik", "Aish", "will", "Dave", "Beth"]
new_name = [name for name in name if len(name) < 5]
print(new_name)

################################################################################################################
names = ["Abdulroqeeb", "malikiberry", "Aish", "willims", "Dave", "Beth"]
long_name = [name.upper() for name in names if len(name) > 5]
names = ["Abdulroqeeb", "malikiberry", "Aish", "will", "olamide", "Beth"]

for when in names:
    if when > 5:
        print(names)
##################################################################################################################

names = ["Abdulroqeeb", "malikiberry", "Aish", "willims", "Dave", "Beth"]
list_name = [name for name in names if len(name) > 5]
names = ["Abdulroqeeb", "malikiberry", "Aish", "willims", "Dave", "Beth"]
list_name = [name for name in names if len(name) > 5]
names = ["Abdulroqeeb", "malikiberry", "Aish", "willims", "Dave", "Beth"]
name_list = []
for name in names:
    if len(name) > 5:
        name.upper()
name_list.append(name)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_number = [number for number in numbers]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)
################################################################################

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [new % 2 for new in numbers]
print(result)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [new  for new in numbers if new % 2 == 0]
print(result)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
for num in numbers:
    if num % 2 == 0:
        print(num)
