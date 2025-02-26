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
    
        print("\nChoose one of the following shapes by typing its corresponding number, and we will estimate its area using the Monte Carlo method!")
        num = 1
        for shape in list_of_shapes:
            print(f"{num}. {shape}")
            num += 1
        print("\n")    

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
     
def main():
    valid_shapes = ["circle","square","rectangle","ellipse"]
    
    #print the shapes user can choose from
    display_shapes(valid_shapes) 
    
    #let user enter a number corresponding to a shape, but reprompt in cases when it isn't between 1 and 4
    shape_number = input("I choose: ").lower()
    while True:
        if 1 <= int(shape_number) <= 4:
            shape = select_shape(shape_number,valid_shapes)
            break
        else:
            shape_number = input("Invalid entry. Please enter a number between 1 and 4: ")
    print(f"You chose {shape}!")

    

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