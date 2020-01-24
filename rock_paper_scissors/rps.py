#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rock = 'rock'
  paper = 'paper'
  scissors = 'scissors'
  arr_inner = [[rock],[paper],[scissors]]
  if n == 0:
    return [[]]
  elif n == 1:
    return arr_inner
  else:
    arr = []
    for i in range(0, 3**n // 3):
      arr.append([rock])
      # arr.append(arr[i].)
      print(arr[i][0].split().append(scissors))
    for i in range(0, 3**n // 3):
      arr.append([scissors])
    for i in range(0, 3**n // 3):
      arr.append([paper])
    print(arr) 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')