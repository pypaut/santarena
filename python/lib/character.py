class Character:
    def __init__(self):
        # Position
        self.posH = 0
        self.posW = 0

        # Size
        self.spriteH = 50
        self.spriteW = 50

        # Movement
        self.speed = 1

        # Object
        self.sprite = (self.posW, self.posH, self.spriteW, self.spriteH)

    def update(self):
        self.sprite = (self.posW, self.posH, self.spriteW, self.spriteH)
