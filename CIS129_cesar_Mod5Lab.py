# Module 5 Lab 5
# author - cesar
# date - 2025-03-02
"""
Calculates a running total of bottles turned in throughout the week
Then processes the bottle and payout info
Finally, displays the total amount of bottles and the payout to be given
"""

# initialize loop control variables
keepGoing = 'y'

# loop to repeat for each week
while (keepGoing == 'y'):
    NBR_OF_DAYS = 7
    # initialize/reset variable values
    totalBottles = 0
    todayBottles = 0
    totalPayout = 0
    counter = 1
    # loop to repeat for each day of the week
    while (counter <= NBR_OF_DAYS): 
        # code to receive user inputs
        todayBottles = int(input(f'Enter # of bottles for day {counter}: '))
        totalBottles += todayBottles
        counter += 1

    totalPayout = (totalBottles * 0.10)

    # code to display totals
    print()
    print(f'Total bottles collected is {totalBottles}')
    print(f'Total to be paid out is ${totalPayout:.2f}')
    print()

    # code to end looping
    keepGoing = input('Would you like to enter another week of data?\n(Enter y or n): ')
