from fetchScores import football
from miniDisplayScore import displayScore
import time
from system_tools import get_char
from multi_axis_switch import multi_axis_switch

mySwitch = multi_axis_switch()

print("Current Switch States = " + str(mySwitch.switch_state()))
mySwitch.init_event()

while(1):
    time.sleep(0.5)
    if (mySwitch.return_sw_up() == 0):
        print("Up Switch pressed")
    if (mySwitch.return_sw_down() == 0):
        print("Down Switch pressed")
    if (mySwitch.return_sw_push() == 0):
        print("Switch pushed")


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



