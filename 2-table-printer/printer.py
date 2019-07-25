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

def get_header_row_contents():
  while True: 
    header_contents_raw = input()
    header_contents = header_contents_raw.split(',')
    input_columns = len(header_contents)
    if input_columns == columns:
      break
    else:
      print('Error: Expected the number of columnns to be #{columns}, but instead got #{input_columns}. Please try again!')
  return header_contents

def get_number():
  while True:
    num = input()
    # ERROR here if the user puts in something like a string
    num = int(num)
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

if header:
  print('Please paste in the header row, with each column separated by a comma')
  header_contents = get_header_row_contents()
  print('These are the header contents: ', header_contents)



