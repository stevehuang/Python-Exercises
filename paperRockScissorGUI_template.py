# Author: Steve Huang
# Date: August, 2013
#
# Description:
# Template for paper, rock, scissors GUI-ized!. 
# 
# The game is simple. You click on an icon of paper, rock, or scissor.
# Then the computer will select paper, rock, or scissor.
# Finally the results are shown. 
#
#
# How-to run game:
#
# To run the game, run the command:
#  python paperRockScissorGUI_template.py
#
# Make sure you have the pygame libraries installed.
#
#

import pygame
import random

# global variable that represents the display screen
screen = None

# global variable that has all the button objects 
buttonLayer = []

# size of the screen
size = 480, 200
# screen background color
white = 255, 255, 255
backgroundColor = white

# size of the font in the game
FontSize = 24

# initialize pygame
pygame.init()

# This is an object that represents a text box in the game
# A TextBox represents a box with text that is drawn to the screen 
class TextBox:
  text = ""     # the text to be drawn to the screen
  textBoxX = 0  # x-location to draw the text
  textBoxY = 0  # y-location to draw the text
  fontSize = 16 # default font size 
  
  # This function is called right after the object is created
  # input parameters: 
  # 1. text : text to be drawn to the screen
  # 2. x : x-location to draw to screen
  # 3. y : y-location to draw to screen
  # 4. fontsize : size of the font
  def __init__(self, text, x, y, fontsize):
    self.text = text
    self.textBoxX = x
    self.textBoxY = y
    self.fontSize = fontsize
  
  # This function says to draw the TextBox object to the screen
  # the location is already stored when the TextBox was created
  def Draw(self, screen):
    Font = pygame.font.Font(None, self.fontSize)  # create a default Font with the font size
    TextSurface = Font.render(self.text, 1, (0,0,0))  # write out the 
    screen.blit(TextSurface, (self.textBoxX, self.textBoxY))

# This object represents a button object. It'll display the picture of the button (like paper, rock)
# and handle input from the mouse using the ButtonHandler function
#
# To add a button in the game, 
# 1) create a button with a button name and the name of a jpg
# 2) and call the add function to specify the location of the button
# Example:     
#  # create the button with the picture
#  code: button = Button("Button_Paper", "paper.jpg")  
#  # place the button at location (10,100), 88 is width, 94 is the height of the button
#  # ButtonHandler is the function. The function is called when events are processed in the game 
#  code: button.Add(10, 100, 88, 94, ButtonHandler)
#
class Button:
  BoundBox = pygame.Rect(0,0, 100, 100)
  BackgroundColor = 125, 125, 125
  ButtonName = "Button"
  ButtonHandler = None 
  FontSize = 16
  ImageName = ""
  Image = None
  Font = 0
  FontX = 0
  FontY = 0
  
  # name: name of the button
  # imgName: jpg name of the image to display
  def __init__(self, name, imgName):
    self.ButtonName = name 
    self.ImageName = imgName
    self.Image = pygame.image.load(imgName).convert()

  # add the button to the screen at location (x,y)
  # width: width of the button (should match the width of the image)
  # height: height of the button (should match the height of the image)
  # handler: function to call for event processing
  def Add(self, x, y, width, height, handler=None):
    self.BoundBox = pygame.Rect(x,y, width, height)
    if handler != None:
      self.ButtonHandler = handler
   
  # arg1: pygame.event
  def EventHandler (self, event):
    # if the mouse button goes up, if it's within the bounding box
    # then print out something and call Handler 
    if (event.type == pygame.MOUSEBUTTONUP):
      if (self.ButtonHandler != None):
        if (self.BoundBox.collidepoint(pygame.mouse.get_pos()) == True):
          self.BackgroundColor = (125,125,125)
          self.ButtonHandler(self)
    if (event.type == pygame.MOUSEBUTTONDOWN):
      if (self.ButtonHandler != None):
        if (self.BoundBox.collidepoint(pygame.mouse.get_pos()) == True):
          self.BackgroundColor = (150,170,175)
  
  # draw the button image to the screen      
  def Draw(self,screen):
    screen.blit(self.Image, (self.BoundBox.left, self.BoundBox.top))

