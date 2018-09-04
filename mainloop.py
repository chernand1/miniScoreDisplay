# test1

# test2

# https://github.com/chernand1/miniScoreDisplay.git

from fetchScores import football

import time

# matchToWatch = football('football', 'cfl')
matchToWatch = football(league='nfl')
#print(matchToWatch.league())
#matchToWatch.league = 'cfl'

print(matchToWatch.league)
matchToWatch.readHtmlFile()

print(matchToWatch.printUrl())
#matchToWatch.listMatchups()
#print(newyorkgiants.FullDescription['url'])
#newyorkgiants.readHtmlFile()
#newyorkgiants.printMatch(1)
matchToWatch.printAllMatches()
matchToWatch.listTeams()

'''canadiens = hockey()
canadiens.readHtmlFile()
canadiens.listMatchups()
canadiens.printAllMatches()
'''

while(1):
    #print("Updated value = ", matchToWatch.readHtmlFile("NY Giants"))
    #matchToWatch.getMatchDetail()
    #print(matchToWatch.getMatchDetail(13))
    print(matchToWatch.getMatchNumber("NY Giants"))
    print(matchToWatch.getMatchDetail(matchToWatch.getMatchNumber("NY Giants")))
    time.sleep(5)