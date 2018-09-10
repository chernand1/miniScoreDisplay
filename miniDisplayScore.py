from luma.core import cmdline, error
from PIL import Image, ImageDraw, ImageFont
from luma.core.render import canvas
from luma.core.virtual import viewport
from subprocess import check_output
import urllib.request
#import msvcrt

class displayScore:

    def __init__(self):
        self.resolutionX = 96
        self.resolutionY = 64
        self.type ='luma'
        self.chip = 'ssd1331'
        self.bus = 'i2c'
        self.portNumber = '0'

    def createDevice(self, type='luma', chip='ssd1331', width='96', height='64',bus='spi', portNo='0', bgcolor="black"):

        self.resolutionX = width
        self.resolutionY = height
        self.type = type
        self.chip = chip
        self.bus = bus
        self.portNumber = portNo

        if type == 'luma':
            try:
                args = ('-d' + chip, '--width=' + width, '--height=' + height, '-i' + bus, '--spi-device= '+ portNo)
                parser = cmdline.create_parser(description='luma.examples arguments')
                args1 = parser.parse_args(args)
                self.device = cmdline.create_device(args1)
                #self.buffer = Image.new("RGBA", self.device.size, bgcolor)
                #self.device.display(self.buffer.convert(self.device.mode))
                self.virtual = viewport(self.device, width=self.device.width, height=self.device.height)
                return 0
            except error.Error as e:
                return e

    def clearscreen(self, color="white"):

        background = Image.new("RGBA", self.device.size, color)
        self.device.display(background.convert(self.device.mode))

        return 0

    def fonttype(self):
        return {'0': "code2000", '1': "FreePixel", '2': "pixelmix"}

    def print_characters(self, text, font, fontsize, posx=0, posy=0):

        fontsdir = "fonts/"
        makefont = ImageFont.truetype(fontsdir + font + ".ttf", fontsize)

        # virtual = viewport(self.device, width=self.device.width, height=self.device.height)

        with canvas(self.virtual) as draw:
            draw.text((posx, posy), text, font=makefont, fill="blue")
            #draw.text((30, posy+10), text, font=makefont, fill="red")
            #draw.text((60, posy+20), text, font=makefont, fill="green")

    def check_wifi_network(self):

        scanoutput = check_output(["iwlist", "wlan0", "scan"])

        try:
            urllib.request.urlopen('http://www.google.com/')
        except:
            print("Error: No internet connection")
            print("Check available SSID and connect")
            for line in scanoutput.split():
                if line.startswith(b'ESSID'):
                    ssid = line.split(b'"')[1]
                    print (ssid)
            return 0

        return 1
'''
    def display(self, image):
        self._last_image = image.copy()
        self.device.display(image)


    def savepoint(self):
        """
        Copies the last displayed image.
        """
        if self._last_image:
            self.savepoints.append(self._last_image)
            self._last_image = None
'''

'''class keyboard_input:

    def __init__(self):
        self.buffer = 'eof'
        self.is_kbhit = 0

    def key_pressed(self):
        self.is_kbhit = msvcrt.kbhit()
        return self.is_kbhit
'''