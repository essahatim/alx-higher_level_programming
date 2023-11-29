#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = number % 10 if number > 10 else number % -10
msg = "Last digit of %d is %d and is" % (number, last_dig)
if last_dig == 0:
    print(msg, '0')
elif last_dig > 5:
    print(msg, 'greater than 5')
else:
    print(msg, 'less than 6 and not 0')
