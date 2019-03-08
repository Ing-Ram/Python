'''
Chad Ingram
CS 131A
Project 3

'''

class RoundRobin:
  '''
  makes a round robin schedule with the user input list
  '''
  def __init__(self, names):
    '''
    Makes a copy of the list given as one of the parameters
    '''
    self.names = names.copy()
    if (int(len(self.names)) %2 == 1):
      self.names.append('bye')

  def generate_round(self):
    '''
    makes one round of pairs as a return value from the list given as the parameters
    '''
    self.rnd = []
    for i in range(int(len(self.names)/2)):
      pairs = (self.names[i], self.names[-i-1])
      self.rnd.append(pairs)

    self.names.insert(1, self.names[-1])
    del self.names[-1]
    return self.rnd

  def __str__(self):
    return('{}'.format(self.rnd))

# my_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# schedule = RoundRobin(my_list)
# schedule.generate_round()

# print(schedule.rnd)
