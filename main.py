import random
arr = random.sample(range(1,100),20)
print(arr)

def minmax(a):
    min = a[0]
    max = a[0]
    i = 1
    n = len(a)
    while i < n:
        if a[i]<min:
            min = a[i]
        elif a[i]>max:
            max = a[i]
        i = i+1
    return (min,max)


# def quicksort(a):
    
(min,max) = minmax(arr)
print("Largest of numbur in array is: " + str(max))
print("Smallest of numbur in array is: " + str(min))
