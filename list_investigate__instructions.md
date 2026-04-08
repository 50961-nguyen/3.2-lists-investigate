## Setup
1. Create a new file called `list_investigate.py` in your **Github** folder

## Code
```python
"""
author:
date:
An investigation on lists!
"""

# Imports
import random
def lists_basics() -> None:
    """
    Investigating the basic, essential features of lists.

    Run the code to see how this works.
    """

    # To create an empty list
    my_list = []
    # To add an element to the list
    my_list.append(1)
    my_list.append(3)
    my_list.append(5)
    # To print out our list
    print(my_list)

    # To create a list that starts with things inside of it
    my_filled_list = ["Hello", "World", "Nice", "To", "Meet", "U"]
    # Again, print out the list
    print(my_filled_list)


    # This is where things get crazy!
    # Create a list
    favourite_shawarmas = ["Lazeez", "Osmos", "Shawarma Royale", "Homemade tbh"]
    # NOW! Let's loop through this list :O
    for favourite_shawarma in favourite_shawarmas:
        print(f'I like eating shawarma from {favourite_shawarma}') 

    # Let's try that again
    numbers = [11, 6, 3, 5, 4]
    for number in numbers:
        print(number)

def lists_useful_features() -> None:
    """
    # Some useful things to do with lists
    """
    # 1. Save all of the user's input
    user_inputs = []
    num_times = int(input("How many numbers would you like to input: "))
    for i in range(num_times):
        user_input = int(input("Enter a number: "))
        user_inputs.append(user_input)
    print(user_input)

    # 2. Turn a string into a list of words
    sentence = "The quick brown fox jumps over the lazy dog"
    words_in_sentence = sentence.split(" ")
    print(words_in_sentence)

    # 3. Get the number of elements in a list
    cool_list = [8, 'six', 7,  'five', 3, 'oh', 9]
    length_of_cool_list = len(cool_list)
    print(length_of_cool_list)

    # 4. Shuffle a list (We need import random at the top)
    # (5. Cool way to create a list)
    list_of_numbers = list(range(1, 11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(list_of_numbers)
    print(list_of_numbers)

    # 6. Sort a list
    list_of_numbers_sorted_again = sorted(list_of_numbers) 
    print(list_of_numbers_sorted_again)

def square_numbers() -> list[int]:
    """
    Loop through the list below, square each number, append that to a list called squared_nums, and return that list. 

    Return:
        list[int]: the list of each number squared from 1 to 49
    """
    nums = list(range(1, 50))
    squared_nums = []
    # TODO: write the code here. 

def main():
    """
    Main program to run the investigate work. Feel free to comment out the code if you want to test certain list features individually. 
    """
    lists_basics()
    lists_useful_features()
    # TODO: call square_numbers() and print the list

if __name__ == "__main__":
    main()
```