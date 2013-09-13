class Directions:
    """
    Class to represent directions that each face can move.
    """
    CLOCKWISE = 'Clockwise'
    COUNTERCLOCKWISE = 'Counterclockwise'

class Face:
    """
    Class to represent each face on rubix cube.
    """
    TOP = 'Top'
    LEFT = 'Left'
    FRONT = 'Front'
    RIGHT = 'RIGHT'
    BACK = 'Back'
    BOTTOM = 'Bottom'

class Move:
    """
    Class that represents a move on the rubix cube.
    Attributes include direction (clockwise, counterclockwise) and a face (top, left, front, right, back, bottom)
    """
    def __init__(self, direction, face):
        self.direction = direction
        self.face = face
    
    def getDirection(self):
        return self.direction
    
    def getFace(self):
        return self.face

def parse(filename = "cube.txt"):
    f = open(filename, 'r')
    lines = []
    for line in f:
        line = line.strip().split(",")
        lines.append([l.strip() for l in line])
    return lines

def print2D(cube):
    cubeString = ""
    for face in cube:
        for (index,square) in enumerate(face):
            if index % 3 == 0:
                cubeString += "\n"
            cubeString += square + "\t"
        cubeString += "\n\n"
    return cubeString
        
if __name__ == '__main__':
    cube = parse()
    print(cube)
    print(print2D(cube))
