class Plane(object):

    def __init__(self):
        self.isflying = True

    def land(self):
        self.isflying = False

    def take_off(self):
        if self.isflying == True:
            raise Exception('Plane cannot take off while flying')
        self.isflying = True
