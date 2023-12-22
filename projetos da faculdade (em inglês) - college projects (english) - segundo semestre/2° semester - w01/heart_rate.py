#Finding the heart range

age = int(input(f'How old are you? '))
maximum_heart_rate = 220 - age      # The heart doesn't beat more than this

# to strengthen your heart, you should keep your heart rate between 65% and 85% of your heart’s maximum rate.

print(f'Your heart range is {maximum_heart_rate:.2f} per minute.')

minimum_heart_rate_permited = (maximum_heart_rate * 65) / 100
maximum_heart_rate_permited = (maximum_heart_rate * 85) / 100

print(f'When you exercise to strengthen your heart, you should keep your heart rate between {minimum_heart_rate_permited} and {maximum_heart_rate_permited} beats per minute.')

