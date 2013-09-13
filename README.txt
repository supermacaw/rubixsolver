Ashvin Nair
Deepak Kumar
David Chang

Process:

First we set up a github repo so we could all collaborate. Then we divided the work into different parts: parsing, representation, rotation, input/interface, and generating random cubes. We could do this because of abstraction so we communicated to each other the contract of the methods and classes, and developed simultaneously.  Ashvin programmed the parsing.  David and Ashvin pair programmed the rotation.  Deepak programmed the interface and generating random cubes. 

Our vision was to have an elegant solution that allowed flexibility and ease of thinking through the problem. 

Our representation of cubes was basically a list of lists, where each sublist was a face. We abstracted rotation in general, but hard coded the values for the rotation of each face.  The 2D printing generates a folded view of the Rubix cube.  Generating random cubes was accomplished by randomly turning random faces 50 times, guaranteeing solvability.

To use the interface, it prompts you for turn direction (clockwise, counterclockwise), and face to turn(top, bottom, left, right, front, back).  After each turn, it prints the rotated cube.  