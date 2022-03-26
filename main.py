'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  myturtle.width()
  myturtle.pu()
  myturtle.goto(top_left_x,top_left_y)
  myturtle.pd()

  for i in range(4):
    myturtle.forward(width)
    myturtle.right(90)

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.pu()
  myturtle.goto(x_start,y_start)
  myturtle.pd()
  myturtle.goto(x_end,y_end)

  
def drawCircle(myturtle=None, radius=0):
  myturtle.pu()
  myturtle.goto(0, -1)
  myturtle.pd()
  myturtle.circle(radius, steps=100 )
  myturtle.pu()
  
def setUpDartboard(myscreen=None, myturtle=None):
  myscreen.setworldcoordinates(-1, -1, 1, 1)
  drawSquare(myturtle, 2, -1, 1)
  drawLine(myturtle, 0, 1, 0, -1)
  drawLine(myturtle, -1, 0, 1, 0)
  drawCircle(myturtle, 1)

def throwDart(myturtle= None):
  x = random.uniform(-1, 1)
  y = random.uniform(-1, 1)
  myturtle.goto(x, y)
  myturtle.dot()

  if isInCircle(myturtle, 0, 0, 1) == False:
    myturtle.dot('blue')
    return False
  else:
    myturtle.dot('red')
    return True

def isInCircle(myturtle= None, circle_center_x=0, circle_center_y=0, radius=0):
  return (myturtle.distance(circle_center_x,circle_center_y)) <= 1

def playDarts(myturtle=None, player_1=0, player_2=0):
  for i in range(10):
    throwDart(myturtle)
    if(isInCircle(myturtle) == True):
      player_1 += 1
  print("Score for Player 1: ", player_1)
  for i in range(10):
    throwDart(myturtle)
    if(isInCircle(myturtle) == True):
      player_2 += 1
  print("Score for Player 2: ", player_2)
  
def montePi(myturtle=None, num_darts=0):
  inside_count = 0
  for i in range(num_darts):
    throwDart(myturtle)
    if(isInCircle(myturtle) == True):
      inside_count +=1
  approx_pi = (inside_count/ num_darts)*4
  print('Number of darts inside circle: ', inside_count)
  print('Your pi approximation: ', approx_pi)
  return approx_pi
    

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)
 
 # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)

    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...") 

    # Don't hide or mess with window while it's 'working'
    window.exitonclick()


main()
