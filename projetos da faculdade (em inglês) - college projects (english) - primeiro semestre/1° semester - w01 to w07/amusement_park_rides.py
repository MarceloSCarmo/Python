

can_ride = False


rider1_height = int(input(f'Tell your hieght in inches? '))
rider1_age = int(input(f'How old are you? '))


is_rider_2 = input(f'Is there any other rider?\nPS: Answer "YES" or "NOT". Anything different will not be avialable"\n')


if is_rider_2.lower() == 'yes':
    rider2_height = int(input(f'Tell his hieght in inches? '))
    rider2_age = int(input(f'How old is He? '))
    
    if rider1_height < 36 or rider2_height < 36:
        can_ride = False
    else:
        if rider1_age >= 18 or rider2_age >= 18:
            can_ride = True
        else:
            can_ride = False
else:
    if rider1_age >= 18 and rider1_height >= 62:
        can_ride = True
    else:
        can_ride = False


if can_ride:
    print('You can ride.')
else:
    print('So sorry, you may not ride.')



