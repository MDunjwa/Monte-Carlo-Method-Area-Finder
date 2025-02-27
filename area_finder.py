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
     
def find_actual_area(shape,width=0,length=0,diameter=0,radius1=0,radius2=0):
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
    
            

def main():
    valid_shapes = ["circle","square","rectangle","ellipse"]
    
    #print the shapes user can choose from
    print("\n")
    display_shapes(valid_shapes) 
    print("\n")
    
    #let user enter a number corresponding to a shape, but reprompt in cases when it isn't between 1 and 4
    shape_number = input("I choose: ").lower()
    while True:
        if 1 <= int(shape_number) <= 4:
            shape = select_shape(shape_number,valid_shapes)
            break
        else:
            shape_number = input("Invalid entry. Please enter a number between 1 and 4: ")
    print(f"You chose {shape}!")
    
    # get dimensions for particular shape from user
    
    

    

    # if shape == "circle":
    #     s = Shape(radius1=5)
    #     print(s.circle_area())
    # elif shape == "square":
    #     square = Shape(width=5)
    #     print(square.square_area())
    # elif shape == "rectangle":
    #     rectangle = Shape(width=5,height=20)
    #     print(rectangle.rectangle_area())
    # elif shape == "ellipse":
    #     ellipse = Shape(radius1=3,radius2=5)
    #     print(ellipse.ellipse_area())



if __name__ == "__main__":
    main()