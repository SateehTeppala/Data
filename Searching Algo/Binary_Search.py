'''
@author:Sateesh Teppala
Binary Search using Recurssion
'''
import random
def Binary_Search(array,low,high,key):

    if high>=low:
        mid = (high+low)//2
        if array[mid]==key:
            print(mid)
        elif array[mid]<key:
            return Binary_Search(array,mid+1,high,key)
        else:
            return Binary_Search(array,low,mid-1,key)

    else:
        return False

if __name__=="__main__":
    a = random.sample(range(1,50),5)
    a.sort()
    print(a)
    key = int(input("Enter Key To Search"))
    high =len(a)-1
    print(Binary_Search(a,0,high,key))