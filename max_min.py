import sys
def method_1(arr):
    """
    This method iterates through the given array to find the maximum and minimum values.
    It initializes `int_min` and `int_max` to store the minimum and maximum values respectively.
    The method compares each element with `int_min` and `int_max` and updates them accordingly.
    Finally, it prints out the maximum and minimum values found in the array.
    """
    int_min = sys.maxsize
    int_max = -sys.maxsize-1
    for i in arr:
        if i > int_max:
            int_max = i
        if i < int_min:
            int_min = i
    print("Maximum: " + str(int_max) + " | Minimum: " + str(int_min))
    
def method_2(arr):
    """
    This method finds the maximum and minimum values in the given array using built-in Python functions.
    It utilizes the `max()` function to find the maximum value and the `min()` function to find the minimum value.
    The method then prints out these values.
    """
    print("Maximum: " + str(max(arr)) + " | Minimum: " + str(min(arr)))
    
if __name__ == "__main__":
    arr = [20, 80, 64, 12, 105, 97]
    # method_1(arr)
    method_2(arr)