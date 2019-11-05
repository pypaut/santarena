import lib.constants as c

class Character():
    def __init__(self):
        # Position
        self.posH = 0
        self.posW = 0

        # Size
        self.spriteH = 50
        self.spriteW = 50

        # Object
        self.sprite = (self.posW, self.posH, self.spriteW, self.spriteH)


    def Update(self):
        self.sprite = (self.posW, self.posH, self.spriteW, self.spriteH)
