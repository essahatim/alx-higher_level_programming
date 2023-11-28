#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = number % 10 if number > 10 else number % -10
msg = "Last digit of %d is %d " % (number, last_dig)
if last_dig > 5:
    print(msg, 'and is greater than 5')
elif last_dig == 0:
    print(msg, 'and is 0')
else:
    print(msg, 'and is less than 6 and not 0')
