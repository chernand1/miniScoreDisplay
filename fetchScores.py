# defines a sport from which to retrieve scores
# Gets scores from bottom line web site

import urllib
import urllib.request
import re

matchup = {'team1': '', 'score1': 0, 'team2': '', 'score2': 0}

class sportsClass:

    cities = {'Atlanta': 'atl', 'Boston': 'bos', 'Montreal': 'mtl', 'NY Giants': 'nyg', 'NY Islanders': 'nyi',
              'NY Jets': 'nyj', 'NY Rangers': 'nyr', 'Toronto': 'tor', 'Vancouver': 'van', 'Winnipeg': 'wpg',
              'Ottawa': 'ott', 'Edmonton': 'edm', 'Calgary': 'cgy', 'San Jose': 'sj', 'New Jersey': 'nj',
              'Florida': 'fla', 'Philadelphia': 'phi', 'San Francisco': 'sf', 'San Diego': 'sd', 'Los Angeles': 'la',
              'Tampa Bay': 'tb', 'Green Bay': 'gb', 'New England': 'ne', 'Carolina': 'car', 'Cleveland': 'cle',
              'Houston': 'hou', 'Dallas': 'dal', 'Seattle': 'sea', 'Chicago': 'chi', 'Kansas City': 'kc', 'Washington': 'was',
              'Pittsburgh': 'pit', 'Oakland': 'oak', 'Miami': 'mia', 'Buffalo': 'buf', 'New Orleans': 'no', 'Cincinnati': 'cin',
              'Denver': 'den', 'Arizona': 'ari', 'Baltimore': 'bal', 'Tennessee': 'ten', 'Detroit': 'det', 'Indianapolis': 'ind',
              'Jacksonville': 'jac', 'Minnesota': 'min', 'Colorado': 'col', 'Vegas': 'vgs', 'Anaheim': 'ana', 'NY Yankees': 'NYY',
              'NY Mets': 'NYM', 'Chicago Sox': 'chw', 'Chicago Cubs': 'chc', 'Milwaukee': 'mil', 'St. Louis': 'stl', 'LA Dodgers': 'lad',
              'LA Angels': 'laa', 'Texas': 'tex', 'Columbus': 'cbj', 'Nashville': 'nsh'}

    def __init__(self, sport='', league=''):
        self.sportSel = sport
        self.FullDescription = {'sport': sport, 'league': league, 'time': True, 'separator': '', 'timeSeparator': 0, 'url': '', 'sport_separator': ''}
        self.league = league
        self.teamList = ['','']
        self.matchups = {'match1':{}}
        self.available_leagues = ['nfl', 'nhl', 'mlb', 'nba']

    def get_leagues(self):
        return self.available_leagues

    def description(self):
        for key, value in self.FullDescription.items():
            print(key + ": " + str(value))

    def listTeams(self):
        for item in self.teamList:
            print(item)

    def listMatchups(self):
        for key, value in self.matchups.items():
            print(key + ": " + str(value['team1']) + " at " + str(value['team2']))

    def readHtmlFileEspn(self):
        updatedScore = False
        try:
            f = urllib.request.urlopen(self.FullDescription['url'])
            # Debug
            # f = open("debugpathhere/nfl_scores_test.html")
        except:
            print("Unable to read page ", self.FullDescription['url'])
            exit

        #time.sleep(20)
        stringMatches = f.read()
        f.close()

        #print("\"events\":[{\"date\":\"")
        #splitLeague = (stringMatches.decode("utf-8")).split("\"events\":[{\"date\":\"")
        splitLeague = (stringMatches.decode("utf-8")).split("\"National Football League\",\"season\"")
        #splitMatches = (stringMatches.decode("utf-8")).split("<div class=""scoreboard-wrapper"">")
        splitMatches = splitLeague[1].split("\"competitions\":[{\"date\":")
        splitStats = splitMatches[14].split(",")

        f = open("testfile.txt", "w+")

        #for match_index in range(1,  len(splitMatches)):
        match_index = 1
        display_clock = splitMatches[match_index].split("displayClock\":\"")[1].split("\"")[0]
        score1 = splitMatches[match_index].split("\"homeAway\":\"home\"")[1].split("\"score\":\"")[1].split("\"")[0]
        score2 = splitMatches[match_index].split("\"homeAway\":\"away\"")[1].split("\"score\":\"")[1].split("\"")[0]
        team1_logo = splitMatches[match_index].split("\"logo\":\"")[1].split("\"")[0]
        team2_logo = splitMatches[match_index].split("\"logo\":\"")[2].split("\"")[0]

        print("Score Home = " + score1)
        print("Score Away = " + score2)
        print("Time Left = " + display_clock)
        print("Team 1 logo = " + team1_logo)
        print("Team 2 logo = " + team2_logo)
        print("")

        for a in splitStats:
           # print(a)
            if (a.find("displayClock") != -1):
                f.write("Display Clock = " + a + "\n")
            f.write(a)
            f.write("\n")

        '''
        f.write(splitMatches[1].split("\"score\":\"")[1])
        f.write("\n")
        f.write(splitMatches[1].split("\"score\":\"")[2])
        '''

    def readHtmlFile(self, teamToWatch='Montreal'):
        updatedScore = False

        try:
            f = urllib.request.urlopen(self.FullDescription['url'])
            # Debugscoreboard-wrapper
            # f = open("debugpathhere/nfl_scores_test.html")
        except:
            print("Unable to read page ", self.FullDescription['url'])
            exit

        stringMatches = f.read()
        splitMatches = (stringMatches.decode("utf-8")).split("left")

        for team in splitMatches[1:]:

            gameNotStarted = False

            if "%20at%20" in team:
                splitTeams = '%20at%20'
                timeLeft = team.split('(')[1].split(')')[0]
                gameNotStarted = True
            else:
                splitTeams = '%20%20'
                gameNotStarted = False

            try:
                team1 = team.split(splitTeams)[0].split("right")[0].replace("%20", " ")
                matchNumber = team1.split('=')[0]
                team1 = team1.split('=')[1]
                team2 = team.split(splitTeams)[1].split("(")[0].replace("%20", " ")

                if gameNotStarted:
                    team1Score = 0
                    team2Score = 0
                else:
                    team1Score = int(re.findall('\d+', team1)[0])
                    team2Score = int(re.findall('\d+', team2)[0])

                string1Score = str(team1Score)
                string2Score = str(team2Score)
                team1 = team.split(splitTeams)[0].split('=')[1].replace("%20", " ").replace(string1Score, "").lstrip('^ ').rstrip()
                tempTimeSep = team.split('(')[1].split(')')[0]

                if "FINAL" not in tempTimeSep:
                    if "END%20OF%20" in tempTimeSep:
                        separator = tempTimeSep.split("END%20OF%20")[1]
                        timeLeft = "0:00"
                    elif "IN" in tempTimeSep:
                        separator = tempTimeSep.split("%20IN%20")[1]
                        timeLeft = tempTimeSep.split("%20IN%20")[0]
                    else:
                        try:
                            separator = tempTimeSep.split("%20")[1]
                        except:
                            separator = tempTimeSep

                        timeLeft = tempTimeSep.split("%20")[0]

                else:
                    timeLeft = "0:00"
                    separator = "FINAL"

                team2 = team.split(splitTeams)[1].split("(")[0].replace("%20", " ").replace(string2Score, "").lstrip('^ ').rstrip()

            except(ValueError):
                print("Type Error ", team1Score)

            try:
                if ((self.matchups['match' + str(matchNumber)]['team1'].find(teamToWatch) != -1) or (self.matchups['match' + str(matchNumber)]['team2'].find(teamToWatch) != -1)):
                    if (self.matchups['match' + str(matchNumber)]['score1'] != team1Score) or (
                        self.matchups['match' + str(matchNumber)]['score2'] != team2Score):
                        updatedScore = True
            except:
                print("Exception")
                updatedScore = False

            self.matchups['match' + str(matchNumber)]= {'team1': team1, 'score1': team1Score, 'team2': team2, 'score2': team2Score, 'timeleft': timeLeft, 'separator': separator}

        return updatedScore

    def getScores(self):
        print("Scores")

    def getMatchDetail(self, matchup=1):
        try:
            return self.matchups['match' + str(matchup)]

        except:
            print("No matches found")

    def getMatchNumber(self, teamString):
        for i in self.matchups:
            if (self.matchups[i]['team1'] == teamString) or (self.matchups[i]['team2'] == teamString):
                return i.replace('match','')
        return -1

    def printMatch(self, matchup=1):
        try:
            if len(self.matchups['match' + str(matchup)]['team1']) > len(self.matchups['match' + str(matchup)]['team2']):
                lengthOfPrint = len(self.matchups['match' + str(matchup)]['team1'])
            else:
                lengthOfPrint = len(self.matchups['match' + str(matchup)]['team2'])

            print(self.matchups['match' + str(matchup)]['team1'] + " ", self.matchups['match' + str(matchup)]['score1'])
            print(self.matchups['match' + str(matchup)]['team2'] + " ", self.matchups['match' + str(matchup)]['score2'])
            print(self.matchups['match' + str(matchup)]['separator'])
            print(self.matchups['match' + str(matchup)]['timeleft'])

        except:
            print("No matches found")

    def get_cities_abrev(self, city):
        try:
            return self.cities[city]
        except:
            print("Error unable to find " + city + " in cities")
            print("Available names are:")
            print(self.cities)
            return ''

    def printAllMatches(self):
        for key, value in self.matchups.items():
            print("\n", key)
            self.printMatch(int(key.replace("match", "")))

    def getMatchups(self):
        matchups = []

        #sorted_matchups = sorted(self.matchups, key=str.replace("match", ""))

        #for key, value in self.matchups.items():
         #   matchups.append(self.cities[(self.matchups[key]['team1'])] + " @ " + self.cities[str(self.matchups[key]['team2'])])

        print("Len of matchups 2 = " + str(len(self.matchups)))
        for match_no in range (1, len(self.matchups) + 1):
            new_key = "match" + str(match_no)
            try:
                matchups.append(self.cities[(self.matchups[new_key]['team1'])] + " @ " + self.cities[str(self.matchups[new_key]['team2'])])
            except:
                print("Unable to find city....")

        print(matchups)

        return matchups

    def getTeamsScore(self, teamString):
        return teamString

    def printUrl(self):
        print(self.FullDescription['url'])

    def get_sport_separator(self):
        return self.FullDescription['sport_separator']

    def updateScores(self, matchup):

        return 0

