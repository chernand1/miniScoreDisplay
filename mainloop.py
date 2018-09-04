# test1

# test2

# https://github.com/chernand1/miniScoreDisplay.git

from fetchScores import football

import time

matchToWatch = football(league='nfl')

print(matchToWatch.league)
matchToWatch.readHtmlFile()

print(matchToWatch.printUrl())
matchToWatch.printAllMatches()
matchToWatch.listTeams()


while(1):
    print(matchToWatch.getMatchNumber("NY Giants"))
    print(matchToWatch.getMatchDetail(matchToWatch.getMatchNumber("NY Giants")))
    time.sleep(5)