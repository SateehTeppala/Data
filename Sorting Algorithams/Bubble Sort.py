'''
Optimized   Bubble Sort Algorithm
'''
def BubbleSort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

if __name__ == "__main__":
    a = [2,312,21,121,2,454,567,787,453,45,545,3,534,5,34]
    data = BubbleSort(a)
    print("Array Sorting using Bubble Sort")
    print(data)