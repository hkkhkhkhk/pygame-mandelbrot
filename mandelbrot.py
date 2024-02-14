import pygame
import math
import cmath

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_size = (1000, 1000)
focus_coord = [0,0]
zoom_level = 1

# Create the Pygame window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Pygame Window")

MAX_ITERATION = 50
iterations_mat = [[0] * window_size[0] for _ in range(window_size[1])]

def remap(old_min, old_max, new_min, new_max, old_val):
    return (new_max - new_min)*(old_val - old_min) / (old_max - old_min) + new_min

def px_to_complex_no(x, y):
    real = remap(0, window_size[0], -2/zoom_level + focus_coord[0], 2/zoom_level + focus_coord[0], x)
    imag = remap(0, window_size[1], 2/zoom_level + focus_coord[1], -2/zoom_level + focus_coord[1], y)
    return complex(real, imag)

def iteration_to_col(it):
    val = remap(0,1, 0, 255, 0 if it == 1 else it)
    return (val,val,val)

def mandelbrot(c, x, y):
    z = 0
    iteration = 0
    while iteration < MAX_ITERATION:
        z = z**2 + c
        if abs(z) < 2:
            iteration += 1
        else:
            return iteration
    return MAX_ITERATION

def draw_mandelbrot():
    num_rows = len(iterations_mat)
    num_columns = len(iterations_mat[0])
    screen.fill(0)
    for x in range(1, num_rows+1):
        for y in range(1, num_columns+1):
            c = px_to_complex_no(x, y)
            it = mandelbrot(c, x, y)
            iterations_mat[x-1][y-1] = it / MAX_ITERATION
            screen.set_at((x, y), iteration_to_col(iterations_mat[x-1][y-1]))
    # Update the display
    pygame.display.flip()

draw_mandelbrot()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEWHEEL:
            x, y = pygame.mouse.get_pos()
            scroll_val = event.precise_y
            zoom_level += scroll_val/10
            mouse_complx_no = px_to_complex_no(x, y)
            focus_coord = [(mouse_complx_no.real), (mouse_complx_no.imag)]

            draw_mandelbrot()

            #print(event.x, event.y)

    # Your game logic goes here
