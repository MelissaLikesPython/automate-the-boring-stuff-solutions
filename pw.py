#! /usr/bin/env python3

# pw.py - An insecure password locker program to learn how these things work.

PASSWORDS = {'email': 'badEmailPassword',
             'blog': 'anotherCrappyPasswordForBlog',
             'luggage': '12345'}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')

account = sys.argv[1]    # first command line arg is the account name    

import pyperclip

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
