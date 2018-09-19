# test1

# test2 12

# https://github.com/chernand1/miniScoreDisplay.git

from fetchScores import football
#from miniDisplayScore import keyboard_input

import time

matchToWatch = football(league='nfl')

print(matchToWatch.league)
matchToWatch.readHtmlFile()

print(matchToWatch.printUrl())
matchToWatch.printAllMatches()
matchToWatch.listTeams()
#my_keyboard_reader = keyboard_input()

while(1):
    print(matchToWatch.getMatchNumber("NY Giants"))
    print(matchToWatch.getMatchDetail(matchToWatch.getMatchNumber("NY Giants")))
    matchToWatch.readHtmlFile()
    #print("Is key pressed = " + str(my_keyboard_reader.key_pressed))
    time.sleep(5)
