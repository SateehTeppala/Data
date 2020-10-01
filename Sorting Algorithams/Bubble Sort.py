'''
Optimized   Bubble Sort Algorithm
'''
import random
def BubbleSort(array):
    for i in range(len(array)):
        swap = True
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
                swap = False
        if swap:
            break

if __name__ == "__main__":
    data = random.sample(range(-50,50),50)
    BubbleSort(data)
    print("Array Sorting using Bubble Sort")
    print(data)