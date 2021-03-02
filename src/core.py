import sys
import story


class playerStats():
  def __init__(self, level, health, power, agility, protection, magic):
      self.level = level
      self.health = health
      self.power = power
      self.agility = agility
      self.protection = protection
      self.magic = magic


class playerAttributes():
  def __init__(self, name, age, specialty, height, eyeColor, hairColor, skinColor, favorite):
    self.name = name
    self.age = age
    self.specialty = specialty
    self.height = height
    self.eyeColor = eyeColor
    self.hairColor = hairColor
    self.skinColor = skinColor
    self.favorite = favorite


p1 = playerAttributes("undefined", 0, 'undefined', 0, 'undefined', 'undefined', 'undefined', 'undefined')
p2 = playerStats(0, 0, 0, 0, 0, 0)


def menuSettings():
    print('In Developement')


def menuCredits():
  print('In Developement')


def menuHelp():
  print('In Developement')


def gameLoad():
  print('In Developement')


def gameNew():
  print('WARNING: We suggest reading the Help Menu before creating a character as it provides critical information about the selections you are choosing for your character, please keep in mind that your character has the option to be edidted only ONCE outside of the character creation menu.')
  print('')
  p1.name = input('Character Name: ')
  p1.age = input('Character Age: ')
  p1.favortite = input('Charcter Favortie Thing: ')
  p1.eyeColor = input('Character Eye Color: ')
  p1.hairColor = input('Character Hair Color: ')
  p1.skinColor = input('Character Skin Color: ')
  p1.height = input('Character Height (Inches): ')

  print('1. Warrior - Standard Character')
  print('2. Assassing - High Damage, Low HP, Physical')
  print('3. Mage - Normal Damage, Normal HP, Magical')
  print('4. Guardian - Low Damage, High Health, Physical')
  print('5. Hunter - Normal Damage, Low HP, Physical')
  p1.specialty = input('Character Class: ')

  story.chapterOne()

def menuMain():
  print('Text Adventure Game')
  print('1. New Game')
  print('2. Load Game')
  print('3. Help Page')
  print('4. Credits Page')
  print('5. Settings Page')
  print('')
  menuMainInput = input('Select a option from above: ')

  if menuMainInput == '1':
    print('')
    gameNew()
  if menuMainInput == '2':
    print('')
    gameLoad()
  if menuMainInput == '3':
    print('')
    menuHelp()
  if menuMainInput == '4':
    print('')
    menuCredits()
  if menuMainInput == '5':
    print('')
    menuSettings()
  else:
    print('')
    menuMain()



menuMain()