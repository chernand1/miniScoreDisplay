from fetchScores import football
from miniDisplayScore import displayScore
import time
from system_tools import get_char

myKey = get_char()

print("First one =")

while(1):
    a = myKey.get_key()
    print("Before myKey")
    print(a)
    print("After myKey = " + str(a))
    time.sleep(2)

#matchToWatch = football(league='nfl')
#matchToWatch.readHtmlFileEspn()
'''
mydisplayscore = displayScore()
mydisplayscore2 = displayScore()
mydisplayscore.createDevice(portNo='0', bgcolor="black", reset_pin='25', rotate_screen=180)
mydisplayscore2.createDevice(portNo='1', bgcolor="black", reset_pin='22', rotate_screen=180)
mydisplayscore.download_and_display_graphic("http://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/", "chi", "png")
mydisplayscore.download_and_display_graphic("http://a.espncdn.com/combiner/i?img=/i/teamlogos/nhl/500/", "chi", "png")
mydisplayscore2.download_and_display_graphic("http://a.espncdn.com/i/teamlogos/nfl/500/scoreboard/", "sea", "png")
'''



