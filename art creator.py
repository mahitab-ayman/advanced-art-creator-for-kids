import pygame
import math
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import colorsys
import time

# Initialize Pygame
pygame.init()

# Initialize the mixer
pygame.mixer.init()

# Load and play the music
pygame.mixer.music.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\upbeat-happy-logo-2-versions-146604.mp3")
pygame.mixer.music.play(-1)  # Play the music infinitely
# Define the dimensions of the window
width, height = 900, 790

# Create the window
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))  # Fill the screen with white color

# Set the window caption
pygame.display.set_caption("Interactive Art Creator")

# Define drawing parameters
draw_color = (0, 0, 0)  # Start with black color
radius = 10
shape = 'circle'  # Default shape
draw_mode = 'free'  # Default draw mode to 'free'
gradient_mode = False  # Default gradient mode to False

# Define color options
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 105, 180), # Pink
    (255, 255, 0),  # Yellow
    (0, 0, 0),      # Black
    (218, 165, 32), # Golden
    (192, 192, 192), # Silver
    (173, 216, 230), # Light Blue
    (152, 251, 152), # Pale Green
    (255, 182, 193), # Light Pink
    (0, 255, 255),  # Cyan
    (128, 0, 128),  # Purple
    (255, 165, 0),   # Orange
]

# Create a gradient
def create_gradient(color1, color2):
    gradient = pygame.Surface((width, height))  # Create a new surface
    for y in range(height):
        blend = y / height  # This will range from 0 to 1, indicating how to blend the colors
        color = [(1 - blend) * color1[i] + blend * color2[i] for i in range(3)]  # Blend the draw color to white
        pygame.draw.line(gradient, color, (0, y), (width, y))
    return gradient

# Create color buttons
color_buttons = [(i*60+30, 30, 25) for i in range(len(colors))]  # create a button for each color

# Define brush sizes
brush_sizes = [5, 10, 15, 20, 25]

# Create brush size buttons
brush_buttons = [(width - 30, i * 60 + 30, size) for i, size in enumerate(brush_sizes)]

# Calculate the x-coordinate for the new buttons position
button_x = 30  # set this to any value you want

# Define the button size
button_width, button_height = 120, 60

# Calculate the y-coordinate for the eraser button
eraser_y = 30 + len(brush_sizes) * 50  # Decrease the multiplier to move the button up
eraser_button = pygame.Rect(button_x, eraser_y, button_width, button_height)


# Calculate the y-coordinate for the gradient button
gradient_y = eraser_y + button_height
gradient_button = pygame.Rect(button_x, gradient_y, button_width, button_height)

# Calculate the y-coordinate for the undo button
undo_y = gradient_y + button_height
undo_button = pygame.Rect(button_x, undo_y, button_width, button_height)

# Calculate the y-coordinate for the redo button
redo_y = undo_y + button_height  # 60 is the height of the undo button
redo_button = pygame.Rect(button_x, redo_y, button_width, button_height)

# Calculate the y-coordinate for the clear all button
clear_all_y = redo_y + button_height  # 60 is the height of the redo button
clear_all_button = pygame.Rect(button_x, clear_all_y, button_width, button_height)

# Calculate the y-coordinate for the export button
export_y = clear_all_y + button_height  # 60 is the height of the clear all button
export_button = pygame.Rect(button_x, export_y, button_width, button_height)
import_y = export_y + button_height  # 60 is the height of the export button
import_button = pygame.Rect(button_x, import_y, button_width, button_height)
text_y = import_y + button_height  # 60 is the height of the import button
text_button = pygame.Rect(button_x, text_y, button_width, button_height)

# Calculate the y-coordinate for the stop music button (place it above the eraser button)
stop_music_y = eraser_y - button_height  # Subtract the button_height to move it up
stop_music_button = pygame.Rect(button_x, stop_music_y, button_width, button_height)
# Calculate the y-coordinate for the increase brightness button
# Calculate the y-coordinate for the finish button (place it above the stop music button)
finish_y = stop_music_y - button_height  # Subtract the button_height to move it up
finish_button = pygame.Rect(button_x, finish_y, button_width, button_height)



# Define the brush size buttons' x-coordinate
brush_button_x = width - 50

# Create brush size buttons
brush_buttons = [(brush_button_x, i * 60 + 30, size) for i, size in enumerate(brush_sizes)]

# Calculate the starting y-coordinate for the shape buttons based on the last brush button
shape_buttons_y = (len(brush_sizes) * 60) + 30

