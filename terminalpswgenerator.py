# Terminal Password Generator (v 1.0)
#
# terminalpswgenerator.py
#
# MIT License
#
# Copyright (c) 2022 Emiliano Gabriele
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import string
import random
from tkinter import Tk

print("Terminal Password Generator (v 1.0)")

char = list(string.ascii_letters + string.digits + "?=|!@#$%^&*()+-")

# clipboard copy
def clipboard(str):

	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(str)
	r.update() 
	r.destroy()

# password generator
def generate_password():

	random.shuffle(char)
	
	password = []
	for i in range(length):
		password.append(random.choice(char))

	random.shuffle(password)

	clipboard("".join(password))

	print('Password created, paste it where you want.')
	print(f"For more info visit: https://github.com/ylian89 \n")

# Select the lenght of psw
length = int(input("Enter password length (min 8): "))

# Check the lenght (min 8 characters)
if length < 8:
	print('Password is too short')
	print(f"For more info visit: https://github.com/ylian89 \n")
	input('Press ENTER to exit') # Is only for not close di terminal
else:
	generate_password()
	


