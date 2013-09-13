import move
import random

class Directions:
    """
    Class to represent directions that each face can move.
    """
    CLOCKWISE = 'Clockwise'
    COUNTERCLOCKWISE = 'Counterclockwise'
    LIST = [CLOCKWISE, COUNTERCLOCKWISE]


class Face:
    """
    Class to represent each face on rubik cube.
    """
    TOP = 'Top'
    LEFT = 'Left'
    FRONT = 'Front'
    RIGHT = 'Right'
    BACK = 'Back'
    BOTTOM = 'Bottom'
    LIST = [TOP, LEFT, FRONT, RIGHT, BACK, BOTTOM]

class Move:
    """
    Class that represents a move on the rubik cube.
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

def get2DCube(cube):
    """
    Takes in a cube (list of lists of strings) and returns a string that prints it in 2D.
    The string separates each face with newlines.
    Each face is a 3x3 grid and each entry is the color of that square.
    """
    cubeString = ""
    for face in cube:
        cubeString += get2DFace(face) + "\n\n"
    return cubeString

def get2DFace(face):
    """
    Takes in a face (list of strings) of a rubik cube and prints it as a 3x3 grid.
    """
    faceString = ""
    for (index, square) in enumerate(face):
        if index % 3 == 0:
            faceString += "\n"
        faceString += square + "\t"
    return faceString

def get2DCubeFolded(cube):
    """
    Like get2DCube but prints 2D version that looks folded.
    """
    cubeString = ""
    
    #Print top face
    cubeString += get3Elements(cube[0], 0) + "\n" + get3Elements(cube[0], 1) + "\n" + get3Elements(cube[0], 2)
    
    cubeString += "\n\n"
    
    #Print left, front, top faces
    for row in range(0, 3):
        cubeString += get3Elements(cube[1], row) + "\t" + get3Elements(cube[2], row) + "\t" + get3Elements(cube[3], row)
        cubeString += "\n"
        
    cubeString += "\n"

    #Print bottom
    cubeString += get3Elements(cube[5], 0) + "\n" + get3Elements(cube[5], 1) + "\n" + get3Elements(cube[5], 2)

    cubeString += "\n\n"

    #Print back
    cubeString += get3ElementsReversed(cube[4], 0) + "\n" + get3ElementsReversed(cube[4], 1) + "\n" + get3ElementsReversed(cube[4], 2)

    return cubeString

def get3Elements(lst, index):
    """
    Given a list of strings and index, returns string of elements from 3*index to (3*index)+3 in list.
    """
    str = ""
    for square in lst[3*index:(3*index)+3]:
        str += square + "\t"
    return str

def get3ElementsReversed(lst, index):
    str = ""
    for square in lst[(3*index):(3*index)+3:-1]:
        str += square + "\t"
    return str

def generateRandomCube():
    randomCube = parse() #Start with solved cube.
    for i in range(0, 50):
        randomDirection = random.choice(Directions.LIST)
        randomFace = random.choice(Face.LIST)
        makeMove(randomCube, Move(randomDirection, randomFace))
    return randomCube

def makeMove(cube, moveChosen):
    """
    Makes moveChosen on cube.
    """
    if moveChosen.direction == Directions.CLOCKWISE:
        if moveChosen.face == Face.TOP:
            move.up_cw(cube)
        elif moveChosen.face == Face.LEFT:
            move.left_cw(cube)
        elif moveChosen.face == Face.FRONT:
            move.front_cw(cube)
        elif moveChosen.face == Face.RIGHT:
            move.right_cw(cube)
        elif moveChosen.face == Face.BACK:
            move.back_cw(cube)
        elif moveChosen.face == Face.BOTTOM:
            move.bottom_cw(cube)
    elif moveChosen.direction == Directions.COUNTERCLOCKWISE:
        if moveChosen.face == Face.TOP:
            move.up_ccw(cube)
        elif moveChosen.face == Face.LEFT:
            move.left_ccw(cube)
        elif moveChosen.face == Face.FRONT:
            move.front_ccw(cube)
        elif moveChosen.face == Face.RIGHT:
            move.right_ccw(cube)
        elif moveChosen.face == Face.BACK:
            move.back_ccw(cube)
        elif moveChosen.face == Face.BOTTOM:
            move.bottom_ccw(cube)
        
if __name__ == '__main__':
    inputCube = parse()
#     print(cube)
#     print(get2DCube(cube))
    
    while True:
        directionChosen = ""
        while directionChosen not in Directions.LIST:
            directionChosen = raw_input("Choose a direction to rotate: " + str(Directions.LIST) + "\n")
            
        faceChosen = ""
        while faceChosen not in Face.LIST:
            faceChosen = str(raw_input("Choose a face to rotate: " + str(Face.LIST) + "\n"))
            
        moveChosen = Move(directionChosen, faceChosen)
        makeMove(inputCube, moveChosen)
        print(get2DCubeFolded(inputCube))

        
