from engine import Player

# setting up pygame
import pygame

pygame.init()
pygame.display.set_caption("BattleShip Game")

# global variables

SQ_SIZE = 45
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE

INDENT = 10

WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
GREY = (40, 50, 60)
GREEN = (50, 200, 150)
WHITE = (250, 250, 250)
BLUE = (50, 150, 200)
ORANGE = (250, 140, 20)
RED = (250, 50, 100)
COLORS = {"U": GREY, "M": BLUE, "H": ORANGE, "S": RED}


# grid
def draw_grid(player, left=0, top=0, search=False):
    for i in range(100):
        x = left + i % 10 * SQ_SIZE
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, width=3)
        if search:
            x += SQ_SIZE // 2
            y += SQ_SIZE // 2
            pygame.draw.circle(SCREEN, COLORS[player.search[i]], (x, y), radius=SQ_SIZE // 4)


# function to draw ships onto the position grids
def draw_ships(player, left=0, top=0):
    for ship in player.ships:
        x = left + ship.col * SQ_SIZE + INDENT
        y = top + ship.row * SQ_SIZE + INDENT
        if ship.orientation == "h":
            width = ship.size * SQ_SIZE - 2 * INDENT
            height = SQ_SIZE - 2 * INDENT
        else:
            width = SQ_SIZE - 2 * INDENT
            height = ship.size * SQ_SIZE - 2 * INDENT
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(SCREEN, GREEN, rectangle, border_radius=INDENT)


player1 = Player()
player1.show_ships()

player2 = Player()
player2.show_ships()

# pygame loop
animating = True
pausing = False
while animating:

    # track user interaction
    for event in pygame.event.get():

        # user closes the pygame window
        if event.type == pygame.QUIT:
            animating = False

        # user presses key
        if event.type == pygame.KEYDOWN:

            # escape key -- Close the game
            if event.key == pygame.K_ESCAPE:
                animating = False

            # space bar -- Pause the game
            if event.key == pygame.K_SPACE:
                pausing = not pausing

    # execution
    if not pausing:
        # draw background
        SCREEN.fill(GREY)

        # draw search grids
        draw_grid(player1, search=True)
        draw_grid(player2, search=True, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN)

        # draw position grids
        draw_grid(player1, top=(HEIGHT - V_MARGIN) // 2 + V_MARGIN)
        draw_grid(player2, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN, top=(HEIGHT - V_MARGIN) // 2 + V_MARGIN)

        # draw ships onto grids
        draw_ships(player1, top=(HEIGHT - V_MARGIN) // 2 + V_MARGIN)
        draw_ships(player2, left=(WIDTH - H_MARGIN) // 2 + H_MARGIN)

        # update window
        pygame.display.flip()
