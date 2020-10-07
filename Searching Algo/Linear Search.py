import random
def Linear_Search(arr,k):
    for i in range(0,len(arr)):
        if(a[i]==k):
            return "Found"
    return "Not Found"

if __name__ =="__main__":
    a = random.sample(range(20,50),15)
    print(a)
    k = int(input())
    print(Linear_Search(a,k))