# Adjust the x-coordinate for the shape buttons to match the brush buttons
shape_buttons = [(brush_button_x, shape_buttons_y + i * 60, s) for i, s in enumerate(['circle', 'rectangle', 'free', 'line', 'curve', 'triangle'])]
# Calculate the y-coordinate for the increase brightness button
# Calculate the x-coordinate for the increase brightness button (same as shape buttons)
# Calculate the x-coordinate for the increase brightness button (moved to left)
button_x = shape_buttons[0][0] - 60  # Adjust the subtraction value to move the button more or less to the left

# Calculate the y-coordinate for the increase brightness button (placed under the triangle button)
increase_brightness_y = shape_buttons[-1][1] + 60  # y-coordinate of the last shape button plus button height
increase_brightness_button = pygame.Rect(button_x, increase_brightness_y, button_width, button_height)
decrease_brightness_y = increase_brightness_y + button_height
decrease_brightness_button = pygame.Rect(button_x, decrease_brightness_y, button_width, button_height)
# Define font for buttons
# Load the icon images
eraser_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\erase.png")
gradient_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\mix.jpg")
undo_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\undo.jpg")
redo_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\redo.png")
clear_all_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\clear.png")

finish_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\finish.png")
text_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\text.jpg")
stop_music_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\stop music.png")
curve_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\curve.jpg")
# Load the icon images
circle_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\circle.png")
triangle_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\triangle.png")
darker_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\darker.png")
brighter_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\brighter.png")
line_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\line.png")
export_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\export.png")
import_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\import.png")
rectangle_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\rectangle.png")
draw_icon = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\draw.png")

# Define the desired width and height for the icons
icon_width, icon_height = 32, 32

# Resize the icons
eraser_icon = pygame.transform.scale(eraser_icon, (icon_width, icon_height))
gradient_icon = pygame.transform.scale(gradient_icon, (icon_width, icon_height))
undo_icon = pygame.transform.scale(undo_icon, (icon_width, icon_height))
redo_icon = pygame.transform.scale(redo_icon, (icon_width, icon_height))
clear_all_icon = pygame.transform.scale(clear_all_icon, (icon_width, icon_height))
curve_icon = pygame.transform.scale(curve_icon, (icon_width, icon_height))
text_icon = pygame.transform.scale(text_icon, (icon_width, icon_height))
stop_music_icon = pygame.transform.scale(stop_music_icon, (icon_width, icon_height))
draw_icon = pygame.transform.scale(draw_icon, (icon_width, icon_height))
circle_icon = pygame.transform.scale(circle_icon, (icon_width, icon_height))
triangle_icon = pygame.transform.scale(triangle_icon, (icon_width, icon_height))
darker_icon = pygame.transform.scale(darker_icon, (icon_width, icon_height))
brighter_icon = pygame.transform.scale(brighter_icon, (icon_width, icon_height))
line_icon = pygame.transform.scale(line_icon, (icon_width, icon_height))
export_icon = pygame.transform.scale(export_icon, (icon_width, icon_height))
import_icon = pygame.transform.scale(import_icon, (icon_width, icon_height))
rectangle_icon = pygame.transform.scale(rectangle_icon, (icon_width, icon_height))
finish_icon = pygame.transform.scale(finish_icon, (icon_width, icon_height))
font = pygame.font.Font(None, 32)

circle_text_surface = circle_icon
rectangle_text_surface = rectangle_icon
free_text_surface =  draw_icon
line_text_surface = line_icon
curve_text_surface = curve_icon
triangle_text_surface = triangle_icon

export_text_surface = export_icon
import_text_surface = import_icon
erase_text_surface = eraser_icon
gradient_text_surface = gradient_icon
undo_text_surface = undo_icon
redo_text_surface = redo_icon
clear_all_text_surface = clear_all_icon
finish_text_surface =finish_icon
text_text_surface = text_icon
stop_music_text_surface = stop_music_icon

# Create a surface for the increase brightness button
increase_brightness_text_surface = brighter_icon
decrease_brightness_text_surface = darker_icon
erase_text_surface = eraser_icon
gradient_text_surface = gradient_icon
undo_text_surface = undo_icon
redo_text_surface = redo_icon
clear_all_text_surface = clear_all_icon

text_text_surface = text_icon
stop_music_text_surface = stop_music_icon

# Create a surface for the increase brightness button

# Define shapes list
shapes = []
undo_stack = []

