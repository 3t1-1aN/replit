import random, os, time
def roll(sides):
  thrown_roll = random.randint(1,sides)
  return thrown_roll
#def roll2():
 # thrown_roll2 = random.randint(1,12)
 # return(thrown_roll2)
def health():
  hp = roll(6) * roll(12) / 2 + 10
  return hp
def strength():
  muscle = roll(6) * roll(8) / 2 + 12
  return muscle
  
'''//////////////////////////////////////////////////////////////////////////////////////////////////'''

while True:
################### char1 ##########################
  print('character Builder Battle')
  char1hp = health()
  char1stng = strength()
  c1name = input('Name your legend: ')
  y = ['almighty', 'glorious', 'endevored', 'magnificant', 'long awaited','powerful', '', 'fearsome', 'skillful','virtous']
  c1type = input('character type: (Human, Elf, Wizard, Orc) ')
  print('Contenstant 1:', c1name, 'the', random.choice(y), c1type)
  print('HEALTH:', char1hp)
  print('STRENGTH:', char1stng)
  
################### char2 ##########################
  
  c2name = input('who are you battling?')
  c2type = input('character type: (Human, Elf, Wizard, Orc) ')
  char2hp = health()
  char2stng = strength()
  print('Contestant 2:', c2name, 'the', random.choice(y), c2type)
  print('HEALTH:', char2hp)
  print('STRENGTH:', char2stng)
  time.sleep(5)
  os.system('clear')
  round = 1
  print('BATTLE TIME!!!')
  '''/////////////////////////////////////////////////////////////////////// BATTLE ///////////////////'''
  
  while True:
    time.sleep(3)
    c1roll = roll(6)
    c2roll = roll(6)
############### char1 giving damage ################
    if c1roll > c2roll:
      damage = abs(char1stng - char2stng)+1
      losthp1 = char2hp - damage
      print(c2name, 'has taken some serious damage and lost', damage, 'healthpoints')
      print()
      print(c1name, 'wins the round', round)
      print()
      round += 1
############### char2 giving damage ################
    elif c2roll > c1roll:
      damage = abs(char2stng - char1stng)+1
      losthp2 = char1hp - damage
      print(c1name, 'has taken some serious damage and lost', damage, 'healthpoints')
      print()
      print(c2name, 'wins round', round)
      print()
      print(c1name, 'HEALTH: ', losthp2)
      round += 1
####################### draw #######################
    else:
      print('It is a draw')
      print()
    '''/////////////////// DIED /////////////////'''
    if losthp1 <= 0:
      print(c1name, 'has died; defeated in', round, 'rounds')
      print(c2name, 'is the new legend!')
      break
      
    elif losthp2 <= 0:
      print(c2name, 'has died; defeated in', round, 'rounds')
      print(c1name, 'remains the legend!')
      break
    
    
    
