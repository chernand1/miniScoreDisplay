from luma.core import cmdline, error
from PIL import Image, ImageDraw, ImageFont
from luma.core.render import canvas
from luma.core.virtual import viewport
import smbus2

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

    def lcddisplaytest(self, segment_numbers):

        I2C_COMM1 = 0x40
        I2C_COMM2 = 0xC0
        I2C_COMM3 = 0x80

        i2cbus = smbus2.SMBus(1)
        #a = i2cbus.i2c_rdwr(I2C_COMM1)
        i2cbus.write_byte(I2C_COMM1,0)
        #i2cbus.i2c_rdwr(I2C_COMM2)
        #i2cbus.i2c_rdwr(5)
        #i2cbus.i2c_rdwr(I2C_COMM3 + 0xf)

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
            draw.text((0, posy), text, font=makefont, fill="blue")
            draw.text((30, posy+10), text, font=makefont, fill="red")
            draw.text((60, posy+20), text, font=makefont, fill="green")

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
