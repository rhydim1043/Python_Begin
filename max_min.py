import sys
def method_1(arr):
    int_min = sys.maxsize
    int_max = -sys.maxsize-1
    for i in arr:
        if i > int_max:
            int_max = i
        if i < int_min:
            int_min = i
    print("Maximum: " + str(int_max) + " | Minimum: " + str(int_min))
    
def method_2(arr):
    print("Maximum: " + str(max(arr)) + " | Minimum: " + str(min(arr)))
    
if __name__ == "__main__":
    arr = [20, 80, 64, 12, 105, 97]
    # method_1(arr)
    method_2(arr)