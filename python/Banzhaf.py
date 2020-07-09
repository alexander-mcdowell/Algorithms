import numpy as np
import math
import itertools
from prettytable import PrettyTable
import operator

# Banzhaf algorithm: computes the Banzhaf Power Index of a selection of voters; shows who has the most power in an election.
# Requirements: There must be a certain threshold (quota) of votes for a particular vote to pass.
# Method:
    # 1. Using a Monte-Carlo method, generate a random coalition (subset of voters who support a particular vote) of voters excluding the voter whose index is being calculated.
    # 1 cont. For example, if the voters are [A, B, C, D] and you are testing A's power, a random coalition would be (C, D).
    # 2. A winning coalition is a coalition whose total votes exceed the threshold for a vote to pass.
    # 2 cont. If A has 4 votes, B has 3 votes, C has 2 votes, and D has 1 vote and the threshold is 6, then (A, B), (A, C), (A, B, D) are winning coalitions
    # 3. If the random coalition does not pass the threshold, but passes if the voter being tested joins the coalition, increment a "winning counter".
    # 3 cont. For example, coalition (B, C) does not pass the threshold, but (A, B, C) does. Thus, increment A's winning counter.
    # 4. The Banzhaf index of the winner is thus the winning counter divided by the coalitions tested.

def randomSubset(set):
    subsets = []
    for m in set:
        u = math.floor(np.random.rand() * 2)
        if u == 0:
            subsets.append(m)
    return subsets

def BanzhafMeasure(voter, voters, weights, quota, tries):
    k = 0
    n = 0
    while k < tries:
        coalition = randomSubset(voters)
        votes = 0
        for m in coalition:
            votes += weights[voters.index(m)]
        if (votes < quota) and (votes + weights[voters.index(voter)]) >= quota:
            n += 1
        k += 1
    return n / k

if __name__ == '__main__':
    state_votes = {'Alabama': 9, 'Alaska': 3, 'Arizona': 10, 'Arkansas': 6, 'California': 55,
                   'Colorado': 9, 'Connecticut': 7, 'D.C': 3, 'Delaware': 3, 'Florida': 27,
                   'Georgia': 15, 'Hawaii': 4, 'Idaho': 4, 'Illinois': 21, 'Indiana': 11, 'Iowa': 7,
                   'Kansas': 6, 'Kentucky': 8, 'Louisiana': 9, 'Maine': 4, 'Maryland': 10, 'Massachusetts': 12,
                   'Michigan': 17, 'Minnesota': 10, 'Mississippi': 6, 'Missouri': 11, 'Montana': 3, 'Nebraska': 5,
                   'Nevada': 5, 'New Hampshire': 4, 'New Jersey': 15, 'New Mexico': 5, 'New York': 31, 'North Carolina': 15,
                   'North Dakota': 3, 'Ohio': 20, 'Oklahoma': 7, 'Oregon': 7, 'Pennsylvania': 21, 'Rhode Island': 4,
                   'South Carolina': 8, 'South Dakota': 3, 'Tennessee': 11, 'Texas': 34, 'Utah': 5, 'Vermont': 3, 'Virginia': 13,
                   'Washington': 11, 'West Virginia': 5, 'Wisconsin': 10, 'Wyoming': 3}
    voters = list(state_votes.keys())
    weights = list(state_votes.values())
    quota = 270
    accuracy = 0.95
    eta = 0.001
    iterations = math.ceil(math.log(2 / (1 - accuracy)) / (2 * eta * eta))

    table = PrettyTable()
    table.field_names = ["State Name", "Electoral Votes", "Banzhaf Measure (Voting Power)"]
    for state in state_votes:
        power = BanzhafMeasure(state, voters, weights, quota, iterations)
        table.add_row([state, state_votes[state], power])
    print(table.get_string(sortby = "Banzhaf Measure (Voting Power)", reversesort = True))
