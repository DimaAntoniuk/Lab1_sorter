class Vase():

    def __init__(self, volume, weight, material):
        self.volume = volume
        self.weight = weight
        self.material = material

    def __str__(self):
        return str(self.volume) + ' '\
                + str(self.weight) + ' '\
                + self.material
