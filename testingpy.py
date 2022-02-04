import random

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print("x is:" + str(x))

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print("Today is:" + day)

if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')