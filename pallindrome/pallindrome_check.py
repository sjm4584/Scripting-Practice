#!/usr/bin/env python

#takes number of lines, then input, checks if it's a pallindrome
#example input:
'''
3
Was it a car
or a cat
I saw
'''

input = ""
num_lines = raw_input('Enter number of lines >>> ')

for i in range(int(num_lines)):
    input += raw_input('>>> ')

if input[::-1].replace(' ', '') == input.replace(' ', ''):
    print "Pallindrome!"
else:
    print "Not a pallindrome"
