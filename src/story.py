import sys
import time
import text


currentChapter = {}
currentFight = {}


def printout(str):
  for char in str:
    time.sleep(0.029)
    sys.stdout.write(char)
    sys.stdout.flush()


def chapterOne():
  printout(text.chapterOne)