class football(sportsClass):


    def __init__(self, league):
        sportsClass.__init__(self,sport='football',league='nfl')
        # sportsClass.__init__(self)
        self.FullDescription['url'] = 'http://www.espn.com/' + self.league + '/bottomline/scores'
        #self.FullDescription['url'] = 'http://www.espn.com/' + self.league + '/scoreboard'
        self.FullDescription['time'] = True
        self.FullDescription['separator'] = 'Quarter'
        self.FullDescription['timeSeparator'] = 15
        self.FullDescription['sport_separator'] = 'QTR'

        if self.league == 'nfl':
            self.FullDescription['league'] = 'nfl'
            self.teamList = ['ATL', 'GBY', 'CHI']
            self.matchups = {'match1':{}}
        elif self.league == 'cfl':
            self.FullDescription['league'] = 'cfl'
            self.teamList = ['MTL', 'CGY', 'OTT']
            self.matchups = {'match1':{}}
        elif self.league == 'ncaa':
            self.FullDescription['league'] = 'ncaa'
            self.teamList = ['CYR', 'MCH', 'FLO']
            self.matchups = {'match1':{}}

class hockey(sportsClass):

    def __init__(self, league):
        sportsClass.__init__(self,sport='hockey',league='nhl')
        self.FullDescription['url'] = 'http://www.espn.com/' + self.league + '/bottomline/scores'
        self.FullDescription['time'] = True
        self.FullDescription['separator'] = 'Period'
        self.FullDescription['timeSeparator'] = 20
        self.FullDescription['sport_separator'] = 'PER'

        if self.league == 'nhl':
            self.FullDescription['league'] = 'nhl'
            self.teamList = ['ATL', 'GBY', 'CHI']
            self.matchups = {'match1':{}}


