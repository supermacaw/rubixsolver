
def bottom_ccw(cube):
    rotate_face_ccw(cube[5])
    rotate_faces_ccw(cube, [2,3,4,1], [[6,7,8], [6,7,8], [6,7,8], [6,7,8]])
    
def bottom_cw(cube):
    rotate_face_cw(cube[5])
    rotate_faces_cw(cube, [2,3,4,1], [[6,7,8], [6,7,8], [6,7,8], [6,7,8]])

def back_ccw(cube):
    rotate_face_ccw(cube[4])
    rotate_faces_ccw(cube, [3,0,1,5], [[2,5,8], [3,2,1], [0,3,6], [6,7,8]])
    
def back_cw(cube):
    rotate_face_cw(cube[4])
    rotate_faces_cw(cube, [3,0,1,5], [[2,5,8], [3,2,1], [0,3,6], [6,7,8]])

def up_ccw(cube):
    rotate_face_ccw(cube[0])
    rotate_faces_ccw(cube, [2,1,4,3], [[0,1,2], [0,1,2], [0,1,2], [0,1,2]])
    
def up_cw(cube):
    rotate_face_cw(cube[0])
    rotate_faces_cw(cube, [2,1,4,3], [[0,1,2], [0,1,2], [0,1,2], [0,1,2]])
    
def left_cw(cube):
    rotate_face_cw(cube[1])
    rotate_faces_cw(cube, [0, 2, 5, 4], [[0, 3, 6], [0, 3, 6], [0, 3, 6], [8, 5, 2]])

def left_ccw(cube):
    rotate_face_ccw(cube[1])
    rotate_faces_ccw(cube, [0, 2, 5, 4], [[0, 3, 6], [0, 3, 6], [0, 3, 6], [8, 5, 2]])

def front_cw(cube):
    rotate_faces_cw(cube, [0, 3, 5, 1], [[6, 7, 8], [0, 3, 6], [0, 1, 2], [2, 5, 8]])
    rotate_face_cw(cube[2])

def front_ccw(cube):
    rotate_faces_ccw(cube, [0, 3, 5, 1], [[6, 7, 8], [0, 3, 6], [0, 1, 2], [2, 5, 8]])
    rotate_face_ccw(cube[2])

def right_cw(cube):
    rotate_face_cw(cube[3])
    rotate_faces_cw(cube, [0,4,5,2], [[8,5,2], [0,3,6], [8,5,2], [8,5,2]])

def right_ccw(cube):
    rotate_face_ccw(cube[3])
    rotate_faces_ccw(cube, [0,4,5,2], [[8,5,2], [0,3,6], [8,5,2], [8,5,2]])


def rotate_face_ccw(face):
    face[0] = face[2]
    face[1] = face[5]
    face[2] = face[8]
    face[3] = face[1]
    face[4] = face[4]
    face[5] = face[7]
    face[6] = face[0]
    face[7] = face[3]
    face[8] = face[6]

def rotate_face_cw(face):
    face[2] = face[0]
    face[5] = face[1]
    face[8] = face[2]
    face[1] = face[3]
    face[4] = face[4]
    face[7] = face[5]
    face[0] = face[6]
    face[3] = face[7]
    face[6] = face[8]
    
def rotate_faces_ccw(cube, faces, faces_squares):
    return rotate_faces(cube, faces[::-1], faces_squares[::-1])
    
def rotate_faces_cw(cube, faces, faces_squares):
    return rotate_faces(cube, faces, faces_squares)
    
def rotate_faces(cube, faces, faces_squares):
    temp = [cube[faces[0]][i] for i in faces_squares[0]]
    for i in range(3):
        for j in [3, 2, 1]:
            cube[faces[(j + 1) % 4]][faces_squares[(j + 1) % 4][i]] = cube[faces[j]][faces_squares[j][i]]
    for i in range(3):
        cube[faces[1]][faces_squares[1][i]] = temp[i]
    return cube

def rotate_into(cube, from_face, from_squares, to_face, to_squares):
    temp = [cube[to_face][i] for i in to_squares]
    end_squares = []
    for i in range(3):
        cube[to_face][to_squares[i]] = cube[from_face][from_squares[i]]
        cube[from_face][from_squares[i]] = temp[i]
    return cube, 

# up_ccw(cube)
# print(print2D(cube))
# up_cw(cube)
# print(print2D(cube))
# 
# rotate_faces_cw(cube, [0, 3, 5, 1], [[6, 7, 8], [0, 3, 6], [0, 1, 2], [2, 5, 8]])
# rotate_faces_ccw(cube, [0, 3, 5, 1], [[6, 7, 8], [0, 3, 6], [0, 1, 2], [2, 5, 8]])
# print(print2D(cube))
# 
# bottom_ccw(cube)
# print(print2D(cube))
# bottom_cw(cube)
# print(print2D(cube))
# 
# right_ccw(cube)
# print(print2D(cube))
# right_cw(cube)
# print(print2D(cube))

