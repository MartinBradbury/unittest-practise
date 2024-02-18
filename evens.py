# def even_number_of_evens(numbers):
#     """
#     Should Raise a TypeError if a list in not passed into the function
#     error message: "A list was not passed into the function"
#     if the list is empty it will return False
#     if the number of even numbers is odd - return False
#     if the numner of even numbers is even - return True
#     """

#     if isinstance(numbers, list):
#         if numbers == []:
#             return False
#         else:
#             evens = 0 # initialise evens as a variable and give it an initial value of 0

#             for n in numbers:  # write a for loop to loop over the number
#                 if n % 2 == 0:  # if the remainder when divided by 2 is = to 0 add 1 to the evens number
#                     evens += 1 #add 1 to evens in loop

#             if evens:
#                 return evens % 2 == 0 #return evens if when divided by 2 = 0
#             else:
#                 return False
#     else:
#         raise TypeError("A list was not passed into the function")

# if __name__ == "__main__":
#     print(even_number_of_evens(5))


# REFACTORED CODE BELOW

def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])
        
        return True if evens and evens % 2 == 0 else False

    else:
        raise TypeError("A list was not passed into the function")
    return None

if __name__ == "__main__":
    print(even_number_of_evens([2, 1, 4]))