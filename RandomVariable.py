class RandomVariable:
    def __init__(self, tag, name):
        self.tag = tag
        self.name = name

    def __str__(self):
        return self.name + ', ' + self.tag
