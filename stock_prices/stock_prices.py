#!/usr/bin/python

import argparse

def find_max_profit(prices):
  lowest = prices[0]
  highest = prices[0]
  highest_index = 0
  for i in range(0, len(prices)-1):
    if prices[i] >  highest:
      highest = prices[i]
      highest_index = i
  for j in range(0, highest_index):
    if prices[j] < lowest:
      lowest = prices[j]
  return highest - lowest


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))