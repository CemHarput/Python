def selection(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j

        arr[min],arr[i]=arr[i],arr[min]
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]





def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key
def quicksort(arr):
    less=[]
    equal=[]
    greater=[]
    if len(arr)>1:
        pivot=arr[0]
        for i in arr:
            if i<pivot:
                less.append(i)
            if i==pivot:
                equal.append(i)
            if i>pivot:
                greater.append(i)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return arr


def main():
 arr=[38,27,43,3,9,82,10]
 #arr=quicksort(arr)

 #insertion(arr)
 selection(arr)
 #bubbleSort(arr)

 for i in range(len(arr)):
    print("%d"%arr[i])




if __name__ == '__main__':
    main()
