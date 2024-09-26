# Personal Sticky Notes Project
import pygame, sys, random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Setup
Width, Height = 900, 700
NOTE_WIDTH, NOTE_HEIGHT = 200, 150
NOTE_COLOR = (70, 29, 124)
NOTE_BORDER_COLOR = (253, 208, 35)

# Screen
WINDOW = pygame.display.set_mode((NOTE_WIDTH, NOTE_HEIGHT))
pygame.display.set_caption('LSU Sticky Notes')

#Sticky Notes Class
class StickyNote:
    def __init__(self, x, y, text=''):
        self.rect = pygame.Rect(x, y, NOTE_WIDTH, NOTE_HEIGHT)
        self.color = NOTE_COLOR
        self.text = text
        self.is_moving = False
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, NOTE_BORDER_COLOR, self.rect, 3)  # Draw border
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

#Main Function
def main():
    notes = []
    looping = True 

    while looping:
        WINDOW.fill((0, 0, 0))  # Fill background with black
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Create new sticky note on mouse click
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                new_note = StickyNote(x, y, f"Note {len(notes) + 1}")
                notes.append(new_note)

            # Detect clicks on sticky notes
            for note in notes:
                if note.rect.collidepoint(event.pos):
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        note.is_moving = True
                        mouse_x, mouse_y = event.pos
                        offset_x = note.rect.x - mouse_x
                        offset_y = note.rect.y - mouse_y

                    elif event.type == MOUSEBUTTONUP and event.button == 1:
                        note.is_moving = False

                    elif event.type == MOUSEMOTION:
                        if note.is_moving:
                            mouse_x, mouse_y = event.pos
                            note.rect.x = mouse_x + offset_x
                            note.rect.y = mouse_y + offset_y
                            break

        # Draw all sticky notes
        for note in notes:
            note.draw(WINDOW)

        pygame.display.flip()  # Update the display

if __name__ == "__main__":
    main()