# global variables representing the outcomes for the game
user_wins = 0
cpu_wins = 1
tie_game = 2

# global variables representing paper, rock, or scissor
paper = 0
rock = 1
scissor = 2

# Function: RunPaperRockScissor()
#
# TODO(1): Fill in this function. The function does as follows:
#
# 1) This function will take as input the 
# user_selection as integer (0 = paper, 1 = rock, 2 = scissor).
# 2) Then it will choose a random value between [0-2] representing
# the computer's choice of paper, rock, scissor. 
# 3) Finally, compare the answers and determine the winner
# Return a list of the winner (0 = user_wins, 1 = cpu_wins, 2 = tie_game)
# and the computer's selection
#
def RunPaperRockScissor(user_selection):

#
# Fill in code here
#
#
  return None

# Function: ButtonHandler
#
# This function looks at the button (passed as input) and
# determines which button it was. Then, it will run the main game engine
# which determines who won by calling RunPaperRockScissor().
#
# Use Fill in the string Text with what you picked, the computer picked
# and the winner.
#
def ButtonHandler(button):
  global textInfo
  global FontSize
  user_answer = 0
  if (button.ButtonName == "Button_Paper"):   
    user_answer = paper
    Text = "You picked paper."
  elif (button.ButtonName == "Button_Rock"):
    user_answer = rock
    Text = "You picked rock."
  else:
    user_answer = scissor
    Text = "You picked scissor."

############################################
#
# TODO(2):
# Add code here to run the paper rock scissor game
# by calling the function RunPaperRockScissor(user_answer)
# Use the results and add the answer to the string Text
#
############################################

  textInfo = TextBox(Text, 50, 50, FontSize)
  return

# more global variables
textInfo = TextBox("Select paper, rock, or scissor", 50, 50, FontSize)


#################################
#
# Main Routine
#
################################     
def main():
  global screen
  global FontSize
  global textInfo
  global backgroundColor
  
  backgroundColor = white
  running = True
  screen = pygame.display.set_mode(size)
  
  # This is where we added buttons for the game. 
  
  # The first one is the paper button. This is button that is displayed
  # on the screen which the user clicks on with a mouse to select.
  butt = Button("Button_Paper", "paper.jpg")  # create the button with the picture
  butt.Add(10, 100, 88, 94, ButtonHandler)    # place the button at location (10,100)
  # we add this button to the button Layer which is just a list
  buttonLayer.append(butt)
  
  # TODO (3)
  #
  #############################################
  # Add code for the rock button below
  #
  # butt = Button("Button_Rock ....
  #  ... more code
  # we add this button to the button Layer which is just a list
  # buttonLayer.append(butt)
  #############################################
    
  #############################################
  # Add code for the scissor button below
  #
  # butt = Button("Button_Scissor ....
  #  ... more code
  # we add this button to the button Layer which is just a list
  # buttonLayer.append(butt)
  #############################################
    
  while running:
    screen.fill(backgroundColor)    
    
    # poll grabs one event. If nothing it returns NOEVENT
    event =pygame.event.poll()
    if event.type == pygame.QUIT:
      running = False
      
    # process the events. Pass the event to all the buttons by
    # cycling through each button in the buttonLayer list
    for button in buttonLayer:
      button.EventHandler(event)
    
    # drawing all the buttons  by 
    # cycling through each button in the buttonLayer list    
    for button in buttonLayer:
      button.Draw(screen)
    
    # draw information text to the screen
    textInfo.Draw(screen)
    
    pygame.display.flip()

  pygame.quit()

    
    
if __name__ == '__main__':
  main()
