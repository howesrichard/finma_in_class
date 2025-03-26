a = "the dog barked "
x = 3
b = " times"
print(a + str(x) + b)

print(a + x + b)

def describe_dog_barks(times):
    """
    Returns a string describing how many times the dog barked.
    
    Args:
        times (int): The number of times the dog barked.
    
    Returns:
        str: A descriptive string.
    """
    a = "the dog barked "
    b = " times"
    return a + str(times) + b

# Example usage
print(describe_dog_barks(3))


# function to make a cat meow
def describe_cat_meows(times):
    """
    Returns a string describing how many times the cat meowed.
    
    Args:
        times (int): The number of times the cat meowed.
    
    Returns:
        str: A descriptive string.
    """
    a = "the cat meowed "
    b = " times"
    return a + str(times) + b