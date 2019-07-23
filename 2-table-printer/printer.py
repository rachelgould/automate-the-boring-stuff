#! python3
# printer.py - takes a list of strings and displays them in a well-organized table

def get_header_row():
  valid_inputs = ['yes', 'no']
  while True:
    header_row = input()
    if header_row.lower() in valid_inputs:
      break
    else:
      print('Please give a yes/no answer.')
  if header_row == 'yes':
    return True
  else:
    return False

def get_number():
  while True:
    num = input()
    if isinstance(num, int) and num != 0:
      break
    else:
      print('Please provide a whole number greater than 0.')
  return num


print('Welcome to this simple table printer!\nLet\'s get started! First of all, do you want a header row? (yes/no): ')

header = get_header_row()

print('How many columns would you like to make?')

columns = get_number()

print('How many rows would you like to make?')

rows = get_number()



