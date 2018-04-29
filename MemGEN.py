import random

class MemGEN:
  inputData=None
  def __init__(self):
  	self.inputData = []

  def learn(self, data):
    self.inputData = data

  def generate(self):
    return random.choice(self.inputData)