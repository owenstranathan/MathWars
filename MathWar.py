import sfml as sf
import random
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
square_size = 80

class Number():
    def __init__(self, arg_val, size_x, size_y, pos_x, pos_y):
        self.value = arg_val
        self.shape = sf.RectangleShape(sf.Vector2(size_x,size_y))
        self.pos = sf.Vector2(pos_x, pos_y)
        self.shape.position = self.pos
        self.shape.outline_color = sf.Color.BLACK
        self.shape.outline_thickness = 3
        self.text = sf.Text(str(self.value))
        self.text.color = sf.Color.BLACK
        self.text.character_size = 30
        self.text.position = sf.Vector2(self.pos.x , self.pos.y)

    def draw(self, window):
        self.text.string = str(self.value)
        print self.text.position
        print self.shape.position
        window.draw(self.shape)
        window.draw(self.text)


class Board():
    def __init__(self, board_size):
        '''Define the board as a matirx of type 'Number' '''
        self.matrix = [[Number(random.randint(-9,9), square_size, square_size, i * square_size, j*square_size) for i in range(10)] for j in range(10)]
        self.size = board_size

'''GET THE NUMBERS DRAWN ON THE WINDOW AND CREATE AN INTERFACE FOR
    EXPERIMENTING WITH THE RULES OF THE GAME'''

class Window(sf.RenderWindow):
    def __init__(self, width, height, name):
        RenderWindow.__init__(sf.VideoMode(width, height), name)


def main():
    '''The main window'''
    window = sf.RenderWindow(sf.VideoMode(SCREEN_WIDTH,SCREEN_HEIGHT), "MathWars")
    '''The number matrix'''

    board = Board(10)

    window.clear(sf.Color.BLUE )

    while window.is_open:
        for event in window.events:
            if type(event) is sf.CloseEvent:
                window.close()

        for row in board.matrix:
            for number in row:
                print number.value ,
                number.draw(window)
            print '\n'


        window.display()




if __name__ == "__main__":
    main()
