from main import *

cube = parse()

def up_ccw(cube):
    rotate_face_ccw(cube[0])
    m = cube[1][:3]
    cube[1][:3] = cube[4][:3]
    cube[4][:3] = cube[3][:3]
    cube[3][:3] = cube[2][:3]
    cube[2][:3] = m
    return cube
    
def up_cw(cube):
    rotate_face_ccw(cube[0])
    m = cube[1][:3]
    cube[1][:3] = cube[2][:3]
    cube[2][:3] = cube[3][:3]
    cube[3][:3] = cube[4][:3]
    cube[4][:3] = m
    return cube
    
def left_cw(cube):
    rotate_face_ccw(cube[1])
    m = cube[1][:3]
    cube[1][:3] = cube[2][:3]
    cube[2][:3] = cube[3][:3]
    cube[3][:3] = cube[4][:3]
    cube[4][:3] = m

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

def rotate_into(from_face, from_squares, to_face, to_squares):
    triple = (face2[column], face2[column + 3], face2[column + 6])
    face2[0] = face1[0]
    face2[1] = face1[1]
    face2[2] = face1[2]

cube = up_ccw(cube)
print(cube)
cube = up_cw(cube)
print(cube)
