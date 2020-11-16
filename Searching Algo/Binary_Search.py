'''
@author:Sateesh Teppala
Binary Search using Recurssion
'''
def Binary_Search(array,low,high,key):

    if high>=low:
        mid = (high+low)//2
        if array[mid]==key:
            print(mid)
        elif array[mid]<key:
            return Binary_Search(array,mid+1,high,key)
        else:
            return Binary_Search(array,low,mid-1,key)
        return
    else:
        return 

if __name__=="__main__":
    a = [21, 98, 52, 45, 62, 42, 15, 78]
    a.sort()
    print(a)
    key = int(input("Enter Key To Search"))
    high =len(a)-1
    print(Binary_Search(a,0,high,key))