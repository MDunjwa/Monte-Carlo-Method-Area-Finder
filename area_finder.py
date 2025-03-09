import pygame
import time
from area_through_formula import *

def display_shapes(list_of_shapes):
        """
        Displays the shapes whose area the program is capable of finding using the Monte Carlo Method

            Parameters:
                list_of_shapes(list): A list of the shapes the user can choose from

            Returns:
                Nothing. Prints a numbered list of the shapes to the terminal and a prompt to choose one

        """
    
        print("Choose one of the following shapes by typing its corresponding number, and we will estimate its area using the Monte Carlo method!")
        num = 1
        for shape in list_of_shapes:
            print(f"{num}. {shape}")
            num += 1  

def select_shape(num_entered,our_shapes):
    """
    Chooses a shape based on the number the user entered. Reprompts the user if it is not a valid selection

    Parameters:
        num_entered (str): The number entered by the user
        our_shapes (list): A list of the valid shapes

    Returns:
        (str): The shape that corresponds with the number entered
    """

    return our_shapes[int(num_entered)-1]
     
def find_actual_area(shape,the_width=0,the_height=0,the_diameter=0,semi_major_axis=0,semi_minor_axis=0):
    """
    Finds the actual area of the chosen shape using the mathematical formula for it, instead of the Monte Carlo Method

        Parameters:
            shape (str): The shape whose actual area we are finding
            width (int): The width if the shape is a square or rectangle
            length (int): The length if the shape is arectangle
            diameter (int): The diameter if the shape is a circle
            radius1 (int): The semi-major axis if the shape is an ellipse
            radius2 (int): The semi-minor axis if the shape is an ellipse

        Returns:
            actual_area (float): The actual area of the shape, calculated through its area formula

    """
    match shape:
        case "circle":
            circle = Shape(diameter=the_diameter)
            return circle.circle_area()
        case "square":
              square = Shape(width=the_width)
              return square.square_area()
        case "rectangle":
              rectangle = Shape(width=the_width,height=the_height)
              return rectangle.rectangle_area()
        case "ellipse":
              ellipse = Shape(radius1=semi_major_axis,radius2=semi_minor_axis)
              return ellipse.ellipse_area()
  
# get dimensions for particular shape from user and draw it
def visualise():

    pygame.init()
    BACKGROUND_SIZE = height,width = 700,700
    background = pygame.display.set_mode(BACKGROUND_SIZE)  
    pygame.display.set_caption("Monte Carlo Area Finder")

    running = True
    while running:
         for event in pygame.event.get():
              if event.type == pygame.QUIT:
                   running = False
    
    pygame.quit()

def main():
    valid_shapes = ["circle","square","rectangle","ellipse"]
    
    #print the shapes user can choose from
    print("\n")
    display_shapes(valid_shapes) 
    print("\n")
    
    #let user enter a number corresponding to a shape, but reprompt in cases when it isn't between 1 and 4
    shape_number = input("I choose: ").lower()
    while True:
        try:
            if 1 <= int(shape_number) <= 4:
                shape = select_shape(shape_number,valid_shapes)
                break
            else:
                shape_number = input("Invalid entry. Please enter a number between 1 and 4: ")
        except ValueError:
             shape_number = input("Invalid entry. Please enter a number between 1 and 4: ")
             
    print(f"You chose {shape}!\n")
    visualise()

 
    

    





if __name__ == "__main__":
    main()