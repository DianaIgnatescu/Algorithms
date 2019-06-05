#!/usr/bin/python

import argparse


def find_max_profit(prices):

    # 1. Keep track of lowest price in the list
    lowest = prices[0]

    # The max profit must be computed by subtracting some price by another price that comes before it
    max_profit = prices[1] - lowest

    # 2. Keep track of current min price so far and max profit so far

    for current_price in prices[1:]:
        # Find the highest profit in the list
        max_profit = max(current_price - lowest, max_profit)

        # Find the smallest price in the list
        lowest = min(current_price, lowest)

    return max_profit


print(find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))