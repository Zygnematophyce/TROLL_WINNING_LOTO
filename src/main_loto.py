"""
Program that allows you to create a grid of 5 digits and a
additional number for the loto game.
"""

import random

def create_loto_win_grid():
    """ Create a table of 5 randomly drawn numbers """
    win_array = list()
    for i in range(0, 5, 1):
        # A grid is 5 numbers from 1 to 49.
        random_number = random.randint(1, 49)

        # Change the number as long as the number is already in the list.
        while random_number in win_array:
            random_number = random.randint(1, 49)
        win_array.append(random_number)

    # tri ascendant sur la liste
    win_array.sort()

    # Add the complementary number between 1 to 10.
    win_array.append(random.randint(1, 10))

    # Returns the list of winning numbers.
    return win_array

def better_display(grid_list):
    """ Function that diplay the results. """
    for i in range(0, len(grid_list)-1):
        print("Le numéro {} est {}".format(i+1, grid_list[i]))

    print("Enfin le numéro complémentaire est", grid_list[-1])

def create_output_text(grid_list, path_file):
    """ Function to create text file with grid numbers. """
    with open(path_file+"numeros_gagnants.txt", "a") as f:
        f.write(str(grid_list))
        f.write("\n")

if __name__ == "__main__":
    print("Loto gagnant !")

    WIN_NUMBER = list()

    # Create loto grid.
    WIN_NUMBER = create_loto_win_grid()

    # Display numbers.
    better_display(WIN_NUMBER)

    # Create text file with all numbers.
    create_output_text(WIN_NUMBER, "results/")
