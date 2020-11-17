import struct
from gl import color

class Texture(object):
    
    def __init__(self, path):
        self.path = path
        self.readTexture()
    
    def readTexture(self):
        
        img = open(self.path, 'rb')
        img.seek(2 + 4 + 4)
        header_size = struct.unpack('=l', img.read(4))[0]
        img.seek(2 + 4 + 4 + 4 + 4)

        self.width = struct.unpack('=l', img.read(4))[0]
        self.height = struct.unpack('=l', img.read(4))[0]
        self.pixels = []
        
        img.seek(header_size)

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(img.read(1)) / 255
                g = ord(img.read(1)) / 255
                r = ord(img.read(1)) / 255
                self.pixels[y].append(color(r, g, b))
        
        img.close()
    
    def getColor(self, tx, ty, intensity = 1):

        if tx >= 0 and tx <= 1 and ty >= 0 and ty <= 1:
            x = int(tx * self.width - 1)
            y = int(ty * self.height - 1)

            return self.pixels[y][x]
        else:
            return color(0,0,0)
    
    def getDimensions(self):

        return self.height, self.width