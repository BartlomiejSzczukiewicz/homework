class TV():
    def __init__(self,status = 'off',channel = 1):
        self.status = status
        self.channel = channel
    def show_status(self):
        return self.status
    def turn_on(self):
        self.status = 'on'
    def turn_off(self):
        self.status = 'off'
    def show_channel(self):
        return self.channel
    
tele = TV()

print(tele.show_status())
