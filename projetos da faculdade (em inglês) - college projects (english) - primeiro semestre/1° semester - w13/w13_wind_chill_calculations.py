import math

wind_speed = 0
count_wind_speed = 5
convertion_to_fahrenheit = 0

def wind_calculations(temperature, wind_speed):
    return 35.74 + (0.6215 * temperature ) - ( 35.75 * ( wind_speed ** 0.16 )) + ( 0.4275 * ( temperature * ( wind_speed ** 0.16 )))

temperature = float (input(f"What is the temperature? "))
temperature_measured = input(f'Fahrenheit or Celsius (F/C)? ')

while wind_speed < 60:                              # the loop will run until wind speed is 60 mph
    wind_speed += count_wind_speed                  #Will increment 5 any time the while loop start again

    if temperature_measured.upper() == 'F':
        calculation = wind_calculations(temperature , wind_speed)           #calling the wind_calculations function 

        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed:.0f} mph, the windchill is: {calculation:.2f}F")

    elif temperature_measured.upper() == 'C':
        convertion_to_fahrenheit = ((9 * temperature) / 5) + 32                     #converting celsius to Fahrenheit

        calculation = wind_calculations(convertion_to_fahrenheit , wind_speed)       #changing the parameter to calculate the temperature in Fahrenheit instead of celsius

        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed:.0f} mph, the windchill is: {calculation:.2f}F")