# Main loop
start_ticks = pygame.time.get_ticks()  # Starter tick
running = True
drawing = False
dragging = False
shape_position = None
gradient_color1 = None
gradient_color2 = None
triangle_base = None
text_inputting = False
user_text = ""
score = 0
# Define your balloon images
brush_icons = [
    pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\most small brush.jpg"),
    pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\smaller brush.png"),
    pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\more brush.png"),
    pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\big brush.png"),
    pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\the biggest brush.png"),
]
while running:
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if finish_button.collidepoint(position):  # Finish button is clicked
                finish_image = pygame.image.load("C:\\Users\\Mahitab.Ayman\\Documents\\Downloads\\comp\\ballon1.png")
                finish_image = pygame.transform.scale(finish_image, (width, height))
                screen.blit(finish_image, (0, 0))
                pygame.display.flip()
                time.sleep(40)  # Display the image for two minutes (120 seconds)            
            if undo_button.collidepoint(position):  # check if the undo button is clicked
                if shapes:  # If there are actions to undo
                    last_action = shapes.pop()  # Remove the last action from the shapes list
                    undo_stack.append(last_action)  # And add it to the undo stack
                    # Increase the score when undoing an action
                    score += 5
            elif redo_button.collidepoint(position):  # check if the redo button is clicked
                if undo_stack:  # If there are actions to redo
                    last_undone_action = undo_stack.pop()  # Remove the last undone action from the undo stack
                    shapes.append(last_undone_action)  # And add it back to the shapes list
                    # Increase the score when redoing an action
                    score += 5
            elif text_button.collidepoint(position):  # Text button is clicked
                root = tk.Tk()
                root.withdraw()  # Hide the main window
                user_text = simpledialog.askstring("Input", "Enter your text:")
                root.destroy()
                if user_text:
                    text_inputting = True
                    # Increase the score when adding text
                    score += 10
                dragging = False
            elif stop_music_button.collidepoint(position):  # Stop music button is clicked
                pygame.mixer.music.stop()
                # Increase the score when stopping the music
                score += 2
            elif text_inputting:  # User is inputting text
                shapes.append(('text',position, user_text, draw_color))
                text_inputting = False
                # Increase the score when adding text
                score += 10
           
            elif eraser_button.collidepoint(position):
                draw_color = (255, 255, 255)  # Eraser color (white)
                gradient_mode = False
                dragging = False
                # Increase the score when using the eraser
                score += 3
            elif increase_brightness_button.collidepoint(position):  # Increase brightness button is clicked
                for x in range(width):
                    for y in range(height):
                        r, g, b, _ = screen.get_at((x, y))
                        r = min(255, r + 30)
                        g = min(255, g + 30)
                        b = min(255, b + 30)
                        screen.set_at((x, y), (r, g, b))
                # Increase the score when increasing brightness
                score += 2
            elif decrease_brightness_button.collidepoint(position):  # Decrease brightness button is clicked
                for x in range(width):
                    for y in range(height):
                        r, g, b, _ = screen.get_at((x, y))
                        r = max(0, r - 30)
                        g = max(0, g - 30)
                        b = max(0, b - 30)
                        screen.set_at((x, y), (r, g, b))
                # Increase the score when decreasing brightness
                score += 2
            elif gradient_button.collidepoint(position):
                if gradient_color1 is None:
                    gradient_color1 = draw_color
                else:
                    gradient_color2 = draw_color
                    gradient = create_gradient(gradient_color1, gradient_color2)
                    shapes.append(('gradient', gradient))
                    gradient_color1 = None
                    gradient_color2 = None
                dragging = False
                # Increase the score when applying a gradient
                score += 5
            elif clear_all_button.collidepoint(position):  # Check if the "Clear All" button was clicked
                shapes.clear()  # Clear all shapes
                undo_stack.clear() 
                # Increase the score when clearing all shapes
                score += 5
            elif export_button.collidepoint(position):  # Export button is clicked
                pygame.image.save(screen, 'exported_image.png')  # Save the screen to a PNG file
                # Increase the score when exporting the image
                score += 5
            elif import_button.collidepoint(position):  # Import button is clicked
                root = tk.Tk()
                root.withdraw()  # Hide the main window
                file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*")])
                root.destroy()
                if file_path:
                    img = pygame.image.load(file_path)
                    imported_img = pygame.transform.scale(img, (width, height))
                    shapes.append(('image', imported_img))  # Add the imported image to the shapes list
                    # Increase the score when importing an image
                    score += 5
            else:
                # Check if a color button was clicked
                for i, (x, y, rad) in enumerate(color_buttons):
                    if math.hypot(x - position[0], y - position[1]) < rad:
                        draw_color = colors[i]
                        dragging = False
                        # Increase the score when selecting a color
                        score += 2
                        break
                # Check if a brush size button was clicked
                for i, (x, y, rad) in enumerate(brush_buttons):
                    if math.hypot(x - position[0], y - position[1]) < rad:
                        radius = brush_sizes[i]
                        dragging = False
                        # Increase the score when selecting a brush size
                        score += 2
                        break
                # Check if a shape button was clicked
                for i, (x, y, s) in enumerate(shape_buttons):
                    if pygame.Rect(x, y, button_width, button_height).collidepoint(position):
                        draw_mode = s
                        dragging = False
                        # Increase the score when selecting a shape
                        score += 3
                        break
                else:
                    dragging = True
                    shape_position = position
                    if draw_mode == 'free':
                        shapes.append(('circle', position, radius, draw_color))
                    elif draw_mode == 'curve':
                        shapes.append(('line', shape_position, position, draw_color))
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            if draw_mode == 'triangle':
                if triangle_base is None:
                    triangle_base = shape_position
                else:
                    shapes.append((draw_mode,triangle_base, shape_position, draw_color))
                    triangle_base = None
            shape_position = None
        elif event.type == pygame.MOUSEMOTION and dragging:
            position = pygame.mouse.get_pos()
            if draw_mode == 'free':
                shapes.append(('circle', position, radius, draw_color))
            elif draw_mode == 'curve':
                shapes.append(('line', shape_position, position, draw_color))
                shape_position = position
            elif shape_position is not None:
                # Remove the last shape if it's ours
                if shapes and shapes[-1][0] == draw_mode and shapes[-1][1] == shape_position:
                    shapes.pop()
                if draw_mode == 'circle':
                    rad = int(math.hypot(position[0] - shape_position[0], position[1] - shape_position[1]))
                    shapes.append((draw_mode, shape_position, rad, draw_color))
                elif draw_mode == 'rectangle':
                    rect = pygame.Rect(shape_position[0], shape_position[1], position[0] - shape_position[0], position[1] - shape_position[1])
                    shapes.append((draw_mode, rect, draw_color))
                elif draw_mode == 'line':
                    shapes.append((draw_mode, shape_position, position, draw_color))
                elif draw_mode == 'triangle' and triangle_base is not None:
                    shapes.append((draw_mode, triangle_base, position, draw_color))
                    triangle_base = None

   

    # Redraw everything
    screen.fill((255, 255, 255))
    
    for shape in shapes:
        if shape[0] == 'circle':
            pygame.draw.circle(screen, shape[3], shape[1], shape[2])
        elif shape[0] == 'rectangle':
            pygame.draw.rect(screen, shape[2], shape[1])
        elif shape[0] == 'line':
            pygame.draw.line(screen, shape[3], shape[1], shape[2])
        elif shape[0] == 'triangle':
            pygame.draw.polygon(screen, shape[3], [shape[1], shape[2], (shape[1][0], shape[2][1])])
        elif shape[0] == 'gradient':
            screen.blit(shape[1], (0, 0))
        elif shape[0] == 'image':
            screen.blit(shape[1], (0, 0))
        elif shape[0] == 'text':
           text_surface = font.render(shape[2], True, shape[3])
           screen.blit(text_surface, shape[1])  
  
  # Draw the imported image if the shape type is 'image'
    for i, (x, y, rad) in enumerate(color_buttons):
        pygame.draw.circle(screen, colors[i], (x, y), rad)
    for i, (x, y, rad) in enumerate(brush_buttons):
        brush_icon = pygame.transform.scale(brush_icons[i], (icon_width, icon_height))
        screen.blit(brush_icon, (x - icon_width // 2, y - icon_height // 2))
    pygame.draw.rect(screen, (0, 0, 0), eraser_button, 2)
    screen.blit(erase_text_surface, (eraser_button.x + (button_width - erase_text_surface.get_width()) // 2, eraser_button.y + (button_height - erase_text_surface.get_height()) // 2))
    pygame.draw.rect(screen, (0, 0, 0), gradient_button, 2)
    screen.blit(gradient_text_surface, (gradient_button.x + (button_width - gradient_text_surface.get_width()) // 2, gradient_button.y + (button_height - gradient_text_surface.get_height()) // 2))
    pygame.draw.rect(screen, (0, 0, 0), undo_button, 2)
  
    # ...
    screen.blit(undo_text_surface, (undo_button.x + (button_width - undo_text_surface.get_width()) // 2, undo_button.y + (button_height - undo_text_surface.get_height()) // 2))
    pygame.draw.rect(screen, (0, 0, 0), redo_button, 2)
    screen.blit(redo_text_surface, (redo_button.x + (button_width - redo_text_surface.get_width()) // 2, redo_button.y + (button_height - redo_text_surface.get_height()) // 2))
    pygame.draw.rect(screen, (0, 0, 0), clear_all_button, 2)
    screen.blit(clear_all_text_surface, (clear_all_button.x + (button_width - clear_all_text_surface.get_width()) // 2, clear_all_button.y + (button_height - clear_all_text_surface.get_height()) // 2))
    pygame.draw.rect(screen, (0, 0, 0), export_button, 2)
    screen.blit(export_text_surface, (export_button.x + (button_width - export_text_surface.get_width()) // 2, export_button.y + (button_height - export_text_surface.get_height()) // 2))
    pygame.draw.rect(screen, (0, 0, 0), import_button, 2)
    screen.blit(import_text_surface, (import_button.x + (button_width - import_text_surface.get_width()) // 2, import_button.y + (button_height - import_text_surface.get_height()) // 2))
    pygame.draw.rect(screen, (0, 0, 0), text_button, 2)
    screen.blit(text_text_surface, (text_button.x + (button_width - text_text_surface.get_width()) // 2, text_button.y + (button_height - text_text_surface.get_height()) // 2))
    pygame.draw.rect(screen, (0, 0, 0), increase_brightness_button, 2)
    screen.blit(increase_brightness_text_surface, (increase_brightness_button.x + (button_width - increase_brightness_text_surface.get_width()) // 2, increase_brightness_button.y + (button_height - increase_brightness_text_surface.get_height()) // 2))
    pygame.draw.rect(screen, (0, 0, 0), stop_music_button, 2)
    screen.blit(stop_music_text_surface, (stop_music_button.x + (button_width - stop_music_text_surface.get_width()) // 2, stop_music_button.y + (button_height - stop_music_text_surface.get_height()) // 2))
    pygame.draw.rect(screen, (0, 0, 0), decrease_brightness_button, 2)
    screen.blit(decrease_brightness_text_surface, (decrease_brightness_button.x + (button_width - decrease_brightness_text_surface.get_width()) // 2, decrease_brightness_button.y + (button_height - decrease_brightness_text_surface.get_height()) // 2))
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 70))
     
    pygame.draw.rect(screen, (0, 0, 0), finish_button, 2)
    screen.blit(finish_icon, (finish_button.x + (button_width - finish_icon.get_width()) // 2, finish_button.y + (button_height - finish_icon.get_height()) // 2))
    for i, (x, y, s) in enumerate(shape_buttons):
        pygame.draw.rect(screen, (0, 0, 0), (x - button_width // 2, y - button_height // 2, button_width, button_height), 2)
        if s == 'circle':
            screen.blit(circle_text_surface, (x - circle_text_surface.get_width() // 2, y - circle_text_surface.get_height() // 2))
        elif s == 'rectangle':
            screen.blit(rectangle_text_surface, (x - rectangle_text_surface.get_width() // 2, y - rectangle_text_surface.get_height() // 2))
        elif s == 'free':
            screen.blit(free_text_surface, (x - free_text_surface.get_width() // 2, y - free_text_surface.get_height() // 2))
        elif s == 'line':
            screen.blit(line_text_surface, (x - line_text_surface.get_width() // 2, y - line_text_surface.get_height() // 2))
        elif s == 'curve':
            screen.blit(curve_text_surface, (x - curve_text_surface.get_width() // 2, y - curve_text_surface.get_height() // 2))
        elif s == 'triangle':
            screen.blit(triangle_text_surface,(x - triangle_text_surface.get_width() // 2, y - triangle_text_surface.get_height() // 2))
    
    minutes = seconds // 60
    seconds = seconds % 60
    timer_text = font.render("Time: {:0>2}:{:0>2}".format(int(minutes), int(seconds)), True, (0, 0, 0))
    screen.blit(timer_text, (10, 100))  # adjust the position accordingly
    
    pygame.display.flip()
pygame.quit()