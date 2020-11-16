'''
@author:Sateesh Teppala
Binary Search using Recurssion
'''
def Binary_Search(array,low,high,key):

    if high>=low:
        mid = low+(high-low)//2
        if array[mid]==key:
            return mid
        elif array[mid]>key:
            return Binary_Search(array,low,mid-1,key)
        else:
            return Binary_Search(array,mid+1,high,key)
    else:
        return -1

if __name__=="__main__":
    a = [21, 98, 52, 45, 62, 42, 15, 78]
    a.sort()
    print(a)
    key = int(input("Enter Key To Search:"))
    high =len(a)-1
    r=Binary_Search(a,0,high,key)
    if r > -1:
        print(r)
    else:
        print(-1)