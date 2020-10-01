'''
Selection Sort
'''
import random
def SelectionSort(array):
    for step in range(len(array)):
        min = step
        for i in range(min+1,len(array)):
            if array[i] < array[min]:
                min = i

        array[step],array[min] = array[min],array[step]

if __name__ == "__main__":

    d = random.sample(range(-50,50),50)
    SelectionSort(d)
    print("Array sorted using Selection sort:")
    print(d)