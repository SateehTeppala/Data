def select(a):
    for i in range(len(a)):
        m=i
        for j in range(i+1,len(a)):
            if a[m] > a[j]:
                m = j
        a[i],a[m] = a[m],a[i]
    return a
if __name__ == "__main__":
    a = list(map(int,input().split()))
    print(select(a))