import copy
from math import exp
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    self.copy = []
    for color, count in kwargs.items():
      while count > 0:
        self.contents.append(color)
        self.copy.append(color)
        count = count - 1

  def draw(self, numOfDraws):
    self.contents = self.copy
    ballsDraw = []
    contentsCopy = copy.copy(self.contents)

    if numOfDraws > len(contentsCopy):
      ballsDraw = copy.copy(contentsCopy)
      contentsCopy = []
    else: 
      while numOfDraws > 0:
        ball = random.choice(contentsCopy)
        ballsDraw.append(ball)
        contentsCopy.remove(ball)
        numOfDraws = numOfDraws - 1

    self.copy = self.contents
    self.contents = contentsCopy

    return ballsDraw



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  isMatch = True
  matchCount = 0
  experimentCount = num_experiments

  ballsExpected = []
  for color, count in expected_balls.items():
    while count > 0:
      ballsExpected.append(color)
      count = count - 1

  contents = copy.copy(hat.copy)

  while num_experiments > 0:
    ballsDraw = hat.draw(num_balls_drawn)
    hat.contents = contents

    for ball in ballsExpected:
      if ball in ballsDraw:
        ballsDraw.remove(ball)
      else:
        isMatch = False

    if isMatch:
      matchCount = matchCount + 1
    

    isMatch = True
    num_experiments = num_experiments - 1

  return matchCount / experimentCount
  


