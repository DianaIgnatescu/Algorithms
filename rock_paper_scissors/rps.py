#!/usr/bin/python

import sys

# generate all possible plays
# the output should be a list of lists


def rock_paper_scissors(n):
    # create a list of choices
    choices = ["rock", "paper", "scissors"]
    plays = []

    # if n == 0:
    #     return [[]]

    # define an inner recursive helper function that will perform the recursion
    def generate_plays(rounds, result=[]):
        # base case
        if rounds == 0:
            plays.append(result)

        else:
            for choice in choices:
                generate_plays(rounds - 1, list(result + [choice]))

    generate_plays(n, [])
    return plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
