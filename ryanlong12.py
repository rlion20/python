from operator import truediv


class television:
    minVolume = 0
    maxVolume = 0
    minChannel = 0
    maxChannel = 0

    def __init__(self, volume = 0, channel = 1):
        status = False
        muted = False
        self.volume = minVolume
        self.channel = minChannel
    def powerOn(self):
        status = True
        return status
    def powerOff(self):
        status = False
        return status
    def muted(self):
        muted = True
        return muted
    def unmuted(self):
        muted = False
        return muted
    def channel_up(self):
        if self.channel >= self.maxChannel:
             self.channel = self.minChannel
        else:
            self.channel += 1
        return True

