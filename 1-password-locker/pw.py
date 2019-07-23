#! python3
# pw.py - An insecure passwork locker program.

PASSWORDS = { 'email': 'KhE!tC9hEd\sx:Q', 
              'blog': 'wcRwq4PhRGy6KNfd',
              'luggage': '2840' }

import sys, pyperclip

if len(sys.argv) < 2:
  print('Usage: python pw.py [account] - copies your password for [account] to the clipboard.')
  sys.exit()

account = sys.argv[1] # the first command line argument is the name of the account to look up

if account in PASSWORDS:
  pyperclip.copy(PASSWORDS[account])
  print('Password for #{account} copied to clipboard.')
else:
  print('There is no account stored that\'s named #{account}.')