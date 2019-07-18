#!/usr/bin/python

import argparse
import math


def find_max_profit(prices):
    # pass
    # keep track of our max_profit
    # prices = args.intergers
    profit = -math.inf
    # step through the list one element at a time
    for i in range(len(prices)):
        # check the profit if we sold at each point after that
        for j in range(i + 1, len(prices)):
            # compare that to the max profit we already know
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]

    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))


#   270 - 1050 = -780 //
#   1540 - 1050 = 490 //
#   3800 - 1050 = 2750 //
#   2 - 1050 = -1048

#   1540 - 270 = 1270 //
#   3800 - 270 = 3530 // MAX
#   2 - 270 = -268

#   3800 - 1540 = 2250
#   2 - 1540 = -1538

#   2 - 3800 = -3798

#   2 - 0 = 0

# max_profit = -99999999999...
# max_profit = -780
# max_profit = 490
# max_profit = 2750
# max_profit = 3530  Max


# --------- UNDERSTANDING ---------

# For this problem, we essentially want to find the maximum difference between the smallest and largest numbers in the list of numbers.
# The maximum difference is computed by subtracting the the smallest number from the largest number if the largest number is right in front of it.

# ie: prices = [1050, 270, 1540, 3800, 2]

# 1540 - 270
# 3800 - 1050
# 3800 - 270
# 3800 - 1540

# --------- PLAN ---------

# Cut the list in 2.
# Check which value is the largest in both lists.
# Store those 2 values in 2 variables
# Then compare those 2 values and return the largest of the 2.
# Then look in the original list which value matches the highest value, and look for the index of this value.
# If the index is 0 then return this value as the maximum profit.
# if the index is > 0
