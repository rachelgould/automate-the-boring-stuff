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
      print(f'Error: Expected the number of columnns to be {columns}, but instead got {input_columns}. Please try again!')
  return header_contents

def get_row_contents():
  contents_raw = input()
  contents = contents_raw.split(',')
  return contents

def calc_widest_value(header=False, header_contents=[], body_contents=[]):
  all_contents = header_contents + body_contents
  return len(max(all_contents, key=len))

def get_number():
  while True:
    num = input()
    if num.isdigit() and num != '0':
      break
    else:
      print('Please provide a whole number greater than 0.')
  return int(num)

header_contents=[]

print('Welcome to this simple table printer!\nLet\'s get started! First of all, do you want a header row? (yes/no): ')

header = get_header_row()

print('How many columns would you like to make?')

columns = get_number()

print('How many rows would you like to make?')

rows = get_number()

if header:
  print('Please paste in the header row, with each value separated by a comma')
  header_contents = get_header_row_contents()

print('Please paste in the table contents, with each value separated by a comma')
body_contents = get_row_contents()

widest_value = calc_widest_value(header, header_contents, body_contents)

print('Thanks! Here\'s your table:')

top_row = '|'
if header:
  print('=' * columns * (widest_value + 1))
  for value in header_contents:
    cell = value.center(widest_value)
    top_row = top_row + cell + '|'
  print(top_row) 
  print('=' * columns * (widest_value + 1))

concatenated_body_contents = '|'
for index, value in enumerate(body_contents):
  cell = value.center(widest_value)
  concatenated_body_contents = concatenated_body_contents + cell + '|'
  if (index + 1) % columns == 0 and index != len(body_contents) - 1:
    concatenated_body_contents = concatenated_body_contents + '\n' + ('-' * columns * (widest_value + 1)) + '\n' + '|'
print(concatenated_body_contents)
