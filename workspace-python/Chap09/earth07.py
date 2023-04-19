class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self):
        print(self.channel, self.volume, self.on)

    def setChannel(self, chnnel):
        self.channel = chnnel

    def getChannel(self):
        return self.channel

t = Television(9,10, True)
t.show()

t.setChannel(90)
t.show()


