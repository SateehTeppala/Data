def BubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]


if __name__ == "__main__":
    data = list(map(int,input().split()))
    BubbleSort(data)
    print("Array Sorting using Bubble Sort")
    print(data)