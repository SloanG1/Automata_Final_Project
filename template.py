
# import pygame library
import pygame
import time
import random

# initialise the pygame font
pygame.font.init()

# Total window
screen = pygame.display.set_mode((700, 700))

# Title and Icon
pygame.display.set_caption("SUDOKU SOLVER")
img = pygame.image.load('icon2.png')
pygame.display.set_icon(img)

x = 0
y = 0
dif = 500 / 9
val = 0

#Starting Board
Sudoku_Board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)


def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

    # Function to draw required lines for making Sudoku Sudoku_Board


def draw():
    # Draw the lines

    for i in range(9):
        for j in range(9):
            if Sudoku_Board[i][j] != 0:
                # Fill blue color in already numbered Sudoku_Board
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

                # Fill Sudoku_Board with default numbers specified
                text1 = font1.render(str(Sudoku_Board[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    # Draw lines horizontally and vertically to form Sudoku_Board
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

    # Fill value entered in cell


def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))


# Raise error when wrong value entered
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


# Check if the value entered in board is valid
def valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True


# Solves the sudoku board using Backtracking Algorithm
def solve(Sudoku_Board, i, j):
    while Sudoku_Board[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1

        elif i == 8 and j == 8:  # if row and column are equal to 8
            return True  # return True

    pygame.event.pump()
    for it in range(1, 10):
        if valid(Sudoku_Board, i, j, it) == True:
            Sudoku_Board[i][j] = it
            global x, y
            x = i
            y = j
            # white color background\
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(Sudoku_Board, i, j) == 1:
                return True
            else:
                Sudoku_Board[i][j] = 0
            # white color background
            screen.fill((255, 255, 255))

            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False

# If Sudoku_Board is filled return True, else return False
def Sudoku_Board_full():
    return 0 in Sudoku_Board[0] or Sudoku_Board[1] or Sudoku_Board[2] or Sudoku_Board[3] or Sudoku_Board[4] or Sudoku_Board[5] or Sudoku_Board[6] or Sudoku_Board[7] or Sudoku_Board[8]


def modified_solver(Sudoku_Board, i, j):
    valid_solutions = []  # Create list for valid solutions
    while Sudoku_Board[i][j] != 0:  # Check to see if Sudoku_Board position is not 0
        if i < 8:  # if row is less than 8
            i += 1  # add one to row
        elif i == 8 and j < 8:  # if row is equal to 8 and column is less than 8
            i = 0  # set row equal to 0
            j += 1  # add one to row
        elif i == 8 and j == 8:  # if row and column are equal to 8
            return True  # return True

    # For each square on board
    if Sudoku_Board[i][j] == 0:
        # each empty square will check numbers 1-9 to see if valid
        for it in range(1, 10):
            if valid(Sudoku_Board, i, j, it) == True:  # Check to see if the number is True
                valid_solutions.append(it)  # If number works append to valid solutions

        if len(valid_solutions) == 1 and i < 9 and j < 9:
            # Check to see if there is only one valid solution
            Sudoku_Board[i][j] = valid_solutions[0]  # If only one valid solution add to Sudoku_Board
            modified_solver(Sudoku_Board, i, j)  # Call Function back

        elif i < 8 and j < 8:  # If row and column are less than 8
            i += 1  # Add one to row
            modified_solver(Sudoku_Board, i, j)  # Call Function back

        elif i == 8 and j < 8:  # If row is equal to 8 and column is less than 8
            i = 0  # Set row back to zero
            j += 1  # Add one to column
            modified_solver(Sudoku_Board, i, j)  # Call Function back

        elif i < 8 and j == 8:  # If row is less than 8 and column is equal to 8
            i += 1  # Add one to row
            modified_solver(Sudoku_Board, i, j)  # Call Function back

    if Sudoku_Board_full():  # If Sudoku_Board is Full
        i = 0  # Set row back to start
        j = 0  # Set column back to start
        modified_solver(Sudoku_Board, i, j)  # Call Function back

# Display instruction for the game
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))


# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
# The loop thats keep the window running
while run:

    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
        # Get the mouse position to insert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                Sudoku_Board = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # If D is pressed reset the board to default
            if event.key == pygame.K_d:

                # Variation of Sudoku Boards
                Board1 = [
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]

                Board2 = [
                    [4, 0, 0, 8, 0, 1, 2, 0, 0],
                    [3, 0, 1, 6, 7, 0, 0, 0, 0],
                    [0, 8, 7, 0, 4, 9, 0, 1, 0],
                    [5, 0, 0, 2, 8, 0, 1, 9, 6],
                    [0, 2, 0, 0, 0, 0, 7, 4, 5],
                    [0, 0, 0, 0, 0, 7, 8, 0, 0],
                    [0, 0, 4, 0, 2, 8, 0, 0, 0],
                    [0, 1, 5, 7, 6, 3, 4, 0, 0],
                    [6, 9, 0, 0, 0, 0, 3, 7, 0]
                ]

                Board3 = [
                    [2, 9, 0, 0, 7, 0, 0, 0, 4],
                    [5, 8, 0, 3, 0, 0, 0, 6, 0],
                    [7, 0, 3, 0, 0, 0, 8, 1, 9],
                    [8, 6, 5, 0, 0, 2, 0, 0, 0],
                    [0, 7, 4, 5, 9, 0, 1, 0, 6],
                    [1, 0, 0, 0, 0, 4, 5, 8, 0],
                    [0, 5, 0, 0, 2, 7, 9, 0, 0],
                    [4, 0, 2, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 6, 0, 3, 0, 0, 5]
                ]

                Board4 = [
                    [0, 9, 0, 0, 0, 2, 0, 1, 0],
                    [2, 0, 8, 0, 4, 0, 9, 3, 0],
                    [7, 0, 3, 1, 0, 6, 8, 0, 0],
                    [0, 0, 0, 3, 0, 0, 1, 4, 5],
                    [1, 8, 5, 0, 2, 9, 6, 0, 0],
                    [0, 7, 4, 0, 0, 1, 2, 0, 8],
                    [0, 0, 0, 2, 0, 0, 0, 8, 0],
                    [5, 0, 0, 9, 0, 0, 7, 6, 2],
                    [8, 0, 0, 6, 0, 3, 0, 0, 0]
                ]

                Board5 = [
                    [0, 0, 0, 2, 7, 0, 0, 9, 0],
                    [0, 9, 0, 4, 0, 5, 8, 1, 7],
                    [0, 0, 3, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 7, 0, 9, 1, 2, 3],
                    [0, 0, 4, 0, 1, 2, 0, 8, 0],
                    [1, 0, 0, 3, 5, 0, 0, 4, 0],
                    [6, 5, 0, 1, 0, 0, 4, 0, 0],
                    [0, 3, 2, 0, 6, 7, 9, 0, 1],
                    [9, 1, 0, 0, 0, 0, 0, 3, 8]
                ]

                Board6 = [
                    [9, 2, 6, 0, 1, 0, 0, 0, 5],
                    [0, 0, 0, 3, 9, 0, 0, 0, 0],
                    [0, 7, 0, 2, 6, 0, 8, 0, 1],
                    [0, 9, 7, 0, 0, 0, 0, 0, 0],
                    [3, 0, 2, 9, 5, 1, 6, 0, 7],
                    [0, 6, 0, 0, 0, 0, 0, 1, 0],
                    [2, 1, 0, 7, 0, 6, 5, 3, 8],
                    [0, 8, 0, 0, 2, 0, 4, 0, 9],
                    [0, 0, 0, 5, 0, 9, 1, 6, 0]
                ]

                Board7 = [
                    [0, 5, 4, 0, 7, 0, 0, 2, 6],
                    [0, 0, 2, 0, 4, 9, 8, 0, 1],
                    [0, 0, 0, 2, 5, 6, 0, 0, 0],
                    [4, 0, 7, 1, 3, 0, 6, 0, 5],
                    [0, 0, 0, 0, 0, 8, 7, 0, 0],
                    [0, 8, 3, 0, 6, 0, 0, 1, 0],
                    [2, 0, 0, 6, 8, 3, 0, 9, 0],
                    [6, 0, 0, 0, 1, 5, 0, 4, 0],
                    [0, 0, 1, 4, 2, 7, 0, 0, 0]
                ]

                Board8 = [
                    [0, 0, 0, 0, 2, 0, 5, 6, 8],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 7, 9, 1, 0, 3, 4, 2],
                    [4, 7, 0, 1, 3, 0, 0, 0, 0],
                    [0, 6, 2, 0, 9, 0, 0, 0, 0],
                    [0, 3, 0, 7, 6, 0, 2, 1, 0],
                    [0, 0, 5, 8, 0, 0, 0, 2, 6],
                    [7, 0, 0, 3, 0, 9, 8, 5, 0],
                    [8, 9, 1, 2, 5, 0, 0, 0, 3]
                ]

                Board9 = [
                    [5, 0, 1, 6, 0, 7, 9, 0, 0],
                    [0, 0, 9, 0, 0, 3, 2, 5, 0],
                    [8, 2, 7, 0, 9, 0, 0, 0, 0],
                    [9, 0, 2, 0, 5, 1, 3, 7, 0],
                    [3, 0, 0, 9, 8, 0, 0, 0, 0],
                    [0, 0, 5, 7, 0, 6, 0, 0, 0],
                    [4, 0, 6, 0, 7, 5, 0, 3, 2],
                    [0, 1, 0, 0, 0, 0, 7, 0, 5],
                    [0, 0, 3, 0, 0, 0, 1, 9, 6]
                ]

                Board10 = [
                    [0, 9, 1, 3, 0, 0, 0, 0, 2],
                    [0, 2, 0, 0, 0, 8, 9, 4, 0],
                    [0, 4, 5, 0, 0, 9, 1, 7, 8],
                    [4, 0, 9, 5, 0, 6, 0, 3, 0],
                    [0, 0, 2, 0, 0, 7, 8, 0, 0],
                    [5, 3, 8, 0, 0, 0, 4, 0, 7],
                    [9, 0, 0, 8, 0, 5, 7, 0, 4],
                    [6, 8, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 7, 0, 1, 0, 0, 6]
                ]

                Board = [Board1, Board2, Board3, Board4, Board5, Board6, Board7, Board8, Board9, Board10]
                Sudoku_Board = random.choice(Board)

                rs = 0
                error = 0
                flag2 = 0


    if flag2 == 1:
        start_time = time.time()  # Time Start
        if modified_solver(Sudoku_Board, 0, 0) == False:  # User can swap out modified_solver for the original solve function
            error = 1
        else:
            rs = 1
        flag2 = 0
        print("test")
        end_time = time.time()  # Time End
        final_time = end_time - start_time  # Final Time
        print(f"Total Time: {final_time}")  # Return Final Time
    if val != 0:
        draw_val(val)
        if valid(Sudoku_Board, int(x), int(y), val) == True:
            Sudoku_Board[int(x)][int(y)] = val
            flag1 = 0
        else:
            Sudoku_Board[int(x)][int(y)] = 0
            raise_error2()
        val = 0

    if error == 1:
        raise_error1()
    if rs == 1:
        result()
    draw()
    if flag1 == 1:
        draw_box()
    instruction()

    # Update window
    pygame.display.update()

# Quit pygame window
pygame.quit()
