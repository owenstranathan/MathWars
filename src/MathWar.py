import sfml as sf
import random
import sys
from enum import Enum

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 704
square_size = 64
##board_size = 10

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

owner = enum('PLAYER1', 'PLAYER2', 'NONE')

class Number():
    def __init__(self, arg_val, size_x, size_y, pos_x, pos_y):
    ##integer value of the number
        self.value = arg_val
    ##the tile for the number
        self.shape = sf.RectangleShape(sf.Vector2(size_x,size_y))
    ##position of  the shape
        self.pos = sf.Vector2(pos_x, pos_y)
    ##owner of the number
        self.owner = owner.NONE

    ##init shape
        self.shape.position = self.pos
        self.shape.outline_color = sf.Color.BLACK
        self.shape.outline_thickness = 1

    ##init text
        ##get the font
        try:
            font = sf.Font.from_file("../resources/abw.ttf")
        except:
            print "Could not load font"
            exit(1)

        ##make the text string equal to the number's value
        self.text = sf.Text(str(self.value))
        ##set the font
        self.text.font = font
        ##set text color
        self.text.color = sf.Color.BLACK
        ##set font size to be two-thirds the size of the numbers shape
        self.text.character_size = int(square_size * 0.66)
        ##set the position of the text to be as close to the middle as I care
        x = self.pos.x + (square_size/2-self.text.character_size/2)
        y = self.pos.y + (square_size/2-self.text.character_size/2)
        self.text.position = sf.Vector2( x , y)

    def draw(self, window):
        ##set the value of the test.string to reflect the number's value
        self.text.string = str(self.value)
        ##color code according to owner
        if self.owner is owner.PLAYER1:
            self.shape.fill_color = sf.Color.BLUE
        ##color code according to owner
        elif self.owner is owner.PLAYER2:
            self.shape.fill_color = sf.Color.RED
        ##draw the shape
        window.draw(self.shape)
        ##draw the text
        window.draw(self.text)
        '''
            NOTE:
            the position of shapes and text is internal to
            sfml. So the position of the shape/text does not need to be
            specified in the argument list of the window.draw(*args) function
        '''

class turn():
    '''
        NOTE:
        the turn class must be initialized with
        the player argument being
        either owner.PLAYER1 or owner.PLAYER2 ( 0 or 1)
        any deviation from this contract will result in undefined behavior
    '''
    def __init__(self, player):
        if player is owner.PLAYER1 or player is owner.PLAYER2:
            self.whos_turn = player


    def change():
        ##if it was player one's turn give control to player two
        if self.whos_turn is owner.PLAYER1:
            self.whos_turn = owner.PLAYER2
        ##if it was player two's turn give control to player one
        elif self.whos_turn is owner.PLAYER2:
            self.whos_turn = owner.PLAYER1


class Board():

    '''
        The board class is a matrix of
        'randomly' generated numbers between -9 and 9

    '''
    def __init__(self, board_size):
        '''
            Define the board as a matirx of type 'Number'
            do this by randomly generating a number between -9 and 9
        '''
        self.matrix =[
            [
                Number
                (
                    random.randint(-9,9), ##arg_val
                    square_size, ##size_x
                    square_size, ##size_y
                    i * square_size, ##pos_x
                    j*square_size   ##pos_y
                )
                for i in range(board_size)
            ]
            for j in range(board_size)
        ]

        ##store the size of the board
        self.size = board_size
        ##set the top left number to player one
        self.matrix[0][0].owner = owner.PLAYER1
        ##make player one positive and start with positive 9
        self.matrix[0][0].value = 9
        ##set the bottom right number to player 2
        self.matrix[self.size-1][self.size-1].owner = owner.PLAYER2
        ##make player two negative and start with negative 9
        self.matrix[self.size-1][self.size-1].value = -9

    def draw(self, window):
        for row in self.matrix:
            for number in row:
                number.draw(window)

'''GET THE NUMBERS DRAWN ON THE WINDOW AND CREATE AN INTERFACE FOR
    EXPERIMENTING WITH THE RULES OF THE GAME'''

class Window(sf.RenderWindow):
    def __init__(self, width, height, name):
        RenderWindow.__init__(sf.VideoMode(width, height), name)


def onLeftMouse(event, board):
    ##left click
    if event.pressed and event.button is sf.Mouse.LEFT:
        ##get mouse position
        pos = event.position
        ##get the board position of the click
        pos.x = pos.x / square_size
        pos.y = pos.y / square_size
        if board.turn is owner.PLAYER1:
            ##do some stuff
            pass
        board.matrix[pos.y][pos.x].shape.fill_color = sf.Color.YELLOW




def main():

    '''The main window'''
    window = sf.RenderWindow(sf.VideoMode(SCREEN_WIDTH,SCREEN_HEIGHT), "MathWars")
    '''The number matrix'''
    board_size = 10
    board = Board(board_size)


    window.clear(sf.Color.BLUE )

    while window.is_open:

        ##EVENT HANDLING LOOP
        for event in window.events:
            if type(event) is sf.CloseEvent:
                window.close()

            if type(event) is sf.MouseButtonEvent:
                onLeftMouse(event, board)

        ##DRAW BOARDS
        board.draw(window)



        window.display()




if __name__ == "__main__":
    main()
