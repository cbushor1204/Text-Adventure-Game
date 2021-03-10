import sys
import time
import random


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


class enemyStats():
  def __init__(self, health, power, agility, protection, magic):
    self.health = health
    self.power = power
    self.agility = agility
    self.protection = protection
    self.magic = magic


class playerInventory():
  def __init__(self, item, health, power, agility, protection, magic):
    self.item = item
    self.health = health
    self.power = power
    self.agility = agility
    self.protection = protection
    self.magic = magic


class playerItem():
  def __init__(self, name, health, power, agility, protection, magic, healing, lifesteal):
    self.name = name
    self.health = health
    self.power = power
    self.agility = agility
    self.protection = protection
    self.magic = magic
    self.healing = healing
    self.lifesteal


p1 = playerAttributes("undefined", 0, 'undefined', 0, 'undefined', 'undefined', 'undefined', 'undefined')
p2 = playerStats(0, 0, 0, 0, 0)


##Random Enemy Generator!!!


def printout(str):
  for char in str:
    time.sleep(0.029)
    sys.stdout.write(char)
    sys.stdout.flush()


def storyChapterOne():
	Progress = 1
  e1 = enemyStats(30, 5, 0, 0, 0)
	printout(f'')


def storyProlouge():
	Progress = 0
  print('')
  printout(f'The kingdom of Araluen was once a peacful and prosperous land. King Alexander & Queen Charlotte had been in power for 20 strong years, having 3 children; Prince {p1.name}, Prince Henry, & Princess Meredith. However, the Baron of a newly gained teritory to the north began fighting the royal families rule. Baron Seth of Mount Obsideon mounted a full fleged attack against Castle Whitefire. The siege lasting 120 days untill the attackers broke through, slaughtering the inhabitants. Fortunatly, a knight managed to assist the royal family in an escape attempt; failing the royal family was slaughtered except Prince {p1.name} managing to escape to the southern wastelands...')
  storyChapterOne()


def storyChapterOne():
  print('In Developement')



def menuSettings():
  print('In Developement')


def menuCredits():
  print('Lead Developer: Caden Bushor')
  print('Beta Tester: N/A')


def menuHelp():
  print('In Developement')


def gameLoad():
  print('In Developement')


def gameNew():
  print('WARNING: We suggest reading the Help Menu before creating a character as it provides critical information about the selections you are choosing for your character, please keep in mind that your character has the option to be edidted only ONCE outside of the character creation menu.')
  print('ATTENTION: In the case of a numbered list, to choose an option use the NUMBER associated with desiered selection(s).')
  print('')
  p1.name = input('Character Name: ')
  p1.age = input('Character Age: ')
  p1.favortite = input('Charcter Favortie Thing: ')
  p1.eyeColor = input('Character Eye Color: ')
  p1.hairColor = input('Character Hair Color: ')
  p1.skinColor = input('Character Skin Color: ')
  p1.height = input('Character Height (Inches): ')

  print('1. Fire')
  print('2. Water')
  print('3. Air')
  print('4. Earth')
  print('5. Light')
  print('6. Weather')
  p1.specialty = input('Character Element Class: ')

  if p1.specialty == "1":
    p1.specialty = "Fire"
  if p1.specialty == "2":
    p1.specialty = "Water"
  if p1.specialty == "3":
    p1.specialty = "Air"
  if p1.specialty == "4":
    p1.specialty = "Earth"
  if p1.specialty == "5":
    p1.specialty = "Light"
  if p1.specialty == "6":
    p1.specialty = "Weather"

	storyProlouge()



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