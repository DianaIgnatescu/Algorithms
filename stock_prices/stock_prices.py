#!/usr/bin/python

import argparse

# A bot that buys and sells amazon stock

# function should return the max profit that can be made from a single buy and sell
# find the max difference between the smallest and largest prices in the list of prices



def find_max_profit(prices):

    # 1. Keep track of lowest price in the list
    lowest = prices[0]
    print(lowest)

    # The max profit must be computed by subtracting some price by another price that comes before it
    max_profit = prices[1] - lowest

    # 2. Keep track of current min price so far and max profit so far

    for current_price in prices[1:]:
        # find the highest profit in the list
        max_profit = max(current_price - lowest, max_profit)
        print(current_price)
        print(max_profit)
        # find the smallest price in the list
        lowest = min(current_price, lowest)
        print(lowest)

    return max_profit


print(find_max_profit([300, 1500, 280, 5120, 14]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))