class baseball(sportsClass):

    def __init__(self, league):
        sportsClass.__init__(self,sport='baseball',league='mlb')
        self.FullDescription['url'] = 'http://www.espn.com/' + self.league + '/bottomline/scores'
        self.FullDescription['time'] = True
        self.FullDescription['separator'] = 'Innings'
        self.FullDescription['timeSeparator'] = 0
        self.FullDescription['sport_separator'] = 'INI'

        if self.league == 'mlb':
            self.FullDescription['league'] = 'mlb'
            self.teamList = ['ATL', 'GBY', 'CHI']
            self.matchups = {'match1':{}}

class basketball(sportsClass):
    def __init__(self, league):
        sportsClass.__init__(self, sport='basketball', league='nba')
        self.FullDescription['url'] = 'http://www.espn.com/' + self.league + '/bottomline/scores'
        self.FullDescription['time'] = True
        self.FullDescription['separator'] = 'Quarters'
        self.FullDescription['timeSeparator'] = 0
        self.FullDescription['sport_separator'] = 'QTR'

        if self.league == 'nba':
            self.FullDescription['league'] = 'nba'
            self.teamList = ['ATL', 'LAC', 'CHI']
            self.matchups = {'match1': {}}

'''class soccer(sportsClass):

    def __init__(self):
        sportsClass.__init__(self,sport='soccer',league='mls')
        self.FullDescription['url'] = 'http://www.espn.com/' + self.league + '/bottomline/scores'
        self.FullDescription['time'] = True
        self.FullDescription['separator'] = 'Half'
        self.FullDescription['timeSeparator'] = 0


        if self.league == 'mls':
            self.FullDescription['league'] = 'mls'
            self.teamList = ['ATL', 'GBY', 'CHI']
            self.matchups = {'match1':{}}'''