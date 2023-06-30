from tkinter import *
import random

#array that stores the content of the Tic Tac Toe grid
grid = ["", "", "", "", "", "", "", "", ""]

#function that draws a circle based on a given coordinate which is here the mouse click
def circle(canvas, x1, y1):
  canvas.create_oval(x1, y1, x1 + 150, y1 + 150, outline="#7e4b8b", width=10)

#function that draws an X based on a given coordinate which is here a randomly generate square
def X(canvas, x1, y1):
  text = canvas.create_text(x1+100, y1+100, text="X", font=("Arial", 150), fill="#7e4b8b")

#function that checks who wins or if the game is over and displays the respective message
def checkWin():
  if ((grid[0] == "O" and grid[1] == "O" and grid[2] == "O") or (grid[3] == "O" and grid[4] == "O" and grid[5] == "O") or
      (grid[6] == "O" and grid[7] == "O" and grid[8] == "O") or (grid[0] == "O" and grid[3] == "O" and grid[6] == "O") or
      (grid[1] == "O" and grid[4] == "O" and grid[7] == "O") or (grid[2] == "O" and grid[5] == "O" and grid[8] == "O") or
      (grid[0] == "O" and grid[4] == "O" and grid[8] == "O") or (grid[2] == "O" and grid[4] == "O" and grid[6] == "O")):
    canvas.create_text(415, 400, text = "YOU WIN", font=("Arial", 100), fill="red")
  elif ((grid[0] == "X" and grid[1] == "X" and grid[2] == "X") or (grid[3] == "X" and grid[4] == "X" and grid[5] == "X") or
      (grid[6] == "X" and grid[7] == "X" and grid[8] == "X") or (grid[0] == "X" and grid[3] == "X" and grid[6] == "X") or
      (grid[1] == "X" and grid[4] == "X" and grid[7] == "X") or (grid[2] == "X" and grid[5] == "X" and grid[8] == "X") or
      (grid[0] == "X" and grid[4] == "X" and grid[8] == "X") or (grid[2] == "X" and grid[4] == "X" and grid[6] == "X")):
    canvas.create_text(415, 400, text = "YOU LOSE", font=("Arial", 100), fill="red")
  elif (grid[0] != "" and grid[1] != "" and grid[2] != "" and grid[3] != "" and grid[4] != "" and grid[5] != "" and 
        grid[6] != "" and grid[7] != "" and grid[8] != ""):
    canvas.create_text(415, 400, text = "GAME OVER", font=("Arial", 100), fill="red")


#simple AI move for the game
def simpleAI():
  emptyGrid = list()
  
  #check what squares are empty
  for i in range(9):
    if (grid[i] == ""):
      emptyGrid.append(i)

  #choose a random empty square
  if (len(emptyGrid)):
    num = random.choice(emptyGrid)
    print(num)

  #based on the square chosen, draw a square there
  if (num == 0):
    X(canvas, 100, 100)
    grid[0] = "X"
  if (num == 1):
    X(canvas, 300, 100)
    grid[1] = "X"
  if (num == 2):
    X(canvas, 500, 100)
    grid[2] = "X"
  if (num == 3):
    X(canvas, 100, 300)
    grid[3] = "X"
  if (num == 4):
    X(canvas, 300, 300)
    grid[4] = "X"
  if (num == 5):
    X(canvas, 500, 300)
    grid[5] = "X"
  if (num == 6):
    X(canvas, 100, 500)
    grid[6] = "X"
  if (num == 7):
    X(canvas, 300, 500)
    grid[7] = "X"
  if (num == 8):
    X(canvas, 500, 500)
    grid[8] = "X"

  checkWin()

#draw a circle where there is a mouse click
def handle_click(event):
  x = event.x
  y = event.y
 

  if ((x>100 and x<300 and y>100 and y<300) and grid[0] == ""):
    circle(canvas, 125, 125)
    grid[0] = "O"

  if ((x>300 and x<500 and y>100 and y<300) and grid[1] == ""):
    circle(canvas, 325, 125)
    grid[1] = "O"

  if ((x>500 and x<700 and y>100 and y<300) and grid[2] == ""):
    circle(canvas, 525, 125)
    grid[2] = "O"

 

  if ((x>100 and x<300 and y>300 and y<500) and grid[3] == ""):
    circle(canvas, 125, 325)
    grid[3] = "O"

  if ((x>300 and x<500 and y>300 and y<500) and grid[4] == ""):
    circle(canvas, 325, 325)
    grid[4] = "O"

  if ((x>500 and x<700 and y>300 and y<500) and grid[5] == ""):
    circle(canvas, 525, 325)
    grid[5] = "O"

 

  if ((x>100 and x<300 and y>500 and y<700) and grid[6] == ""):
    circle(canvas, 125, 525)
    grid[6] = "O"

  if ((x>300 and x<500 and y>500 and y<700) and grid[7] == ""):
    circle(canvas, 325, 525)
    grid[7] = "O"

  if ((x>500 and x<700 and y>500 and y<700) and grid[8] == ""):
    circle(canvas, 525, 525)
    grid[8] = "O" 

  checkWin()
  simpleAI()


root = Tk()

#define the canvas
canvas = Canvas(root, width=800, height=800, bg="#ae9da9", highlightthickness="20", highlightcolor="#7e4b8b")
canvas.pack()

#create the grid
text = canvas.create_text(400, 50, text="Tic Tac Toe", font=("Arial", 24), fill="#7e4b8b")
canvas.create_line(300, 100, 300, 700, fill="#aaaaaa", width="10")
canvas.create_line(500, 100, 500, 700, fill="#aaaaaa", width="10")
canvas.create_line(100, 300, 700, 300, fill="#aaaaaa", width="10")
canvas.create_line(100, 500, 700, 500, fill="#aaaaaa", width="10")

canvas.bind("<Button-1>", handle_click)

root.mainloop()

