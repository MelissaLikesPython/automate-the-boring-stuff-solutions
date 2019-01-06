#! /usr/bin/env python3

# stockPhrase.py - Adds stock phrases to clipboard to paste into student reports.

PHRASES = {'A': ' is an excellent student and a pleasure to have in the class.',
             'B': ' is a competent student who should do well with some initial support.',
             'C': ' has shown development over the course but will need support in the initial stages.'}

import sys
if len(sys.argv) < 2:
    print('Usage: python stockPhrase.py [grade] - copy stock phrase for grade')

grade = sys.argv[1]    # first command line arg is the account name    

import pyperclip

if grade in PHRASES:
    pyperclip.copy(PHRASES[grade])
    print('Stock phrase for ' + grade + ' student copied to clipboard.')
else:
    print('There is no stock phrase for grade ' + grade)
