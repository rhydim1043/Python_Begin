from essentials import *

def method_1(arr, n):
    """
    This method reverses the array by iteratively swapping the first and last elements,
    then the second and second-to-last, and so on, until reaching the middle of the array.
    """
    for i in range(int(n/2)):
        arr[i], arr[n-i-1] = swap(arr[i], arr[n-i-1])
    print(arr)
    
def method_2(arr):
    """
    Utilizes Python's built-in reverse() method of list objects to reverse the array in place.
    This is a direct and efficient approach leveraging Python's standard library.
    """
    arr.reverse()
    print(arr)
    
def method_3(arr):
    """
    Employs slicing to reverse the array. This method creates a new array that is a reversed
    copy of the original, using the slicing technique with a step of -1.
    """
    arr = arr[::-1]
    print(arr)
    
def method_4(arr):
    """
    Uses the built-in reversed() function, which returns an iterator that accesses
    the given sequence in the reverse order. The result is then converted back to a list.
    """
    arr = list(reversed(arr))
    print(arr)
    
def method_5(arr, start, end):
    """
    This method implements recursion to reverse the array. It swaps the first and last elements,
    then recursively calls itself for the subarray excluding the already swapped elements,
    until the start index is no longer less than the end index.
    """
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        method_5(arr, start+1, end-1)
    else:
        print(arr)

if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    n = len(arr)
    # method_1(arr, n)
    # method_2(arr)
    # method_3(arr)
    # method_4(arr)
    # method_5(arr, 0, n-1)
