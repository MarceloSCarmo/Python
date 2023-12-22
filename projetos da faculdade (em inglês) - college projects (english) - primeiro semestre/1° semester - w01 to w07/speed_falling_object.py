
# Assignment

print('Please enter the following information:\n')

mass = float(input(f'Mass (in kg): '))  #m
gravity = float(input(f'Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))  #g 
time = float(input(f'Mass (in seconds): '))  #t 
density = float(input(f'Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))  #p 
area = float(input(f'Cross sectional area (in m^2): '))  #A 
constant = float(input(f'Drag constant (0.5 for sphere, 1.1 for cylinder): '))  #C 
radius_bowling_ball = float(input(f'The radius of the bowlling ball (in m^2): ')) 



# exp = the number e(2.71828) in math library is function math.exp(value)
# sqrt = the square root of the givien expression. In math library function math.sqrt(value)

import math # import the math library

c = ( 1 / 2 ) * (density * area * constant)

velocity = math.sqrt(( mass * gravity) / c ) * (1 - math.exp(( - math.sqrt( mass * gravity * c ) / mass ) * time )) # the formula that calculates the velocity of
# a falling object.

print('\n') # Skip one line

print(f"The inner value of c is: {c:.3f}")
print(f"The velocity is {velocity:.3f} m/s^2\n")

# STRETCH CHALLENGE

area_bowlling_ball = math.pi * ( radius_bowling_ball ** 2 ) # calculating the bowlling ball area

B = ( 1 / 2 ) * (density * area_bowlling_ball * constant)  # for this calculation I'll use B instead of c, and instead of the area I'll use the area_bowlling_ball to calculate the area

velocity_bowlling_ball = math.sqrt(( mass * gravity) / c ) * (1 - math.exp(( - math.sqrt( mass * gravity * B ) / mass ) * time )) # the formula that calculates the velocity of
# a falling object.

print(f"The velocity of the bowlling ball is {velocity_bowlling_ball:.3f} m/s^2\n")