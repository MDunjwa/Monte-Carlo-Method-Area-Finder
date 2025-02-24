import pygame
import time

def choose_shape():
    """
    This function allows the user to choose a shape from a list of shapes

        Paremeters:
            No parameters

        Returns:
            chosen_shape (str): The shape entered by the user
    """

    while True:
        valid_shapes = ["circle","square","rectangle","ellipse"]        
        print("\nChoose one of the following shapes by typing its name, and we will estimate its area using the Monte Carlo method!")
        for shape in valid_shapes:
            print(f"• {shape}")
        print("\n")
        chosen_shape = input().lower()
        if chosen_shape in valid_shapes:
            print(f"You chose {chosen_shape}!")
            return chosen_shape
        else:
            shape_meant = did_you_mean(chosen_shape,valid_shapes)
            if shape_meant in valid_shapes:
                ans = input (f"Did you mean {shape_meant}? [yes/no]")
                if ans.lower() == "yes":
                    print(f"You chose {shape_meant}!")
                    return shape_meant
                else:
                    print(f"\"{chosen_shape}\" is not a valid choice. Try again\n")
                    time.sleep(1)
            else:
                print(f"\"{chosen_shape}\" is not a valid choice. Try again\n")
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

def choose_dimensions():
    pass

def main():
    shape = choose_shape()
    # print(did_you_mean("elepce",["circle","square","rectangle","ellipse"]))
if __name__ == "__main__":
    main()