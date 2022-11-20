class Parallelogram (object):
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.S = Parallelogram.get_area(width, length)

    @staticmethod
    def get_area(width, length):
        return width * length


Square = Parallelogram(12, 10)
print(Square.S)


class Square (Parallelogram):

    @staticmethod
    def get_area(width, length):
        return width * width


Square = Parallelogram(12, 12)
print(Square.S)
