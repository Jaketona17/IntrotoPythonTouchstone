

question1 = ('Hello! Would you like to go to Walt Disney World?: ')

question2 = ('Do you have a valid ticket for admission \
into Walt Disney World?: ')

question3 = ('Great! Let\'s go to the Magic Kingdom. \
What ride do you want to go on first?: ')

question4 = ('How tall are you? Please measure in inches: ')


options2 = ('1. Single-Day Park Hopper',
'2. Annual Pass', '3. None')


# 1 ask the user if they want to go to wdw
answer1 = print(question1)

if answer1 == 'Yes':
    answer2 = int(input(question2))
    print(options2)
elif answer1 == 'No':
    print('Alright, maybe some other time then. Goodbye!')
    exit(0)
else: print('Please answer in \"Yes\" or \"No\"')


# 2 ask user if they have a ticket for wdw
if answer2 == 1 or answer2 == 2:
    answer3 = input(question3)
elif answer2 == 3:
    print('You must first purchase a ticket if you wish to go.')
    exit(0)
else: print('Please type 1, 2, or 3')

# 3 ask what ride to go on (just SM for now)
answer3 = ride_list = ('Space Mountain')

if answer3 == 'Space Mountain':
    answer4 = input(question4)
else: print('Please type the full name of the attraction you would\
like to go on first. (Space Mountain)')

# 4 ask height
height = 44

if height >= 44:
    print('Have fun!')
    end(0)

elif height < 44:
    print('Sorry, you are not tall enough to ride this ride.')

