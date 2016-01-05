class Airport(object):

    def __init__(self):
        self.planes = []

    def instruct_to_land(self, plane):
        plane.land()
        self.planes.append(plane)

    def instruct_to_take_off(self, plane):
        if plane not in self.planes:
            raise Exception("Plane is not at this airport")
        plane.take_off()
        self.planes.remove(plane)
