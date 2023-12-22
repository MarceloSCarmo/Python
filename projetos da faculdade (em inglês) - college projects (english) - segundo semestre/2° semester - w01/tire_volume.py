
import math
from datetime import datetime



width = float(input(f'What is the width of the tire? '))
tire_aspect_ratio = float(input(f'What is the aspect ratio? '))
wheel_diameter = float(input(f'What is the diameter of the wheel that the tire fits? '))


volume = ( math.pi * (width ** 2) * tire_aspect_ratio * ((width * tire_aspect_ratio) + (2540 * wheel_diameter)) ) / 10000000000

print(f'The volume of space inside that tire: {volume:.2f} liters') 

#       W01 Prove Assignment: Tire Volume

current_day = datetime.now()
weekday = current_day.weekday()


#       If statement to print the day of the week.
if weekday == 0:
    print(f'Monday, {current_day}')
elif weekday == 1:
    print(f'Tuesday, {current_day}')
elif weekday == 2:
    print(f'Wednesday, {current_day}')
elif weekday == 3:
    print(f'Thursday {current_day}')
elif weekday == 4:
    print(f'Friday, {current_day}')
elif weekday == 5:
    print(f'Saturday, {current_day}')
elif weekday == 6:
    print(f'Sunday, {current_day}')

    #with open("volumes.txt", "at" ) as volume_file:



with open("volumes.txt", "at" ) as volume_file:
    print(weekday, file=volume_file)
    print(f"{width}, {tire_aspect_ratio}, {wheel_diameter}, {volume}", file=volume_file)