import pygame
import time
from area_through_formula import *

def display_shapes(list_of_shapes):
        """
        Displays the shapes whose area the program is capable of finding using the Monte Carlo Method

            Parameters:
                list_of_shapes(list): A list of the shapes the user can choose from

            Returns:
                Nothing. Prints a bullet form list of the shapes to the terminal and a prompt to choose one

        """
    
        print("\nChoose one of the following shapes by typing its name, and we will estimate its area using the Monte Carlo method!")
        num = 1
        for shape in list_of_shapes:
            print(f"{num}. {shape}")
            num += 1
        print("\n")    

def validate_shape(chosen_shape,accepted_shapes):
    """
    Checks whether the shape the user chose is valid. Does a spellcheck for possible errors. Reprompts user if neither of the first
    options work.

        Paremeters:
            chosen_shape (str): The shape entered by the user
            accepted_shapes (list): A list of the valid shapes

        Returns:
            chosen_shape (str): The shape entered by the user

    """

    while True:
        valid_shapes = ["circle","square","rectangle","ellipse"]        
        # chosen_shape = input().lower()
        if chosen_shape in valid_shapes:
            print(f"You chose {chosen_shape}!")
            return chosen_shape
        else:
            shape_meant = did_you_mean(chosen_shape,valid_shapes)
            if shape_meant in valid_shapes:
                ans = input (f"Did you mean {shape_meant}? [yes/no] ")
                if ans.lower() == "yes":
                    print(f"You chose {shape_meant}!")
                    return shape_meant
                elif ans.lower() == "no":                    
                    print(f"\"{chosen_shape}\" is not a valid choice. Try again \n")
                    time.sleep(1)
                else:
                    print(f"\"{ans}\" is not a valid answer. Try again ")
                    time.sleep(1)
            else:
                print(f"\"{chosen_shape}\" is not a valid choice. Try again \n")
                time.sleep(1)       

def did_you_mean(user_shape,list_of_shapes):
    similarity = []
    closest = None
    for shape in list_of_shapes:
        similar_points = 0
        original_shape = shape
        for letter in user_shape:
            if letter in shape:
                similar_points += 1
                shape = shape.replace(letter,"")
        similarity.append(similar_points)
    highest = max(similarity)
    #in the case of multiple words having the same similarity ranking, choose the one that is closest in length to user word
    if similarity.count(highest) > 1:
        first_highest_index = similarity.index(highest)
        first_len_difference = abs(len(user_shape)-len(list_of_shapes[first_highest_index]))
        for rating in range(len(similarity)):
            if similarity[rating] == highest:
                i = rating
                len_difference = abs(len(user_shape)-len(list_of_shapes[i]))
                if len_difference < first_len_difference:
                    first_len_difference = len_difference
                    closest = list_of_shapes[i]
                    #maybe make a list of shapes that fit for if there are multiple like in the case of "elepce". then validate among those
                    #shapes. if first letter is the same. of last letter is the same
    else:
        i = similarity.index(highest)
        return list_of_shapes[i]
    if closest != None:    
        return closest
    else: 
        return user_shape

def main():
    valid_shapes = ["circle","square","rectangle","ellipse"]

    display_shapes(valid_shapes) #1.show user their options
    chosen_shape = input("I choose: ").lower()

    shape = validate_shape(chosen_shape,valid_shapes)
    

    if shape == "circle":
        s = Shape(radius1=5)
        print(s.circle_area())
    elif shape == "square":
        square = Shape(width=5)
        print(square.square_area())
    elif shape == "rectangle":
        rectangle = Shape(width=5,height=20)
        print(rectangle.rectangle_area())
    elif shape == "ellipse":
        ellipse = Shape(radius1=3,radius2=5)
        print(ellipse.ellipse_area())



if __name__ == "__main__":
    main()